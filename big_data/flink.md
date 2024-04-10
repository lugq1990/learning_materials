## Flink


### Flink base
- [Flink架构](https://flink.apache.org/zh/flink-architecture.html)
  
  架构总结：
  - 支持有界流和无界流
  - 可以通过各类资源管理器保证资源调用YARN，MESOS，K8S
  - 任意规模的数据：亿万事件，TB状态，数千内核
  - 利用内存计算

- [flink 运维](https://flink.apache.org/zh/flink-operations.html)
- [flink的核心架构，非常全面](https://blog.51cto.com/u_15294184/3052633)
- [flink核心内容,非常详细](https://blog.csdn.net/a805814077/article/details/108095451)
- [Flink流处理读书笔记，推荐！](https://cloud.tencent.com/developer/article/2136281)

### Flink CDC
- [Flink CDC应用场景](https://developer.aliyun.com/article/777502)
  - CDC两种模式
    - 基于查询：select全表扫描，发现变更数据
    - 基于日志：读取系统binlog日志
  - 基于日志的好处
    - 捕获全部的更新数据，异地容灾、数据备份
    - 基于DML操作，无需全表扫描，更高的效率和性能
    - 无需侵入业务、业务解耦
- [Flink CDC架构介绍](https://flink-learning.org.cn/article/detail/3ebe9f20774991c4d5eeb75a141d9e1e)


### Flink hands-on
- [pyflink hands-on with code](https://flink-learning.org.cn/article/detail/65bcdf72a377d468b5436c3e76a63437)


### Flink state storage
- [How to use rocksdb as state backend storage with code](https://towardsdatascience.com/heres-how-flink-stores-your-state-7b37fbb60e1a)
- [Use remote rocksdb as state storage is fine?](https://stackoverflow.com/questions/70900933/flink-state-using-rocksdb)
- [flink state backend storage official introduce](https://nightlies.apache.org/flink/flink-docs-master/docs/ops/state/state_backends/)


### Online books
- [尚学堂的flink的介绍](https://confucianzuoyuan.github.io/flink-tutorial/book/chapter01-00-00-第一章，有状态的流式处理简介.html)