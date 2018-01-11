# external import
import glob
import os
import h5py
import numpy as np
from sklearn.model_selection import KFold
import math

# internal import
import utils.DataPreprocessing as datapre

def fPatching(cfg, dbinfo):
    patchSize = cfg['patchSize']
    dRefPatches = np.empty((0, patchSize[0], patchSize[1]))
    dArtPatches = np.empty((0, patchSize[0], patchSize[1]))
    dRefPats = np.empty((0, 1))
    dArtPats = np.empty((0, 1))

    lDatasets = cfg['selectedDatabase']['dataref'] + cfg['selectedDatabase']['dataart']
    for ipat, pat in enumerate(dbinfo.lPats[0:2]):
        if os.path.exists(dbinfo.sPathIn + os.sep + pat + os.sep + dbinfo.sSubDirs[1]):
            for iseq, seq in enumerate(lDatasets):
                # patches and labels of reference/artifact
                tmpPatches, tmpLabels = datapre.fPreprocessData(os.path.join(dbinfo.sPathIn, pat, dbinfo.sSubDirs[1], seq),
                                                                patchSize, cfg['patchOverlap'], 1, 'volume')

                if iseq == 0:
                    dRefPatches = np.concatenate((dRefPatches, tmpPatches), axis=0)
                    dRefPats = np.concatenate((dRefPats, ipat * np.ones((tmpPatches.shape[0], 1), dtype=np.int)), axis=0)
                elif iseq == 1:
                    dArtPatches = np.concatenate((dArtPatches, tmpPatches), axis=0)
                    dArtPats = np.concatenate((dArtPats, ipat * np.ones((tmpPatches.shape[0], 1), dtype=np.int)), axis=0)
        else:
            pass

    assert(dRefPatches.shape == dArtPatches.shape and dRefPats.shape == dArtPats.shape)

    return dRefPatches, dArtPatches, dRefPats

def fSplitDataset(sSplitting, dRefPatches, dArtPatches, allPats, split_ratio, nfolds):
    train_ref_fold = []
    test_ref_fold = []
    train_art_fold = []
    test_art_fold = []

    # normal splitting
    if sSplitting == 'normal':
        nPatches = dRefPatches.shape[0]
        dVal = math.floor(split_ratio * nPatches)
        rand_num = np.random.permutation(np.arange(nPatches))
        rand_num = rand_num[0:int(dVal)].astype(int)

        test_ref_fold = dRefPatches[rand_num, :, :]
        train_ref_fold = np.delete(dRefPatches, rand_num, axis=0)
        test_art_fold = dArtPatches[rand_num, :, :]
        train_art_fold = np.delete(dArtPatches, rand_num, axis=0)

    # crossvalidation with mixed patient
    if sSplitting == "crossvalidation_data":
        if nfolds == 0:
            kf = KFold(n_splits=len(np.unique(allPats)))
        else:
            kf = KFold(n_splits=nfolds)

        for train_index, test_index in kf.split(dRefPatches):
            train_ref, test_ref = dRefPatches[train_index], dRefPatches[test_index]
            train_art, test_art = dArtPatches[train_index], dArtPatches[test_index]

            train_ref_fold.append(train_ref)
            train_art_fold.append(train_art)
            test_ref_fold.append(test_ref)
            test_art_fold.append(test_art)

    elif sSplitting == 'crossvalidation_patient':
        unique_pats = np.unique(allPats)

        for ind_split in unique_pats:
            train_index = np.where(allPats != ind_split)[0]
            test_index = np.where(allPats == ind_split)[0]
            train_ref, test_ref = dRefPatches[train_index], dRefPatches[test_index]
            train_art, test_art = dArtPatches[train_index], dArtPatches[test_index]

            train_ref_fold.append(train_ref)
            train_art_fold.append(train_art)
            test_ref_fold.append(test_ref)
            test_art_fold.append(test_art)

    train_ref_fold = np.asarray(train_ref_fold, dtype='f')
    train_art_fold = np.asarray(train_art_fold, dtype='f')
    test_ref_fold = np.asarray(test_ref_fold, dtype='f')
    test_art_fold = np.asarray(test_art_fold, dtype='f')

    return train_ref_fold, test_ref_fold, train_art_fold, test_art_fold

def run(cfg, dbinfo):
    patchSize = cfg['patchSize']
    sOutsubdir = cfg['subdirs'][3]
    sOutPath = cfg['selectedDatabase']['pathout'] + os.sep \
               + ''.join(map(str, patchSize)).replace(" ", "") + os.sep + sOutsubdir
    sDatafile = sOutPath + os.sep + ''.join(map(str, patchSize)).replace(" ", "") + '.h5'

    # if h5 file exists
    if glob.glob(sDatafile):
        with h5py.File(sDatafile, 'r') as hf:
            train_ref = hf['train_ref'][:]
            train_art = hf['train_art'][:]
            test_ref = hf['test_ref'][:]
            test_art = hf['test_art'][:]
            patchSize = hf['patchSize'][:]

    else:
        # perform patching
        dRefPatches, dArtPatches, dAllPats = fPatching(cfg, dbinfo)

        print(dRefPatches.shape)
        print(dArtPatches.shape)
        print(dAllPats.shape)

        # perform splitting
        train_ref, test_ref, train_art, test_art = fSplitDataset(cfg['sSplitting'], dRefPatches, dArtPatches, dAllPats, cfg['dSplitval'], cfg['nFolds'])

        # save to h5 file
        if cfg['lSave']:
            with h5py.File(sDatafile, 'w') as hf:
                hf.create_dataset('train_ref', data=train_ref)
                hf.create_dataset('test_ref', data=test_ref)
                hf.create_dataset('train_art', data=train_art)
                hf.create_dataset('test_art', data=test_art)
                hf.create_dataset('patchSize', data=patchSize)
