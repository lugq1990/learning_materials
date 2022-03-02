## Cloud Computing

### Cloud native

- [微软云cloud native](https://docs.microsoft.com/zh-cn/dotnet/architecture/cloud-native/definition)

12个应用程序（快速部署和缩放并应对变化）：
- 1-基本代码	每个微服务的一个基本代码，存储在其自己的存储库中。 通过版本控制进行跟踪，可以部署到多个环境 (QA、过渡、生产) 。
- 2-依赖项	每个微服务都隔离并打包其自己的依赖项，以在不影响整个系统的情况下进行更改。
- 3-配置	配置信息通过代码之外的配置管理工具移出微服务和外部化。 相同的部署可以在应用了正确配置的环境中进行传播。
- 4-支持服务	辅助资源 (数据存储、缓存、消息代理) 应通过可寻址 URL 公开。 这样做会使资源与应用程序分离，使其能够互相替换。
- 5-生成、发布、运行	每个版本都必须在生成、发布和运行阶段执行严格的分离。 每个都应使用唯一 ID 标记，并支持回滚功能。 新式 CI/CD 系统有助于满足此原则。
- 6-进程	每个微服务应在其自己的进程中执行，与其他正在运行的服务隔离。 外部化要求状态到后备服务，如分布式缓存或数据存储。
- 7-端口绑定	每个微服务都应自包含在其自己的端口上公开的接口和功能。 这样做会提供与其他微服务的隔离。
- 8-并发	如果容量需要增加，请在多个相同的进程中横向横向扩展服务 (复制) ，而不是在功能最强大的计算机上向上扩展单个大型实例。 开发应用程序，使其在云环境中以无缝横向扩展。
- 9-Disposability	服务实例应该是可释放的。 优先于快速启动，提高可伸缩性机会，并使系统保持正常状态。 Docker 容器以及 orchestrator 本身就满足了这一要求。
- 10-开发/生产奇偶校验	使环境在应用程序生命周期中保持尽可能相似，避免成本高昂的快捷方式。 在这里，使用容器可以通过提升相同的执行环境来做出极大的贡献。
- 11-日志记录	将微服务生成的日志视为事件流。 使用事件聚合器处理它们。 将日志数据传播到数据挖掘/日志管理工具（如 Azure Monitor 或 Splunk）并最终到长期存档。
- 12-管理进程	以一次性进程的形式运行管理/管理任务，例如数据清理或计算分析。 使用独立工具从生产环境中调用这些任务，而不是与应用程序分开。

- [Cloud computing concepts hub from AWS](https://aws.amazon.com/cn/what-is/?faq-hub-cards.sort-by=item.additionalFields.sortDate&faq-hub-cards.sort-order=desc&awsf.tech-category=*all)
   - [What is VPN](https://aws.amazon.com/cn/what-is/vpn/?nc1=h_ls)
     
    what is VPN used for: 
    1. Privacy: encryption data;
    2. Anonymity: without ip explod
    3. Security: shut-down for suspicious activity

- [对象存储的原理清晰说明](https://liuag.blog.csdn.net/article/details/17973039)