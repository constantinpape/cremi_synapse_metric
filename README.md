# Tests for the Cremi Synapse Metrics

Tests with toy example data:
Groundtruth which has a single synapse + Prediction which has a true positive and a false positive
detection.
Testing for FP near and far from the gt synapse (-> ideally shouldn't influence the score!).
Also testing for the correct resolution (40., 4., 4.) set in the prediction file (Incorrect Resoultion uses the default value (1., 1., 1.)).

|                      | ADGT | ADF | CREMI-Score |
|----------------------|-----:|----:|------------:|
| Correct Resolution   |      |     |             |
| Near FP              |123.9 |2.5  |63.2         |
| Far FP               |1010.3|2.5  |506.4        |
| Incorrect Resolution |      |     |             |
| Near FP              |123.9 |0.6  |62.3         |
| Far FP               |1010.3|0.6  |505.4        |

## Conclusion

The ADGT is highly susceptible to the distance of false positives to the nearest GT synapse (which should not matter above a certain threshold).
The ADF depends on the resolution set in the prediction volume, which might make the evaluation not objective (I don't really think this is the case, but we should recheck...).
