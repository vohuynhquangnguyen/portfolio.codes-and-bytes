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

In the following sections, we will delve into three core topics of linear regression: simple linear regression (SLR), multiple linear regression (MLR), and logistic regression (LR). Please note that the contents below are a summarized account of important points in linear regression. I strongly recommend you to consult the references for a rigorous treatment of the topics.

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
- $\mathbf{x} =[x_1,x_2,...,x_n]^T$ is a column vector that represents the **independent variable** (a.k.a. **factor**, or **predictor**);
- $\mathbf{\hat{y}} = \beta_o + \beta_1\mathbf{x}$ is a column vector that represents the **deterministic component**;
- $\pmb{\epsilon}$ is the **error component**;
- $\beta_0$ is the **intercept** of the regression line;
- $\beta_1$ is the  **slope** of the regression line. We can interpret it as the amount of increase or decrease in the mean of $\mathbf{y}$ for every unit increase in $\mathbf{x}$.

From (1.2), we define the estimated SLR model, a.k.a. the fitted model, given the dataset as follows:

$$
\tag{1.3}
E(\mathbf{y}) \equiv \hat{\mathbf{y}} = \hat{\beta_0} + \hat{\beta_1}\mathbf{x}
$$

Noted that there is a difference between $\pmb{\hat{\beta}}$ and $\pmb{{\beta}}$: $\pmb{\hat{\beta}}$ are estimated parameters, while $\pmb{{\beta}}$ are true and unknown population parameter. We obtain $\pmb{\hat{\beta}}$ by analysing the dataset, which is a subset of the population.

To estimate unknown parameters, namely $\beta_0$ and $\beta_1$, of the regression model, we use the **least-square method**:
* Formulation:

$$
\tag{1.4}
\begin{aligned}
\hat{\beta_1} &= \frac{SS_{xy}}{SS_{xx}} \\
&= \Bigg[\sum_{i=1}^nx_iy_i - (\sum_{i=1}^nx_i\sum_{i=1}^ny_i)/n\Bigg]\div \Bigg[\sum_{i=1}^nx_i^2 - (\sum_{i=1}^nx_i)^2/n\Bigg] \\
\end{aligned}
$$

$$
\tag{1.5}
\hat{\beta_0} = E(\mathbf{y}) - \hat{\beta_1}E(\mathbf{x}) = \frac{1}{n}\sum_{i=1}^ny_i - \hat{\beta_1}\frac{1}{n}\sum_{i=1}^nx_i
$$

* Properties of the least-squares estimators: both the estimators $\hat{\beta_1}$ and $\hat{\beta_0}$ are **unbiased estimators** of the true population slope $\beta_1$ and the true population intercept $\beta_0$.

Having estimated the slope $\beta_1$ and the intercept $\beta_0$, we need to estimate the variance of the error terms $\sigma^2_{\epsilon}$, which is done as follows:

$$
\tag{1.6}
\begin{aligned}
s_{\pmb{\epsilon}}^2 &= \frac{SS_E}{\text{DOF}} = \frac{SS_E}{n-2} \\
&= \Bigg[\sum_{i=1}^n y_i^2 - n\bar{y}^2\Bigg]\div\Bigg[n-2\Bigg] \\
&= \Bigg[\sum_{i=1}^n y_i^2 - n(\frac{1}{n}\sum_{i=1}^n y_i)^2\Bigg]\div\Bigg[n-2\Bigg] 
\end{aligned}
$$

with $\bar{y}$ is the mean all responses in the dataset, and $\text{DOF}$ is the degree of freedom (d.o.f.). Since we use 2 d.o.f. to estimate the slope and the intercept of the regression line, only $n-2$ d.o.f. left for the error variance estimation. We refer to $s_{\pmb{\epsilon}}$ as the estimated standard error of the regression model. In statistical literature, we usually annotate the estimated standard error and the estimated variance of errors simply as $s$ and $s^2$, respectively.

### Assumptions
When constructing the SLR model, we underline the following crucial assumptions:
* The relationship between the predictor ($\mathbf{x}$) and the response ($\mathbf{y}$) is linear. In other words, there is a **linear association** between $\mathbf{x}$ and $\mathbf{y}$.
* The errors, which are defined as the difference between the observed and the estimated values of the response $\epsilon_ i = y_i - \hat{y}_i$, are **independent and identically distributed**.
* The errors are **normally distributed** with a mean of zero and a quantified standard deviation. In other words, $\pmb{\epsilon} \sim \mathcal{N}(0,\sigma^2)$.
* The errors have **equal variances** (homoscedastic). In other words, the variability in the response does not increase as the value of the predictor increases. 
* The response is a random variable, while the predictor is a non-random variable.
* There is **no presence of highly leveraged and/or highly influential observations**. In other words, there is no presence of outliers.
* The constructed model has a high utility. In other words, there is no definitive presence of **lack of fit** in our model.

### Hypothesis test
In the context of SLR, we use hypothesis tests as a holistic approach to (1) verify the validity of each assumption we made above, and (2) statistically check the utility of our model.

#### Linear association between predictor and response
To quantify the strength of the linear relationship $\mathbf{x}$ and $\mathbf{y}$ given the dataset, we use a measure called **Pearson correlation coefficient**. In SLR, the **Pearson correlation coefficient** between the response and the predictor given the dataset is computed as:

$$
\tag{1.6}
\begin{aligned}
r &= \frac{SS_{xy}}{\sqrt{SS_{xx}SS_{yy}}} \\
&= \Bigg[\sum_{i=1}^n(x_i - \bar{x})(y_i-\bar{y})\Bigg] \div \Bigg[\sqrt{\big(\sum_{i=1}^n(x_i - \bar{x})^2\big) \big(\sum_{i=1}^n(y_i - \bar{y})^2\big)}\Bigg]
\end{aligned}
$$

* Properties of the Pearson correlation coefficient: the value of the measure $r$ is always between $-1$ and $+1$, regardless of the units of measurement used for the variables $\mathbf{x}$ and $\mathbf{y}$. In other words, it is scaleless.

We can test whether the true population Pearson correlation coefficient, $\rho$, of the probabilistic model, $\mathbf{y} = f(\mathbf{x}) + \pmb{\epsilon}$, is different from a hypothesized value, which we usually define to be zero, using the following hypothesis test:
* Hypotheses: $H_0: \rho = 0$ versus $H_a: \rho \neq 0$ at the significant level $\alpha = 0.05$.
* Test statistic: the test statistic follows the Studentized t-distribution with $n-2$ d.o.f., and it is given as:

$$
\tag{1.6}
T_r = r\sqrt{\frac{n-2}{1-r^2}}
$$

* Rejection criteria: we will reject $H_0$ when $T_{r} >  t_{1-\alpha / 2,n-2}$ or $T_{r} < t_{\alpha / 2,n-2}$, with $t_{\alpha / 2,n-2}$ is the lower critical value and $t_{1-\alpha / 2,n-2}$ is the upper critical value. Alternatively, we will reject $H_0$ if the corresponding p-value of the test statistic is lower than the value of the significant level. The p-value of $T_r$ is given as:

$$
\tag{1.7}
p(T_r) = 2\Big(1 - |\Phi(T_r)|\Big)
$$

with $\Phi(T_r)$ is the cumulative distribution function of the test statistic $T_r$.

Additionally, we can quantify whether there is a significant linear association between $\mathbf{x}$ and $\mathbf{y}$ using the t-test on the slope parameter. The t-test is a hypothesis test meaning we are testing whether a parameter is different from a hypothesized value given that the test statistic follows the Studentized t-distribution. The steps of the t-test on the slope parameter are as follows:
* Hypotheses: $H_0: \beta_1 = 0$ versus $H_a: \beta_1 \neq 0$ at the significant level $\alpha = 0.05$.  We can interpret $H_0$ as follows: if $\beta_1$ is zero, $\mathbf{x}$ and $\mathbf{y}$ are completely unrelated.
* Test statistic: the test statistic follows the Studentized t-distribution with $n-2$ degree of freedom, and it is given as:

$$
\tag{1.8}
T_{\beta_1} = \frac{\hat{\beta_1} - \beta_{1,0}}{\text{SE}(\hat{\beta_1})} = \frac{\hat{\beta_1} - \beta_{1,0}}{\sqrt{s^2/SS_{xx}}}
$$

with $\beta_{1,0}$ is the hypothesized value for $\beta_{1}$, which is zero. 

* Rejection criteria: we will reject $H_0$ for the t-test on $\beta_1$ when $T_{\beta_1} >  t_{1-\alpha / 2,n-2}$ or $T_{\beta_1} < t_{\alpha / 2,n-2}$. Alternatively, we will reject $H_0$ if the corresponding p-value of the test statistic is lower than the value of the significant level. The p-value of $T_{\beta_1}$ is given as:

$$
\tag{1.9}
p(T_{\beta_1}) = 2\Big(1 - |\Phi(T_{\beta_1})|\Big)
$$

with $\Phi(T_{\beta_1})$ is the cumulative distribution function of the test statistic $T_{\beta_1}$.

* Confidence interval for $\beta_1$: the confidence interval is an interval where the true value of a parameter most likely lies if we repeat the estimation many times with different samples drawn from the same population. Hence, the $100(1-\alpha)\%$ confidence interval of the slope paramter, $\beta_1$, is given as:

```math
\tag{1.10}
\text{CI}_{\beta_1} = \hat{\beta_1} \pm |t_{\alpha/2, n-2}|\sqrt{s^2 / S_{xx}}
```

Moreover, we can conduct a hypothesis test on the the intercept as follows:
* Hypotheses: $H_0: \beta_0 = 0$ versus $H_a: \beta_0 \neq 0$ at the significant level $\alpha = 0.05$.  We can interpret $H_0$ as follows: if $\beta_0$ is zero, the true regression line will pass through the origin.
* Test statistic: the test statistic, likewise, follows the Studentized t-distribution with $n-2$ degree of freedom, and it is given as:

$$
\tag{1.11}
T_{\beta_0} = \frac{\hat{\beta_0} - \beta_{0,0}}{\text{SE}(\hat{\beta_0})} = \frac{\hat{\beta_0} - \beta_{0,0}}{\sqrt{s^2(1/n + \bar{x}/SS_{xx})}}
$$

with $\bar{x}$ is the average of the predictor values, and $\beta_{0,0}$ is the hypothesized value for $\beta_0$, which is equal to zero.

* Rejection criteria: Similarly, we will reject $H_0$ for the t-test on $\beta_0$ when $T_{\beta_0} >  t_{1-\alpha / 2,n-2}$ or $T_{\beta_0} < t_{\alpha / 2,n-2}$. Alternatively, we will reject $H_0$ if the corresponding p-value is lower than the significant level. The p-value for $T_{\beta_0}$ is given as:

$$
\tag{1.12}
p(T_{\beta_0}) = 2\Big(1 - |\Phi(T_{\beta_0})|\Big)
$$

with $\Phi(T_{\beta_0})$ is the cumulative distribution function of the test statistic $T_{\beta_0}$.


* Confidence interval for $\beta_0$: the $100(1-\alpha)\%$ confidence interval of the intercept paramter, $\beta_0$, is given as:

```math
\tag{1.13}
\text{CI}_{\beta_0} = \hat{\beta_0} \pm |t_{\alpha/2, n-2}|
\sqrt{s^2\Big(\frac{1}{n}+\frac{\bar{x}^2}{S_{xx}}\Big)}
```


To sum up, in the context of SLR, the test on the correlation coefficient and the t-test on the slope parameter relate to the significance of regression. Failing to reject $H_0: \beta_1 = 0$ and $H_0: \rho = 0$ implies that there is no linear relationship between the predictor and the response. 

#### Normality of residuals
To validate whether our residuals are normally distributed, we can either construct a normal quantile-quantile plot and/or conduct a hypothesis test for normality such as the Shapiro-Wilk test (if the dataset we are using has less than 50 observations) or the Kolmogorov-Smirnovon test (if there are more than 50 observations in the dataset) on the standardized residuals. The standardized residuals are given as:

$$
\tag{1.14}
d_i = \frac{y_i - \hat{y}_i}{\sqrt{MSE}} = \frac{y_i - \hat{y}_i}{\sqrt{SS_E / (n-2)}} 
$$

with $MSE$ is the mean square error. If the standardized residuals fall approximately along a straight line, which represents the theoretical value from the hypothesized distribution $\mathcal{N}(0,\sigma^2)$, in the normality plot, we conclude that there is no severe departure from normality. We can also construct a histogram of standardized residuals to further assess whether the errors are normally distributed.

To sum up, in practice we usually combine both the visual approach (constructing the normality plot) and the hypothesis test approach to validate this assumption.

#### Homoscedasticity
To validate whether our residuals are homoscedastic, we have two primary approaches: a visual approach or a hypothesis test approach. In the visual approach, we will construct either a residual-versus-fitted plot or a residual-versus-predictor plot. We outline the following characteristics of a well-behaved residual-versus-fitted plot, which also applicable for the residual-versus-predictor plot:  
* The residuals "bounce randomly" around the $\epsilon_i = 0$ line. This suggests that the assumption that the relationship is linear is reasonable.
* The residuals roughly form a "horizontal band" around the $\epsilon_i = 0$ line. This suggests that the variances of the error terms are equal.
* No one residual "stands out" from the basic random pattern of residuals. This suggests that there are no outliers.

Moving to the second approach, we will conduct a hypothesis test on the error variances. One popular and intuitive hypothesis test is the Goldfeld-Quandt test. The procedure of the Goldfeld-Quandt test, explained in a simplified manner is as follows:
* We divide our dataset into two equal subsets $N_1$ and $N_2$.
* In each subset, we construct a SLR model. Hence, we have two models namely $\mathbf{y}_1 = \hat{\alpha}_0 + \hat{\alpha}_1\mathbf{x}_1$ and $\mathbf{y}_2 = \hat{\gamma}_0 + \hat{\gamma}_1\mathbf{x}_2$.
* We then quantify the respective estimated error variances namely $s_1^2$ and $s_2^2$ for the models.
* Finally, we conduct the test of equal variances for these estimators of error variance. 

The test of equal variances in the context of the Goldfeld-Quandt test consists of the following steps:
* Hypotheses: $H_0: s_1^2 = s_2^2$ versus $H_a: s_1^2 \neq s_2^2$ at the significant level $\alpha = 0.05$.
* Test statistic: the test statistic follows the F-distribution with $n_1 - 1$ numerator d.o.f. and $n_2 - 1$ denominator d.o.f. (in the case of the Goldfeld-Quandt test, $n_1 = n_2 = n/2$), and is given as:

$$
\tag{1.15}
F_0 = \frac{s_1^2}{s^2_2} = \frac{MSE_1}{MSE_2}
$$

* Rejection criteria: we will reject $H_0$ when $F_0 > f_{1-\alpha/2,n_1-1,n_2-1}$ or $F_0 < f_{\alpha/2,n_1-1,n_2-1}$, with $f_{\alpha/2,n_1-1,n_2-1}$ is the lower critical value and $f_{1 - \alpha/2,n_1-1,n_2-1}$ is the upper critical value. Alternatively, we can reject $H_0$ if the corresponding p-value of the test statistic is less than the significant level. The p-value for the test statistic $F_0$ is given as:

$$
\tag{1.16}
p(F_0) = 
\begin{cases}
1 - \Phi(F_0), \quad &\Phi(F_0) > 0.5 \\
\Phi(F_0), \quad &\Phi(F_0) < 0.5 \\
\end{cases}
$$

with $\Phi(F_0)$ is the cumulative distribution function of the test statistic $F_0$.

To sum up, similar to the normality of residuals assumption, in practice we will  combine both the visual approach (constructing the residuals-versus-fitted plot) and the hypothesis test approach to validate this assumption. 

#### Leveraged and influential data points
Ideally, the dataset that we used to construct our SLR model should not have any outliers, i.e., not having an extreme $x$ nd $y$ values. Nevertheless, if there are outliers presented in our dataset, we need to quantify their respective leverage and Cook's distance to determine whether these outliers are worth investigating.

* **Leverage of a data point** is a measure of its ability to pull the regression line towards itself. The leverage of a data point depends entirely on its $x$-value: if the $x$-value of a data point  is far removed from the center of all $x$-values, then that data point will have a high leverage. In the context of SLR, a leverage of the $i$-th observation is given as:

$$
\tag{1.17}
h_{ii} = \frac{1}{n} + \frac{(x_i -\bar{x})^2}{SS_{xx}}
$$

* The **Cook's distance** of a data point is a measure of how influential that data point is by quantifying its effect on the linear model if omitted from the analysis. As a result, Cook's distance is a function of both the leverage and the magnitude of the residual. The Cook's distance of the $i$-th observation is given as:

```math
\tag{1.18}
D_i = \frac{(y_i-\hat{y}_{(i)})^2}{2\times\text{MSE}} \Bigg[\frac{h_{ii}}{(1-h_{ii})^2}\Bigg]
```

An observation with the Cook's distance larger than three times the mean Cook's distance might be an outlier.  As a rule of thumb, if $D_i$  is greater than 0.5, then the $i$-th data point is worthy of further investigation as it may be influential. If $D_i$ is greater than 1, then the $i$-th data point is quite likely to be influential. If $D_i$ stands out from the other Cook's distance values in addition to being greater than 1, it is almost certainly influential.

To sum up, in practice we usually construct two scatter plots namely the standardized-residuals-versus-fitted plot and the Cook's-distance-versus-leverage plot to identify which data point is potentially an outlier with high influential. 

#### Utility of the model
In the context of linear regression, the utility of a model is the significance of regression. In other words, it represents how well our model describes the relationship between the response and the predictor. As mentioned above, to test the significance of regression in the context of SLR, we conduct the t-test on the slope parameter and/or the test on the correlaition coefficient. In addition to these two tests, a general approach is to conduct the analysis of variance (ANOVA). The ANOVA consists of the following steps:
* We first partition the total variability in the response variable $\mathbf{y}$ into two meaningful components:
  
$$
\tag{1.19}
SS_T = SS_R + SS_E 
$$

with $SS_T$ represents the total variability, a.k.a. the total sum of squares; $SS_R$ represents the regression variability, a.k.a. the regression sum of squares; $SS_E$ represents the error variability, a.k.a. error sum of squares. $SS_R$ and $SS_E$ are computed as follows:

$$
\tag{1.20}
SS_R = \sum_{i=1}^n(\hat{y_i} - \bar{y})^2
$$

$$
\tag{1.21}
SS_E = \sum_{i=1}^n(y_i - \hat{y_i})^2
$$

* We then compute the coefficient of determination $R^2$, which is interpreted as the proportion of variability in the response that is explained by our model: 

$$
\tag{1.22}
R^2 = \frac{SS_R}{SS_T} = 1 - \frac{SS_E}{SS_T}
$$

Once we have acquired the coefficient of determination $R^2$, we will conduct the test for model utility as follows:
* Hypotheses: $H_0: \beta_1 = 0 | \beta_0$ versus $H_0: \beta_1 \neq 0 | \beta_0$ at the significant level $\alpha = 0.05$. We can interpret $H_0$ as we are assuming that our model is as good as the intercept-only model.
* Test statistic: the test statistic follows the F-distribution with $1$ d.o.f. in the numerator and $n-2$ d.o.f. in the denominator, and it is given as:

$$
\tag{1.23}
F_0 = \frac{SS_R/1}{SS_E/(n - 2)}=\frac{R^2}{(1-R^2)/(n -2)}  
$$

* Rejection criteria: We will reject $H_0$ when $F_0 >  f_{1-\alpha / 2,1,n-2}$, with $f_{1-\alpha / 2,1,n-2}$ is the upper critical value. Alternatively, we can reject $H_0$ if the corresponding p-value of the test statistic is less than than the significant level. The p-value for $F_0$ is given as:

$$
\tag{1.24}
p(F_0) = 1 - \Phi(F_0)
$$

### Example
Here is a demo of how to construct a SLR model on a toy dataset using Python:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vohuynhquangnguyen/portfolio.codes-and-bytes/blob/main/projects/linear-regression/notebooks/simple_linear_regression.ipynb)

Here is a demo of how to construct a SLR model on a toy dataset using R:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]()

## Multiple linear regression (MLR) <a name = 'MLR'></a>
