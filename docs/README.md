# Evaluation of a base of 3D multiple-object tracking (AB3DMOT) 

[![Preprint](https://img.shields.io/badge/Preprint-Research%20Square-blue)](https://www.researchsquare.com/article/rs-9150527/latest)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

<img src="https://kovalp.github.io/eval-ab-3d-mot/logo-vicomtech.svg" width="192" alt="logo">

Evaluation part of the AB3DMOT by Xinshuo Weng [original repository](https://github.com/xinshuoweng/AB3DMOT).
The package is dedicated to calculation of the tracking quality metrics for 3D tracking
with KITTI data set. Apart from the refactored evaluation part of the AB3DMOT, 
a binary *Cla*ssifier of the tracking results *v*ia *I*nstrumented *A*ssociation (ClavIA)
can be used on the same tracker.

## Supporting publication

Using the codes from this repository, the user can reproduce the results of the publication
[ClavIA](#citation).

## Installation

[Clone the repository](https://github.com/kovalp/eval-ab-3d-mot),
then execute `uv sync` standing in the root folder.
Note that you might need to [install the package manager `uv`](https://docs.astral.sh/uv/) by 
Astral Software Inc. After installation a number of entry points are exposed in the 
shell. To reproduce the results of the [Supporting publication](#supporting-publication)
the following command-line scripts are used

  - `run-ab-3d-mot-with-clavia`
  - `batch-run-ab-3d-mot`
  - `batch-run-ab-3d-mot-annotations`

The entry points expose the `--help` option producing brief usage descriptions. For example,

```shell
run-ab-3d-mot-with-clavia --help
```

produces

<img src="https://kovalp.github.io/eval-ab-3d-mot/help-usage.png" width="1030" alt="help-usage">

## Compute F1-scores 

Evaluation with the original ClavIA and the reference ClearMOT methodologies can be preformed.  

### Compute F1-scores with ClavIA

To compute the F1 scores with ClavIA, please run

```shell
run-ab-3d-mot-with-clavia assets/annotations/kitti/training/*.txt
```

This command executes the instrumented AB-3D-MOT tracker consuming KITTI annotations.
The output of the tracking is evaluated using ClavIA methodology. After a minute 
the script produces the terminal output 

```terminaloutput
Confusion matrix TP 30601 TN 592 FP 0 FN 70
     accuracy 0.997761
    precision 1.0000
       recall 0.9977
     f1-score 0.9989
```

By default, we run for a *car* object category. To select the *cyclist* or *pedestrian*
category, use the option `--category-obj`, or `-c` for short

```shell
run-ab-3d-mot-with-clavia assets/annotations/kitti/training/*.txt -c cyclist
```

This time, the script runs faster and produces 

```terminaloutput
     ...
     f1-score 0.9969
```

By default, the tracker is provided with category-dependent parameters as in
the [reference implementation](https://github.com/xinshuoweng/AB3DMOT).
However, the script `run-ab-3d-mot-with-clavia` allows to adjust the association
parameters of the pure AB-3D-MOT tracker such as association threshold and 
matching algorithm via command-line options `--threshold`, `-t` and `--algorithm`, `-a`
correspondingly. For example, to run the tracker with the association threshold $-0.2$
using the Hungarian matching algorithm on pedestrians, we should command

```shell
run-ab-3d-mot-with-clavia assets/annotations/kitti/training/*.txt -c pedestrian -t -0.2 -a hungarian
```

This produces terminal output ending with  

```terminaloutput
     ...
     f1-score 0.9404
```

### Compute F1-scores with ClearMOT

To compute the F1 scores with ClearMOT, please run

```shell
batch-run-ab-3d-mot assets/detections/kitti/point-r-cnn-training/car/*.txt
batch-eval-ab-3d-mot assets/annotations/kitti/training/*.txt
```

The first command runs the pure AB-3D-MOT tracker consuming detections of the *car* objects category.
The result of the tracking will be stored in the files `tracking-kitti/car/*.txt`.
The second command runs the ClearMOT evaluation using the tracking output of the car category
and the corresponding split (training split) of KITTI annotations.
After about 10 minutes, the evaluation produces a final report including the F1 score

```terminaloutput
...
Recall                                                                    0.8839
Precision                                                                 0.9521
F1                                                                        0.9167
False Alarm Rate                                                          0.1594
...
```

To compute the F1 scores in cyclist category, please run

```shell
batch-run-ab-3d-mot assets/detections/kitti/point-r-cnn-training/cyclist/*.txt
batch-eval-ab-3d-mot assets/annotations/kitti/training/*.txt -c cyclist
```

The first command runs the pure AB-3D-MOT tracker consuming detections of the *cyclist* objects category.
The result of the tracking will be stored in the files `tracking-kitti/cyclist/*.txt`.
The second command runs the ClearMOT evaluation using the tracking output of the cyclist category
and the corresponding split of KITTI annotations. Final report includes the F1 score

```terminaloutput
...
F1                                                                        0.8390
...
```

By default, the tracker is provided with category-dependent parameters as in
the [reference implementation](https://github.com/xinshuoweng/AB3DMOT).
However, the script `batch-run-ab-3d-mot` allows to adjust the association
parameters of the pure AB-3D-MOT tracker such as association threshold and 
matching algorithm via command-line options `--threshold`, `-t` and `--algorithm`, `-a`
correspondingly. For example, to run the tracker with the association threshold $-0.2$
using greedy matching algorithm on pedestrians, we command

```shell
batch-run-ab-3d-mot assets/detections/kitti/point-r-cnn-training/pedestrian/*.txt -t -0.2 -a greedy
batch-eval-ab-3d-mot assets/annotations/kitti/training/*.txt -c pedestrian 
```

Final report includes the F1 score

```terminaloutput
...
F1                                                                        0.8047
...
```

Apart from the detections, the pure AB-3D-MOT tracker could be fed with KITTI annotations.
To run the pure AB-3D-MOT consuming annotations we use the script 
`batch-run-ab-3d-mot-annotations`. For example, to run the tracker for pedestrian category
with the association threshold $-0.3$ using the Hungarian matching algorithm, 
we execute two commands 

```
batch-run-ab-3d-mot-annotations assets/annotations/kitti/training/*.txt -c pedestrian -t -0.3 -a hungarian
batch-eval-ab-3d-mot assets/annotations/kitti/training/*.txt -c pedestrian
```

Final report of the ClearMOT contains the $F1=0.9576$

```terminaloutput
...
F1                                                                        0.9576
...
```

Note that the experiments run with different association parameters (threshold and matching algorithms)
are stored to the same files. Therefore, we recommend removing tracking and evaluation results before
each experiment

```shell
rm -rf tracking-kitti/ evaluation-kitti/
```

## Citation

If you use this work, please cite:

```biblatex
@online{clavia_2026,
  title = {Simple evaluation of association quality in tracking by detection},
  url = {https://www.researchsquare.com/article/rs-9150527/latest},
  doi = {https://dx.doi.org/10.21203/rs.3.rs-9150527/v1},
  abstract = {Evaluating multiple-object trackers is challenging due to the variable number of quantities involved and the mixed discrete--continuum nature of the problem. Existing methodologies primarily address detection and tracking challenges. These challenges aim at the whole computer-vision pipelines as opposed to sole tracker algorithms. Modern tracker algorithms can get sophisticated enough to merit stand-alone analysis. The most critical part of the tracker is an association procedure. The outcome of the association procedure affects the tracking quality almost entirely. We propose a simple quality assessment framework to probe the association quality of trackers. The framework relies on a minimal, query-oriented instrumentation of the tracker. The instrumentation exposes the tracker internal association decisions allowing for a binary classification of the detection-target matches. The proposed methodology is easy to implement, requires little computational overhead and agrees with the well known ClearMOT metrics. The comparison is demonstrated through the open-source, ready-to-use software packages we provide.},
  eprint = {10.21203/rs.3.rs-9150527}
  eprinttype = {Research Square},
  author = {Koval, Peter and Aranjuelo Ansa, Nerea and Javierre del Rio, Patricia and Menendez Arechalde, Ainhoa},
  year = {2026},
}
```

