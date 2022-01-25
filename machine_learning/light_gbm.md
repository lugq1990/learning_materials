## LightGBM

LightGBM use leaf-wise algorithm to build trees that is much faster than depth-wise tree but will be overfit on training data.

### official information

- [Python basic step to set for lightbgm](https://lightgbm.readthedocs.io/en/latest/Python-Intro.html)
- [How to tune light-gbm model official recommendation](https://lightgbm.readthedocs.io/en/latest/Parameters-Tuning.html#)
- [Features for lightgbm](https://github.com/microsoft/LightGBM/blob/master/docs/Features.rst)
  
  summary:
  1. speed and memory optimization: use histogram-based to split features into bins speed up training and reduce memory use instead of others use pre-sort-based features.
  2. optimize for accuracy: use leaf-wise based tree growth could get better accuracy. ![level-based](https://github.com/microsoft/LightGBM/raw/master/docs/_static/images/level-wise.png) ![leaf-based](https://github.com/microsoft/LightGBM/raw/master/docs/_static/images/leaf-wise.png) 
  3. reduce/gather data to reduce network issue.
  4. For distributed learning: (1)improve feature parallel(instead of spliting data into different workers, but to stored full data in each worker to reduce network) (2)data parallel(use reduce function in each worker then syn update to global split feature) (3)voting parallel
   
