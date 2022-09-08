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