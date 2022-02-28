## Micro Service

### 微服务

微服务的特性：
1. 每个在更大的域上下文内实现特定的业务功能。
2. 每个都是自主开发的，可以独立部署。
3. 每个都是独立的，它封装其自己的数据存储技术、依赖关系和编程平台。
4. 每个运行在其自己的进程中，并使用标准通信协议（例如 HTTP/HTTPS、gRPC、Websocket 或 AMQP）与其他用户通信。
5. 它们共同构成应用程序。

核心：每个模块可以**独立**开发、部署来实现特定功能且每个模块都有自己的**存储**和开发环境，并能够通过通信协议进行**通信**，整合到一起是一个应用程序。
![微服务的架构](https://docs.microsoft.com/zh-cn/dotnet/architecture/cloud-native/media/monolithic-vs-microservices.png)

微服务的优点：
1. 每个服务都有自治的生命周期可以独立开发和部署，降低整个系统崩溃的风险。
2. 每个微服务都可以独立缩放。

微服务的风险：
1. 通信：如何通信和是否可以直接通信？是否使用HTTP进行通信？
2. 复原能力：如果服务无响应或是不可用如何处理？
3. 分布式数据：如何查询不同的服务直接的数据并提供事务的支持？
4. 机密：如何保存机密和敏感的配置信息？

- [什么是微服务,包含对应的代码,简单易懂](https://www.jianshu.com/p/7293b148028f)
- [微服务的各个特性和缺点已经具体应用需要注意的地方,非常详细](https://blog.csdn.net/wuxiaobingandbob/article/details/78642020)
- [java 代码实现订单管理微服务](https://www.jianshu.com/p/efc97f64c21b/)
  
### 微服务的服务编排

- [微服务的编排方式,带有案例](https://blog.csdn.net/xiaoyw71/article/details/119331751)
- 如何实现对不同服务的逻辑定义和处理：编制(同步)，编排(消息驱动)，API网关(适配网关)：[微服务的服务编排](https://www.jianshu.com/p/54e2e223dbac)


### 微服务的监控

- [微服务的调用链监控](https://www.cnblogs.com/jsjwk/p/10937991.html)
  
  调用链解决的问题：多服务之间的关系，从一个请求到一个请求的结束的全链路跟踪，核心三个概念：Trace是一个请求的父节点，span是每个服务的节点，annotation是每一个span上的自定义数据。
  ![trace span annotation](https://img2018.cnblogs.com/blog/1453917/201905/1453917-20190528155959334-1827382171.png)

  链路监控系统的构成：数据埋点采集，数据存储分析，数据分析展示

  作用：
  1. 项目网络拓扑图
  2. 快速定位问题
  3. 优化系统

  开源的产品：
  1. CAT
  2. Open Zipkin
  3. Naver pinpoint
   

### Springboot framework

- [springboot源代码分析](https://github.com/fangjian0423/springboot-analysis)


### Springcloud framework

- [bilibili 尚学堂springcloud教程](https://www.bilibili.com/video/BV18E411x7eT?p=4)