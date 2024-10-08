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
- [spark数据倾斜解决方案](https://www.51cto.com/article/702345.html)
  - 过滤异常数据
  - 对倾斜数据识别，并两阶段分别合并，对有倾斜数据添加key保证并行度，然后再和没有倾斜数据Union
  - 提高shuffle并行度，提供更多资源来保证hash数据分到更多不同worker
  - 自定义hash函数
  - 将reduce端join改成map端join，其实就是通过广播变量的方式

### Spark source insight
- [系统的学习Spark,非常具体细节，推荐细读](https://spark-internals.books.yourtion.com/markdown/1-Overview.html)
- [highlevel explain spark workflow with architecture](https://www.analyticsvidhya.com/blog/2021/08/understand-the-internal-working-of-apache-spark/)
- [Databricks explain spark internals youtube](https://www.databricks.com/session/a-deeper-understanding-of-spark-internals)


### Spark Graphx
- [spark graphX原理讲解](https://blog.csdn.net/weixin_47134119/article/details/117756930)
- [Spark graphx内容整理、非常详细](https://developer.aliyun.com/article/371121)
- [Graphframe基于Dataframe实现的graphx，用起来确实方便](https://graphframes.github.io/graphframes/docs/_site/user-guide.html)