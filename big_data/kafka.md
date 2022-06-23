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