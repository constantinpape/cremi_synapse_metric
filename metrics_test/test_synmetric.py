import sys
import numpy as np
from make_testdata import make_groundtruth, make_predictions

sys.path.append('../cremi_python/')
from cremi.evaluation import Clefts


def single_test(gt_file, prediction_file):
    clefts = Clefts( prediction_file.read_clefts(),
            gt_file.read_clefts() )
    stats_fp = clefts.acc_false_positives()
    stats_fn = clefts.acc_false_negatives()
    adgt = stats_fp['mean']
    adf  =stats_fn['mean']
    print "ADGT:", adgt
    print "ADF:", adf
    print "CREMI-Score:", (adgt + adf) / 2


def test_near_and_far_fp(correct_resolution = True):
    if correct_resolution:
        print "Eval with correct resolution"
    else:
        print "Eval with incorrect resolution"
    gt_file = make_groundtruth(True)
    near_fp_file = make_predictions( (0, 75, 56), correct_resolution)
    far_fp_file  = make_predictions( (12, 320, 413), correct_resolution )
    print "Stats for near false positive"
    single_test(gt_file, near_fp_file)
    print "Stats for far false positive"
    single_test(gt_file, far_fp_file)


if __name__ == '__main__':
    test_near_and_far_fp(False)
