# Evaluation of a base of 3D multiple-object tracking (AB3DMOT) 

Evaluation part of the AB3DMOT by Xinshuo Weng (https://github.com/xinshuoweng/AB3DMOT)
The purpose of the package is to enable calculation of the detection+tracking quality
metrics for 3D tracking with KITTI data set.

## Installation

Should be as easy as `pip install eval-ab-3d-mot`, but if you downloaded the repo,
then `uv sync` standing in the root folder.

## Command-line scripts

### Download the detections (R-CNN)

Should be as easy as

```
eval-ab-3d-mot-download
```


### Batch run the pure AB-3D-MOT tracker 

```
batch-run-ab-3d-mot assets/detections/kitti/point-r-cnn-training/car/*.txt
```




