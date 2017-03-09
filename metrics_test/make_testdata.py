import sys
from skimage.draw import circle
import numpy as np

sys.path.append('../cremi_python/')
import cremi.io as io
import cremi.Volume as Volume

shape = (20,512,512)
syn_radius = 5

def make_groundtruth(correct_resolution = True):
    # fill gt with ignore labels (for whatever reason this is not 0...)
    gt = 0xffffffffffffffff * np.ones(shape, dtype = 'uint64')
    # make one gt synapse
    rr, cc = circle(20, 20, syn_radius)
    gt[0, rr, cc] = 1

    if correct_resolution:
        vol = Volume(gt, resolution = (40.,4.,4.) )
        gt_name = 'gt_correct_res.h5'
    else:
        vol = Volume(gt)
        gt_name = 'gt_incorrect_res.h5'
    cremi_f = io.CremiFile('../data/%s' % gt_name, 'w')
    cremi_f.write_clefts(vol)
    return cremi_f

def make_predictions(fp_pos, correct_resolution = True):
    prediction = 0xffffffffffffffff * np.ones(shape, dtype = 'uint64')

    # make tp synapse prediction
    rr, cc = circle(22, 18, syn_radius)
    prediction[0, rr, cc] = 1

    # make fp synapse prediction
    rr, cc = circle(fp_pos[1], fp_pos[2], syn_radius)
    prediction[fp_pos[0], rr, cc] = 2

    if correct_resolution:
        vol = Volume(prediction, resolution = (40.,4.,4.) )
        prediction_name = 'prediction_correct_res_%s.h5' % '_'.join(map(str, fp_pos))
    else:
        vol = Volume(prediction)
        prediction_name = 'prediction_incorrect_res_%s.h5' % '_'.join(map(str, fp_pos))
    cremi_f = io.CremiFile('../data/%s' % prediction_name, 'w')
    cremi_f.write_clefts(vol)
    return cremi_f
