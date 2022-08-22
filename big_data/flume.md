## Flume


### Flume starter
- [Flume official website starter](https://flume.apache.org/releases/content/1.10.0/FlumeUserGuide.html)
- [flume介绍及原理](https://blog.csdn.net/A210810/article/details/107663808)
  - 日志、事件收集器，将各种数据源集中起来存储，作为一个中间件
  - 特性：高可用、分布式、高容错
  - 优势
    - 数据存储到持久化存储器中，hdfs, hbase
    - 提供上下文路由特征
    - 基于事务，保证数据传输的一致性
    - 可以水平拓展
    - 支持多路径、多源头、多输出、上下文路由等
- [flume和kafka区别](https://blog.csdn.net/justlpf/article/details/115351618)
  - 同样都是流式数据采集框架   
  - flume偏向于日志采集，负责数据采集和保障数据可靠传输，适用于多个生产者，数据安全性不高，适合生产和采集
  - kafka偏向于日志缓存，可持久化的消息队列，数据缓存，适用于多个消费者，数据安全性高，适合数据消费
  - 结合使用：flume作为日志采集，kafka日志消费
  - 流程：线上数据 -> flume -> kafka -> hdfs/spark stremaing/flink -> spark/Hive
  - 数据处理方案：
    - 日志采集：flume/logstash
    - 日志消费：storm, flink, spark streaming
    - 消息队列：kafka, rabbitMQ
    - 离线存储：hdfs, hbase, object storage
    - 离线分析：hive, presto, hadoop
    - 数据查询：ES，Solr