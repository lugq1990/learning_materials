### Kafka


#### kafka cluster
- [how to get kafka server status](https://stackoverflow.com/questions/37920923/how-to-check-whether-kafka-server-is-running)
  
  `echo dump | nc localhost 2181 | grep brokers`

- [how to get full number records in kafka with command]
  
  `./bin/kafka-run-class.sh kafka.tools.GetOffsetShell \
  --broker-list IT-Kafka-Node01:9092 \
  --topic ods-ebs-prod04 \
  --time -1 \
  --offsets 1 \
  | awk -F  ":" '{sum += $3} END {print sum}'`

- [对kafka的核心功能和工作原来进行了解释](https://blog.csdn.net/shutingwang/article/details/108869275)
- [消息中间件的解释](https://blog.csdn.net/m0_37583655/article/details/122575034)
- [Spark读取kafka数据的方式：receiver和direct的区别及代码实现](https://www.jianshu.com/p/9e3d41e27009)
  - 默认可以使用receiver方式，通过WAL和checkpoint保证数据不丢失，kafka的分区个数和spark分区个数没有关系，offset数据通过zookeeper默认保存，数据都是存在spark内存中（如果oom，会造成数据丢失，所以需要checkpint和WAL），如果通过增加topic分区个数并不会提高效率，只是receiver效率高一些
  - direct是通过kafka low level API来手动保存offset数据，kafka和spark分区个数一一对应，通过kafka父辈数据进行恢复