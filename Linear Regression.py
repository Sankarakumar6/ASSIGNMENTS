#!/usr/bin/env python
# coding: utf-8

# # Understanding The Assumption Of Linear Regression Algorithm

# Define Linear Regression?
#       
#       In machine learning,Linear Regression algorthim is used to predict best fit line,to know the relationship between 
#        depentent variable(target) and indepentent variable(prediction).

# # Assumptions of linear regression

# For successful regression analysis, it’s essential to validate the following assumptions :
# 1. Linearity of residuals
# 2.Normal distribution of residuals
# 3.No Autocorrelation
# 4.Homoscedasticity
# 5.Multicollinearity

# # 1.Linearity of residuals

# *Residual is the differnce between actaul value and predcited value
# 
# *There should be a linear relation between actual and predicted value 
# 
# *Use scatter plot to know about it 
# 
# *sample scatter plot images

# <img src="linear.JPg" width="800" height="400">
# 

# # 2.Normal distribution of residuals

# 
# *The residual/error mean should follow a normal distribution with a mean equal to zero or close to zero 
# 
# *This is done to check the selected line is acutally the best fit line or not
# 
# *If in case, the values are not in normally distributed,then it must be studied closely to make a better model 
# 
# 
# 

# <img src="li.jpg" width="800" height="400">
# 

# # 3.No Autocorrelation

# *The residual/ error should not be depentent on one another varibale like (time-series data)
# 
# *There should be no correlation between the residual / error terms

# # 4.Homoscedasticity

# *'Homo' meanns same, 'scedasticity' means scatter
# 
# *The redisual / error must have constant varience,this phenomenon is known as homoscedasticity
# 
# *for an example :if there are 325 rows,there should atleast a single varience constant,the fact is when plotting between an indiviual value against predicted value,varience obtained should be constant.
# 
# *So this is called Homoscedasticity

# <img src="li2.png" width="600" height="200">
# 

# # 5.Multicollinearity

# *This is another critical assumption in Linear Regression that is Multicollinearity
# 
# *In a some manner indepedent varibale is correlated with each other,it affect the predictions,and 
# hence it is necessary to detect multicollineartiy 
# 
# *It can be treated by using VIF- Variance Inflation Factor
# 
# *If VIF < 20 then it is considered as good value 
# 
# *If it exceeds (VIF > 20),then we need to treat it

# In[ ]:




