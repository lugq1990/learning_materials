## HBase


### HBase基础
- [Hbase入门,非常详细，包括模式的设计](https://www.cnblogs.com/guohu/p/13138868.html)
- [Hbase官网入门](https://hbase.apache.org/book.html#quickstart)
- [mac安装hbase](https://www.jianshu.com/p/510e1d599123)
- [hbase数据结构介绍](https://zhuanlan.zhihu.com/p/460659766)


### Hbase应用场景
- [hbase的基本应用场景](https://zhuanlan.zhihu.com/p/115487585?utm_source=qq)
    - 总结：
      - 数据动态可变，支持结构化和半结构化
      - 很多列为空，节省存储空间
      - 高吞吐量，瞬时写入量大
      - 多个数据版本维护问题，基于时间戳维护不同版本数据
      - 高可拓展性，动态拓展存储
      - 标签数据存储
    - 应用场景
      - 搜索引擎
      - 获取增量数据
      - 存储监控数据
      - 存储用户交互数据
      - 广告效果及点击流
      - 交易记录保存
      - 对象存储
      - 车联网数据
    - 缺点
      - 不支持复杂查询，只支持rowkey查询，没有join
    - 优点
      - 任意类型对象都可以使用byte类型存储，byte-in, byte-out
      - 支持PB级数据，压缩效率高，支持亿级别QPS每秒查询率
      - 添加节点和拓展比较容易

- [hbase八大应用场景](https://www.cnblogs.com/hbase-community/p/8629222.html)
![hbase应用场景](https://mmbiz.qpic.cn/mmbiz_png/Yicunacl1x3t9SgwRPCdpqJ4tPkGasvywygNDyhsg3p7CJG2lJ8Sk7GGCq4PWHNNibaZDiaKeGX1C5Q4kW946IicaA/640?wx_fmt=png)
