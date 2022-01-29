## Imbalanced data

### How to solve imbalanced data problem

- [类别不平衡问题如果解决](https://github.com/DA-southampton/NLP_ability/blob/master/机器学习/真实场景如何解决类别不平衡的问题.md)
  
   根本解决：
    1. 是否是数据标注问题
    2. 添加标注样本
    3. 寻找新的特征：好的特征要好于在算法层面的更改
   表面解决：
    1. 欠采样：会改变数据分布，减少训练样本 -> 可以采样N次训练N个模型，上线之后可以进行投票
    2. 过采样：SMOTE算法，添加新样本 -> 测试数据最好不变
    3. 改善评估方法：利用ROC和AUC对不平衡问题不敏感
    4. 类别和样本权重更改：对少类别给与更大的权重，或对少类别预测出错添加惩罚

- 