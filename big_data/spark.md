### Spark


#### How to tune spark job

- [How to tune spark job in real world by cloudera](https://blog.cloudera.com/how-to-tune-your-apache-spark-jobs-part-2/)
- [How to tune sparksql for spark3.0](https://blog.cloudera.com/how-does-apache-spark-3-0-increase-the-performance-of-your-sql-workloads/)

- [When try to read spark source code, we could use 2010 version of spark, I have readed some of them, it's clear!](https://github.com/apache/spark/tree/5b021ce0990ec675afc6939cc2c06f041c973d17/core/src/main/scala/spark)


#### How to use Spark
- [How to read data with JDBC connection](https://www.cnblogs.com/wwxbi/p/6978774.html)
- [How to reduce extract data time](https://www.jianshu.com/p/83d273dfea1c)
  
  summary:
  1. default is no parallel;
  2. Try to use one int column with partitionCol and lower and upper bound
  3. with user defined function to extract data like by date range.

### Spark source insight
- [系统的学习Spark,非常具体细节，推荐细读](https://spark-internals.books.yourtion.com/markdown/1-Overview.html)