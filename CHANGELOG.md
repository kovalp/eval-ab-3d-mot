# 0.1.0

  - Creation.
  - Split the module `evaluation.py` into smaller modules.
  - Unit test the function `box_overlap` (originally `boxoverlap`).
  - Unit test the class `Stat` (originally `stat`).
  - Unit test the class `TrackData` (originally `tData`).
  - Capitalize the constant `num_sample_points` --> `NUM_SAMPLE_POINTS = 41.0`.
  - Remove the `dump` (text file stream) from the class `Stat`.
  - Rename `Stat.print_summary` to `Stat.get_summary`.
  - Remove plot functions from `Stat`.
  - Add the magic `TrackData.__repr__`.
  - Merge `loadGroundTruth` and `loadTracking` into `load_data`.
  - Abstain from loading data from text file (`scripts/KITTI/evaluate_tracking.seqmap.val`).
  - Make `TrackingEvaluation.getThresholds` a standalone function (`thresholds.get_thresholds`).
  - Simplify arguments of the `TrackingEvaluation.load_data`.
  - Test `TrackingEvaluation.reset()`.
  - Start testing `TrackingEvaluation.compute_3d_party_metrics`.
  - Tested all, many by defining smaller functions.
