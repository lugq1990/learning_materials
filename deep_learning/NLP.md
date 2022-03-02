## NLP materials

### NLP summary

- [Github summary for NLP materials, great](https://github.com/DA-southampton/NLP_ability)
- 

### NLP in action

- [Transformers to use pretrained models with python](https://huggingface.co/docs/transformers/index)

    transformers provide pretrained models for text, vision and audio. We could use already trained models and fine-tuning it.

### Mixed Word representation

- 针对不同的词向量表达做了一个整理：[深入浅出词向量表达](https://mp.weixin.qq.com/s/UE7ClHu7kiY_HXoJrZ0CwA)
  
  从LSTM到transformer：
 
  LSTM缺点：1. 梯度消失和梯度爆炸问题，模型不能保存长期的依赖问题； 2. 序列模型不能并行。

  Transformer的两个部分：encoder和decoder；encoder由多个encoder block组成：self-attention -> layer norm -> skip-conneciton -> forward network -> position encoding。 
  ![transformer 架构](https://mmbiz.qpic.cn/mmbiz_png/rB4jswrswuyr4LiawVUqgvEODNvojxd1T3R6tbVkFm0ChAwSxjtJvUtAtOGWM6t49w0tT79KrRXGCycUlGjtoIg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

  BERT:使用transformer架构作为encoder，训练过程中：将语料库的15%单词mask。15%分为3种：80%单词直接mask，10%单词替换成其他词，10%保持不变，称为MLM（Masked Language Model）。


### Word2vec

 - [word2vec（二）：面试！考点！都在这里](https://zhuanlan.zhihu.com/p/133025678)
  
核心是使用skip-gram和negative-sampling算法基于中心词预测周围词的概率，目标函数是：![skip-gram目标函数](https://pic4.zhimg.com/80/v2-1d9d0a01f5c0c1a8d68e5a5951cbdeef_1440w.jpg)

word2vec有两个算法：skip-gram和CBOW,其中skip-gram训练出来的效果更好一些，因为是使用中心去预测同一个窗口的其他词，如果窗口为k，则中心词就会被训练K词，但CBOW是使用其他词预测中心词，所以之后训练一次，但训练速度比较快，skip-gram有更好的表达效果。

负采样具体实施细节

就是创建两个线段，第一个线段切开词表大小的份数，每个份数的长度和频率正比。

第二个线段均分M个，然后随机取整数，整数落在第二个线段哪里，然后取第一个线段对应的词，如果碰到是自己，那么就跳过。

在代码实现中，第一个线段的长度不仅仅是频率，而是一个3/4的幂次方，第二个线段切分为10的8次方个段数。


### ELMo

- [ELMo paper](https://arxiv.org/pdf/1802.05365.pdf)

- [Deep contextualized word representation](https://www.cnblogs.com/jiangxinyang/p/10060887.html)

核心是先对语料库进行预训练，然后对特定的任务进行fine-tuning，对同义词在不同的环境下应该表示成不同的词向量作为目标，利用双向LSTM模型，最终的输出不是训练好的模型的中间的向量，而是利用线性加权的方式得到最终的词向量。

![模型结构](https://img2018.cnblogs.com/blog/1335117/201812/1335117-20181203205511185-937791986.png)

并可以对输出的向量进行缩放![输出向量的缩放](https://img2018.cnblogs.com/blog/1335117/201812/1335117-20181203205956715-1715160653.png)

- [tensorflow implement for EMLo](https://github.com/allenai/bilm-tf)

### Pointer network

用于生成文本摘要。

- [如何理解pointer network](https://zhuanlan.zhihu.com/p/48959800)


### 关键词匹配

- [如何实现中文分词,基于词典分词](https://github.com/DA-southampton/NLP_ability/blob/master/深度学习自然语言处理/关键词提取/中文分词/基于词典的正向最大匹配和逆向最大匹配中文分词.md)
  
  可以通过正向，反向匹配对中文句子进行分词。核心逻辑就是对一句话不断的去掉末尾的词，然后通过对剩下的结果是否在词典内进行判断，如果存在则可以将单词放到结果中，不然继续迭代。