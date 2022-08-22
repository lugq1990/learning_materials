## Solr


### Solr and ES
- [Solr和ES对比](https://blog.csdn.net/weixin_44641846/article/details/115584445)
  - Solr使用zookeeper分布式管理，ES自有
  - Solr支持更多的数据格式，es只支持json
  - Solr使用传统的搜索，es实时搜索效率更高
- [更加相似的solr和es对比](https://www.jianshu.com/p/b4fbc9598629)
  - 建立搜索，solr会出现io阻塞，es效率更高
  - 动态添加数据,solr效率降低，es不会
  - solr是一个web服务，需要使用web服务器
  - solr支持json, xml, csv, es只支持json
  - solr适合已有数据的查询，es适合添加数据的查询

