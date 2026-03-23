# Evaluation of a base of 3D multiple-object tracking (AB3DMOT) 

Evaluation part of the AB3DMOT by Xinshuo Weng [original repository](https://github.com/xinshuoweng/AB3DMOT).
The package is dedicated to calculation of the tracking quality metrics for 3D tracking
with KITTI data set. Apart from the refactored evaluation part of the AB3DMOT, 
a binary *Cla*ssifier of the tracking results *v*ia *I*nstrumented *A*ssociation (ClavIA)
can be used on the same tracker.

## Supporting publication

Using the codes from this repository, the user can reproduce the results of the publication
"Simple evaluation of association quality in tracking-by-detection",
by Peter Koval, Nerea Aranjuelo Ansa, Particia Javierre del Rio, and Ainhoa Menendez Arechalde.

## Installation

Clone the repository, then execute `uv sync` standing in the root folder of the repository.
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

<img src="https://kovalp.github.io/eval-ab-3d-mot/assets/help-usage.png" width="192" alt="help-usage">

## Compute F1-scores 

To compute the F1 scores with ClavIA, please run

```shell
run-ab-3d-mot-with-clavia assets/annotations/kitti/training/*.txt
```

This command executes the instrumented AB-3D-MOT tracker consuming KITTI annotations.
The output of the tracking is evaluated using ClavIA methodology. After a minute 
the script should produce 

```terminaloutput
Confusion matrix TP 30601 TN 592 FP 0 FN 70
     accuracy 0.997761
    precision 1.0000
       recall 0.9977
     f1-score 0.9989
```

By default, a *car* object category is selected. To select the *cyclist* or *pedestrian*
category, use the option `--category-obj`, or `-c` for short

```shell
run-ab-3d-mot-with-clavia assets/annotations/kitti/training/*.txt -c cyclist
```

This time, the script runs faster and produces 

```terminaloutput
     ...
     f1-score 0.9969
```



## Command-line scripts

The command-line scripts are equipped with `--help` option which should be 
sufficient to guess their usage.

### Run the pure AB-3D-MOT tracker

```
batch-run-ab-3d-mot assets/detections/kitti/point-r-cnn-training/car/*.txt
```

Apart from the detections, the `pure-ab-3d-mot` tracker could be fed with KITTI annotations.

```
batch-run-ab-3d-mot-annotations assets/annotations/kitti/training/*.txt
```

By default, the car category is selected.

In both cases, consuming detections or annotations, the output is stored into text files.
The output of the tracker could be evaluated with ClearMOT metric.


### Evaluate the output of the pure AB-3D-MOT tracker using ClearMOT metric 

```
batch-eval-ab-3d-mot assets/annotations/kitti/training/*.txt
```

### Run the pure AB-3D-MOT tracker and evaluate the association quality using ClavIA

```
run-ab-3d-mot-with-clavia assets/annotations/kitti/training/*.txt
```

The script runs the tracker feeding it with (KITTI) annotations.
The result of the tracking is analysed with respect to the association accuracy.
The script allows to select the category of the objects to track (option 
`--category-obj` or `-c` for short).

Apart from the object category, it is possible to choose another category for
tracker *parameters*. Normally, the object category should be the same as
parameters category. By choosing a different parameter category, one could see
the effect of choosing different tracker parameters on the same detections.
The parameter category can be defined via the option `--category-prm` or `-p` for short.
If the option is absent, the parameter category will be the same as object category.

Note that some of the tracker parameters (`algorithm`, `metric`, `threshold` and `max-age`)
are possible to set via command-line options. These parameters affect the association.
