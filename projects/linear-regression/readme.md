# Linear Regression from scratch

## Table of Contents
1. [Overview](#Overview)
2. [Simple Linear Regression](#SLR)
3. [Multiple Linear Regression](#MLR)
4. [References](#Ref)

## Overview <a name = 'Overview'></a>
Linear regression is a fundamental algorithm in data science and machine learning. It is utilized for predicting continuous variables (also called dependent variables or responses) using one or more predictor variables (also known as independent variables or factors).

The process of building a linear regression model involves the following steps:
1. Hypothesize the form of the model.
2. Collect the sample data.
3. Use the sample data to estimate unknown parameters in the model.
4. Specify the probability distribution of the error term, and estimate any unknown parameters of this distribution. Also, check the validity of each assumption made about the probability distribution. 
5. Statistically check the usefulness of the model.
6. When satisfied that the model is useful, use it for prediction, estimation, and so on.

In the following sections, we will delve into three core topics of linear regression: simple linear regression (SLR), multiple linear regression (MLR), and logistic regression (LR).

## Simple Linear Regression (SLR) <a name = 'SLR'></a>
### Overview
Suppose we want to model the monthly sales revenue $\mathbf{y}$ as a function of the advertising expenditure $\mathbf{x}$. One problem arises is that it is unlikely that we can predict the monthly sales exactly given the advertising expenditure. Hence, we propose a probabilistic model for sales revenue as follows:

$$
\tag{1.1}
\mathbf{y} = f(\mathbf{x}) + \pmb{\epsilon}
$$

with $\pmb{\epsilon}$ represents all unexplained variations in sales due to various factors including accounted variables and/or random phenomena. 

From (1.1), we define the **simple linear regression** (MLR) probabilistic model that models the monthly sales as a function of the advertising expenditure as follows:

$$
\tag{1.2}
\mathbf{y} = \beta_o + \beta_1\mathbf{x} + \pmb{\epsilon}
$$

with:
* $\mathbf{y}= [y_1,y_2,...,y_n]^T$ is a column vector that represents the **dependent variable** (a.k.a. the **response** variable);
- $\mathbf{x} =[x_1,x_2,...,x_n]^T$ is a column vector that represents the independent variable (a.k.a. **factor**, or **predictor**);
- $\mathbf{\hat{y}} = \beta_o + \beta_1\mathbf{x}$ is a column vector that represents the **deterministic component**;
- $\pmb{\epsilon}$ is the **error component**;
- $\beta_0$ is the **intercept** of the regression line;
- $\beta_1$ is the  **slope** of the regression line. We can interpret it as the amount of increase or decrease in the mean of $\mathbf{y}$ for every unit increase in $\mathbf{x}$.

From (1.2), we define the estimated SLR model given the dataset as follows:

$$
\tag{1.3}
E(\mathbf{y}) \equiv \hat{\mathbf{y}} = \hat{\beta_0} + \hat{\beta_1}\mathbf{x}
$$

Noted that there is a difference between $\pmb{\hat{\beta}}$ - which is our estimated parameter, and $\pmb{{\beta}}$ - which is our true population parameter: $\pmb{\hat{\beta}}$ is the estimation of $\pmb{{\beta}}$ that we obtain from analysing the dataset, which is a subset of the population.

To estimate unknow parameters (namely $\beta_0$ and $\beta_1$) of the regression models, we use the least-square method:
* Formulation:

$$
\tag{1.4}
\begin{aligned}
\hat{\beta_1} &= \frac{SS_{xy}}{SS_{xx}} = \frac{\sum_{i=1}^nx_iy_i - (\sum_{i=1}^nx_i\sum_{i=1}^ny_i)/n}{\sum_{i=1}^nx_i^2 - (\sum_{i=1}^nx_i)^2/n}  \\
\hat{\beta_0} &= E(\mathbf{y}) - \hat{\beta_1}E(\mathbf{x}) = \frac{1}{n}\sum_{i=1}^ny_i - \hat{\beta_1}\frac{1}{n}\sum_{i=1}^nx_i\\
\end{aligned} 
$$

* Properties of the least-squares estimators: both the estimators $\hat{\beta_1}$ and $\hat{\beta_0}$ are **unbiased estimators** of the true population slope $\beta_1$ and the true population intercept $\beta_0$.

### Assumptions
When constructing the SLR model, we underline the following crucial assumptions:
* The relationship between the predictor ($\mathbf{x}$) and the response ($\mathbf{y}$) is linear. In other words, there is a **linear association** between $\mathbf{x}$ and $\mathbf{y}$.
* The errors, which is defined as the difference between the observed and the estimated values of the reponse $\epsilon_ i = y_i - \hat{y}_i$, are **independent and identically distributed**.
* The errors are **normally distributed** with a mean of zero and a quantified standard deviation. In other words, $\pmb{\epsilon} \sim \mathcal{N}(0,\sigma^2)$.
* The errors have **equal variances** (homoscedastic). In other words, the variability in the response does not increase as the value of the predictor increases. 
* The response is a random variable, while the predictor is a non-random variable.
* There is no presence of highly leverage and/or highly influential observations.

### Hypothesis test
In the context of SLR, we use hypothesis tests as a holistic approach to (1) verify the validity of each assumption we made above, and (2) statiscally check the utility of our model.

#### Linear association between predictor and response
To quantify the strength of the linear relationship $\mathbf{x}$ and $\mathbf{y}$ given the dataset, we use a measure called **Pearson correlation coefficient**. In SLR, the **Pearson correlation coefficient** between the response and the predictor is given as:

$$
\tag{1.5}
r = \frac{SS_{xy}}{\sqrt{SS_{xx}SS_{yy}}} = \frac{\sum_{i=1}^n(x_i - \bar{x})(y_i-\bar{y})}{\sqrt{\Big(\sum_{i=1}^n(x_i - \bar{x})^2\Big)\Big(\sum_{i=1}^n(y_i - \bar{y})^2\Big)}}
$$

* Properties of the Pearson correlation coefficient: the value of the measure $r$ is always between $-1$ and $+1$, regardless of the units of measurement used for the variables $\mathbf{x}$ and $\mathbf{y}$. In other words, it is scaleless.

We can test whether the true Pearson correlation coeffient of the probabilistic model,$\mathbf{y} = f(\mathbf{x}) + \pmb{\epsilon}$, is different from a hypothesized value, which we usually define to be zero, using the following steps:
* Hypotheses: $H_0: \rho = 0$ versus $H_a: \rho \neq 0$ at the significant level $\alpha = 0.05$.
* Test statisitic: the test statistic follows the Studentized t-distribution with $n-2$ degree of freedom, and it is given as:

$$
T_r = r\sqrt{\frac{n-2}{1-r^2}}
$$
* Rejection criteria: we will reject $H_0$ when $T_{r} >  t_{1-\alpha / 2,n-2}$ or $T_{r} < t_{\alpha / 2,n-2}$.

Additionally, we can quantify whether there is a significant linear association between $\mathbf{x}$ and $\mathbf{y}$ using the t-test. The t-test is a hypothesis test meaning we are testing whether a parameter 
* Hypotheses: $H_0: \beta_1 = 0$ versus $H_a: \beta_1 \neq 0$ at the significant level $\alpha = 0.05$.  We can interpret $H_0$ as follows: if $\beta_1$ is zero, $\mathbf{x}$ and $\mathbf{y}$ are completely unrelated.
* Test statisitic: the test statistic follows the Studentized t-distribution with $n-2$ degree of freedom, and it is given as:

$$
T_{\beta_1} = \frac{\hat{\beta_1} - \beta_{1,0}}{\text{se}(\hat{\beta_1})} = \frac{\hat{\beta_1} - \beta_{1,0}}{\sqrt{s^2/SS_{xx}}}
$$

with $\beta_{1,0}$ is the hypothesized value, which is zero.
* Rejection criteria: we will reject $H_0$ when $T_{\beta_1} >  t_{1-\alpha / 2,n-2}$ or $T_{\beta_1} < t_{\alpha / 2,n-2}$.
* Confidence interval of $\beta_1$: the confidence interval is basically a range of values where the true population value is likely fell into. Thus, the $100(1-\alpha)\%$ confidence interval of $\beta_1$ is given as:

$$
\text{CI}_{\alpha/2} = \hat{\beta_1} \pm |t_{\alpha/2,n-2}|\sqrt{s^2/SS_{xx}}
$$

#### Normality of residuals




### Example
Here is a demo of how to construct a SLR model on a toy dataset:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vohuynhquangnguyen/portfolio.codes-and-bytes/blob/main/projects/linear-regression/notebooks/simple_linear_regression.ipynb)

## Multiple linear regression (MLR) <a name = 'MLR'></a>
