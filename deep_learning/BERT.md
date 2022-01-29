### BERT

 - [Bert 改进： 如何融入知识](https://zhuanlan.zhihu.com/p/69941989)
 - [放弃幻想，全面拥抱Transformer：自然语言处理三大特征抽取器（CNN/RNN/TF）比较](https://zhuanlan.zhihu.com/p/54743941)
 - [如何理解BERT,知乎](https://www.zhihu.com/question/298203515)
 - 写的比较深入[谷歌BERT模型深度解析](https://blog.csdn.net/qq_39521554/article/details/83062188) 
 - [清晰简明的解释了BERT](https://www.cnblogs.com/huangyc/p/9813907.html)
 - [Pytorch code implement of Bert](https://github.com/codertimo/BERT-pytorch)
  
  Based on code implement like bellow summary[from bottom to up]:
  1. Load text from disk into sentences.
  2. Split sentences into words and convert words into index, also define mask and missing words index, plus start and end position encoding.
  3. Build emebedding for `word`, `position`, `segment` module.
  4. Build berdembedding module combine `word`, `position`, `segment` output, also add dropout.
  5. Build attention module based on `query`, `key`, `value` tensor.
  6. Build multi-head attention based on attention module convert `word`, `position`, `segment` into vector.
  7. Build BERT module that 12 layers of `transformer` and convert embedding to forward it with multiple layers of `transformers`. ![transformer architecture](https://lilianweng.github.io/lil-log/assets/images/transformer.png)
  8. Build real training module that contain 2 tasks: `next sentence prediction`, `mask word prediction`, just make each one into module, input data is output of `BERT` module, output is 2 parts that could be computed loss
  9.  real training step: load data -> build model -> loss sum -> backward -> optimizer -> loop.

 - [Load official trained model and make prediction based on keras](https://github.com/CyberZHG/keras-bert#Load-Official-Pre-trained-Models)


### Transfomer

- [Comprehensive expain for transformer and attention, also with other works related in chinese](https://lilianweng.github.io/lil-log/2018/06/24/attention-attention.html)
- [Tensorflow official tutorial for transformers](https://github.com/tensorflow/nmt)
- [Harvard NLP team step by step implement transformers based on pytorch, really comprehensive and detail code](http://nlp.seas.harvard.edu/2018/04/03/attention.html)
- [**Best tutorial for transformers step by step! recommend!](https://jalammar.github.io/illustrated-transformer/)
- 