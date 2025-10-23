# Evaluation of a base of 3D multiple-object tracking (AB3DMOT) 

Evaluation part of the AB3DMOT by Xinshuo Weng (https://github.com/xinshuoweng/AB3DMOT)
The purpose of the package is to enable calculation of the detection+tracking quality
metrics for 3D tracking with KITTI data set.

## Installation

Should be as easy as `pip install eval-ab-3d-mot`, but if you downloaded the repo,
then `uv sync` standing in the root folder.

## Download the detections & annotations

Should be as easy as

```
git clone https://github.com/kovalp/eval-ab-3d-mot.git
```

The detections (R-CNN) and annotations (training subset of KITTI)
are now in the folder `eval-ab-3d-mot/assets`.

## Command-line scripts

The command-line scripts are equipped with `--help` option which should be 
sufficient to learn their usage.

### Batch run the pure AB-3D-MOT tracker 

```
batch-run-ab-3d-mot assets/detections/kitti/point-r-cnn-training/car/*.txt
```

### Batch evaluation of the pure AB-3D-MOT tracker 

```
batch-eval-ab-3d-mot assets/annotations/kitti/training/*.txt
```
