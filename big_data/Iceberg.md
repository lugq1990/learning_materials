## IceBerg


### base information
- [IceBerg原理分析，对比分析HIVE的问题,推荐](https://zhuanlan.zhihu.com/p/488467438)

    总结（通过对元数据文件添加索引来提高查询效率）：
    - IceBerg主要解决HIVE对小文件list对NameNode压力过大的问题，通过自建的metadata来保证元数据的存储
    - 通过3类文件：数据文件(parquet文件)，元数据文件(avro和json文件)，catalog文件
    - 提供快照：可以查询过往数据
    - 提供增量读取功能：可以结合flink构建实时数仓
    - schema变更：不需要重新刷全量数据，如果变更可以实现老数据不变，新数据按照不同的查询逻辑实现
    - 支持数据更新和ACID事务

    ![iceberg整体架构图](https://pic3.zhimg.com/80/v2-e70b0482af68a0bf4e8f85e1706c3f8e_1440w.jpg)