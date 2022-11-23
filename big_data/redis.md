## Redis

### Redis面试问题

- 缓存问题：
  
    缓存穿透：key对应的数据在数据源并不存在，每次针对此key 的请求从缓存获取不到，请求都会到数据源，从而可能压垮数据源。

    缓存击穿：key对应的数据存在，但在redis中过期，此时若有大量并发请求过来，这些请求发现缓存过期一般都会从后端DB加载数据并回设到缓存，这个时候大并发的请求可能会瞬间把后端DB压垮。

    缓存雪崩：当缓存服务器重启或者大量缓存集中在某一个时间段失效， 这样在失效的时候，也会给后端系统(比如DB)带来很大压力。

- [redis stream和kafka对比](https://blog.csdn.net/qq_36285124/article/details/102617211)
  - 总结：
    - redis stream
      - 亚秒级延迟，快产快消的场景
      - 数据量不是很大，允许数据丢失
      - 不对过往数据保存
    - kafka
      - 可靠的、稳定的消息传递机制
      - 大量的数据传输
      - 无法容忍消息的丢失，数据保留可以进行追溯
- [Spark read redis hands-on](https://developer.aliyun.com/article/703467)
- [Redis原理介绍](https://www.51cto.com/article/667365.html)
- [redis核心知识及面试问题答案](https://ost.51cto.com/posts/11489)
