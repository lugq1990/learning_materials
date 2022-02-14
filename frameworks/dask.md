### Dask

#### Official website

Summary for Dask:
1. Use for parallel step for numpy, pandas
2. Could train parallel model based on sklearn, for XGBoost, lightgbm could be trained with distributed engine, for tensorflow, pytorch should use other module to wrapper it into a sklearn-alike module to be called by Dask. For parameters searching job could have better time-saving work.
3. Based on a distributed engine like K8s, yarn etc to schedule a distributed graph for distributed learning, it's a lazy work like Spark, have to be triggered by an action.

- Train a distributed model based on sklearn[https://ml.dask.org/joblib.html]
  