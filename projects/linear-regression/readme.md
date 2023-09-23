# Linear Regression from scratch
## Overview
Linear regression is a fundamental algorithm in data science and machine learning. It is utilized for predicting continuous variables (also called dependent variables or responses) using one or more predictor variables (also known as independent variables or factors).

The process of building a linear regression model involves the following steps:
1. **Data Collection**: in this step, we gather the data that we will use to train your model.
2. **Data Preprocessing**: in this step, we preprocess our data by (1) handling any missing values, and (2) normalizing or standardizing the data if the scales of our variables are different.
3. **Model Formulation**: in this step, we decide on the form of our model. For a simple linear regression, there is only one response and one factor, so our model is $\mathbf{Y} = \beta_0 + \beta_1\mathbf{X} + \epsilon$, where $\mathbf{Y}$ is a vector containing all observations of the response, $\mathbf{X}$ is a vector containing all observations of the factor, $\beta_0$ is the intercept, $\beta_1$ is the slope, and $\epsilon$ is the error term.
4. **Parameter Estimation**: in this stage, we estimate the parameters of our model (the intercept and slope in a simple linear regression) using several methods. A common method for estimating the parameters is the least square method.
5. **Model Evaluation**: in this stage, we evaluate how well our model fits our data using a combination of different approaches namely $R$-squared evaluation and residual analysis. 
6. **Prediction**: in this final stage, we use the model to make predictions on new data.
