### Model Interpreter


#### Books

- Really comprehensive book for machine learning to be interpretable: [Interpretable machine learning](https://christophm.github.io/interpretable-ml-book/)


#### Modules

- [Lime](https://github.com/marcotcr/lime)
  
  Lime support both classification, text, images etc.
  ![text explain](https://github.com/marcotcr/lime/raw/master/doc/images/twoclass.png)
  ![image explain](https://raw.githubusercontent.com/marcotcr/lime/master/doc/images/images.png)

- [SHAP](https://shap.readthedocs.io/en/latest/)
  
  If to explain colorful or for **single** user
  ![shap explain](https://shap.readthedocs.io/en/latest/_images/shap_header.png)

- [Eli5](https://eli5.readthedocs.io/en/latest/)
  
  Eli5 will try to explain models based on features: 
  ![eli5 weight sample](https://eli5.readthedocs.io/en/latest/_images/weights.png) 

  meantime, eli5 also support to explain text: 
  ![text explain](https://eli5.readthedocs.io/en/latest/_images/char-ngrams.png)


#### Logics

- How to explain SHAP: [deep learning model explain](https://towardsdatascience.com/interpreting-your-deep-learning-model-by-shap-e69be2b47893)
- SHAP value explain with an example [someone to explain shap](https://towardsdatascience.com/shap-explained-the-way-i-wish-someone-explained-it-to-me-ab81cc69ef30)
- book chapter to explain shap: [SHAP from interpretable machine learning](https://christophm.github.io/interpretable-ml-book/shap.html)
- Convert **shap value into probability** to explain black-box models[shap value for catboost models than logistic regression](https://towardsdatascience.com/black-box-models-are-actually-more-explainable-than-a-logistic-regression-f263c22795d), related code: [code implement convert shap into prob](https://github.com/smazzanti/tds_black_box_models_more_explainable/blob/master/Shap2Probas.ipynb)
- 