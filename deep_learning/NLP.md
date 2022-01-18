## NLP materials

### Bert

 - [Bert 改进： 如何融入知识](https://zhuanlan.zhihu.com/p/69941989)
 - [放弃幻想，全面拥抱Transformer：自然语言处理三大特征抽取器（CNN/RNN/TF）比较](https://zhuanlan.zhihu.com/p/54743941)


### Word2vec

 - [word2vec（二）：面试！考点！都在这里](https://zhuanlan.zhihu.com/p/133025678)
  
核心是使用skip-gram和negative-sampling算法基于中心词预测周围词的概率，目标函数是：![skip-gram目标函数](https://pic4.zhimg.com/80/v2-1d9d0a01f5c0c1a8d68e5a5951cbdeef_1440w.jpg)


### ELMo


- [Deep contextualized word representation](https://www.cnblogs.com/jiangxinyang/p/10060887.html)

核心是先对语料库进行预训练，然后对特定的任务进行fine-tuning，对同义词在不同的环境下应该表示成不同的词向量作为目标，利用双向LSTM模型，最终的输出不是训练好的模型的中间的向量，而是利用线性加权的方式得到最终的词向量。

![模型结构](https://img2018.cnblogs.com/blog/1335117/201812/1335117-20181203205511185-937791986.png)

并可以对输出的向量进行缩放![输出向量的缩放](https://img2018.cnblogs.com/blog/1335117/201812/1335117-20181203205956715-1715160653.png)

- [tensorflow implement for EMLo](https://github.com/allenai/bilm-tf)