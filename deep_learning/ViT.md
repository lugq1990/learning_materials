## ViT vision transformer


### ViT的说明
- [书中的一部分说明ViT,带有代码实现](https://paddlepedia.readthedocs.io/en/latest/tutorials/computer_vision/classification/ViT.html)
  
  核心：
  - 基于attention来对图像进行感知
  - 将图像利用分割，针对每一个分割的图片铺平，然后进行一个线性变化得到一个类似于词的embedding向量
  - 同时需要添加每一个分割的图片的位置信息，类似于文字的position embedding
  - 将位置信息和线性变换的向量整合成一个向量，不同的patch整合到一起类似于文字的向量，N*T(N为单词的个数，T为单词的embeddind)
  - 然后对全部的信息进行一个attetion，剩下的和transformer类似
  - 最终输出一个类别信息，来计算loss，更新模型参数
