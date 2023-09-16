## Section 3.1

### Problem 3.1.9
The probability mass function of $X$ is given as:
$$
f(x) =
\begin{cases}
    a + b, \quad X = 0 \\
    c + d, \quad X = 1.5 \\
    e, \quad X = 2 \\
    f, \quad X = 3
\end{cases}
$$

a.
$$
$$

### Problem 3.1.11
The function $f(x) = \frac{2x+1}{25}$ is a probability mass function when it has the following properties:
* $f(X = x) \geq 0 \quad \forall x \in S$ with $S$ is the sample space of the discrete random variable $X$. 
* $\sum_xf(X = x) = 1 \quad \forall x \in S$

Verifying the first condition:
$$
\begin{cases}
f(X = 0) = \frac{2\times0 + 1}{25} \geq 0 \\
f(X = 1) = \frac{2\times1 + 1}{25} \geq 0 \\
f(X = 2) = \frac{2\times2 + 1}{25} \geq 0 \\
f(X = 3) = \frac{2\times3 + 1}{25} \geq 0 \\
f(X = 4) = \frac{2\times4 + 1}{25} \geq 0 \\
\end{cases}
$$

Verifying the second condition:
$$
\begin{aligned}
\sum_xf(X = x) &= f(X = 0) + f(X = 1) + f(X = 2) + f(X = 3) + f(X = 4)    \\
& = \frac{2\times0 + 1}{25} + \frac{2\times1 + 1}{25} + \frac{2\times2 + 1}{25} + \frac{2\times3 + 1}{25} + \frac{2\times4 + 1}{25} \\
& = 1
\end{aligned} 
$$

Since these conditions are fulfilled, we can conclude that $f(x)$ is a probability mass function.

a.
$$
P(X = 4) = \frac{2\times4 + 1}{25} = \frac{9}{25}
$$

b. 
$$
P(X \leq 1) = P(X = 0) + P(X = 1) = \frac{2\times0 + 1}{25} + \frac{2\times1 + 1}{25} = 0.16
$$

c. 
$$
P(2 \leq X < 4) = P(X = 2) + P(X = 3) = \frac{2\times2 + 1}{25} + \frac{2\times3 + 1}{25} = 0.48
$$

d. 
$$
P(2 \leq X < 4) = P(X = 2) + P(X = 3) = \frac{2\times2 + 1}{25} + \frac{2\times3 + 1}{25} = 0.48
$$

### Problem 3.1.13
The function $f(x)$ is a probability mass function when it has the following properties:
* $f(X = x) \geq 0 \quad \forall x \in S$ with $S$ is the sample space of the discrete random variable $X$. 
* $\sum_xf(X = x) = 1 \quad \forall x \in S$

Verifying the first condition: clearly from the table, $f(X = x) \geq 0 \quad \forall x \in S$.

Verifying the second condition:
$$
\sum_xf(X = x) = 0.2 + 0.4 + 0.1 + 0.2 + 0.1 = 1
$$

Since these conditions are fulfilled, we can conclude that $f(x)$ is a probability mass function.

a.

$$
P(X \geq 2) = P(X = 2) + P(X = 2.2.5) = 0.2 + 0.1 = 0.3
$$

b.

$$
P(X < 1.65) = P(X = 1.25) + P(X = 1.5) = 0.2 + 0.4 = 0.6
$$

c.

$$
P(X = 1.5) = 0.4
$$

d.

$$
P(X < 1.3 \text{or} X > 2.1) = P(X = 1.25) + P(X > 2.25) = 0.2 + 0.1 = 0.3
$$

### Problem 3.1.15
The probability mass function that describes the number of wafers from a lot that passes the test is given as:
$$
f(X = x) = \binom{n}{x}p^x(1-p)^{n-x}
$$

### Problem 3.1.16
Let the random variable $X$ denote the yearly revenue of the product, whose outcomes are very successful - meaning 10 million, moderately successful - meaning 5 million, or unsuccessful - meaning 1 million. The probability mass function is given as:
$$
f(x) = 
\begin{cases}
0.3, \quad x = 10,000,000 \\
0.6, \quad x = 5,000,000 \\
0.1, \quad x = 1,000,000
\end{cases}
$$

### Problem 3.1.17
Denote $X$ as the number of components in the assembly that meet specifications. Thus, $X$ has the following outcomes $S = \{0, 1, 2, 3\} corresponding to (1) no component meets the specification, (2) only one component meets the specs, (3) only two meets the specs, and (4) all components meet the specs. Therefore, the probability mass function of $X$ is given as:
$$
f(x) 
\begin{aligned}
    &=\begin{cases}
    (1 - 0.95)(1-0.98)(1-0.99), X = 0 \\
    0.95(1-0.98)(1-0.99), \quad X = 1 \\
    (0.95)(0.98)(1-0.99), \quad X = 2 \\
    (0.95)(0.98)(0.99), \quad X = 3 \\ 
    \end{cases} \\
    &= \begin{cases} 
        0.00001, \quad X = 0 \\
        0.00019, \quad X = 1 \\
        0.00931, \quad X = 2 \\
        0.92169, \quad X = 3 \\
       \end{cases}
\end{aligned}
$$

## Section 3.2

### Problem 3.2.2
The cumulative distribution of $X$ is given as:
$$
F(X) = \sum_xf(X = x) = f(1) + f(2) + f(3)
$$
with $f(x)$ is the probability mass function.

### Problem 3.2.3
The cumulative distribution of $X$ is given as:
$$
F(X) = \sum_xf(X = x) = f(0) + f(1) + f(2) + f(3) + f(4)
$$

### Problem 3.2.7
The cumulative distribution of $X$ must satisfy the following conditions:
* $0 \leq F(X) \leq 1$.
* If $x\leq y$ then $F(X = x) \leq F(X = y)$.

In this scenario, the function $F(x)$ clearly has all conditions are satisfied as:
* $0 \leq F(X) \leq 1$.
* $F(x < 1) < F(1\leq x \leq 3)$.

Hence, $F(x)$ is a cumulative distribution function of $X$.

a.
$$
P(X \leq 3) = \sum_xf(X \leq 3) = 0 + 0.5 = 0.5
$$

b.
$$
P(X\leq 2) = \sum_xf(X \leq 3)
$$

c. 
$$
P(1\leq X \leq 2) = 
$$

d. 
$$
P(X>2) = 1 - P(X\leq2) = 1 - \sum_xf(X\leq2) = 1 -0.5 = 0.5 
$$

### Problem 3.2.8
The cumulative distribution of $X$ must satisfy the following conditions:
* $0 \leq F(X) \leq 1$.
* If $x\leq y$ then $F(X = x) \leq F(X = y)$.

In this case, clearly the function $F(X)$ has all conditions satisfied since:
* $0 \leq F(X) \leq 1$.
* $F(X<30) \leq F(X<50)$.

Hence $F(X)$ is a cumulative distribution of $X$.

a.
$$
P(X\leq 50) = \sum_{x_i<50}f(x_i) = 0.75
$$

b. 
$$
P(X\leq 40) = \sum_{x_i<40}f(x_i) = 0.75
$$

c.
$$
P(40\leq X\leq 60) = 
$$

d. 

## Section 2.5
### Problem 3.5.2
Recall that the probability mass function of a binomial random variable is given as:
$$
f(x) = \binom{n}{x}p^x(1-p)^{n-x}
$$
with $n=10$ and $p=0.1$.

a. 
$$
P(X ≤ 2) = \binom{10}{2}0.1^2(1-0.1)^{10-2} \approx 0.1937 
$$ 

b. 
$$
P(X > 8) = P(X = 9) + P(X = 10) = \binom{10}{9}0.1^9(1-0.1)^{10-9} + \binom{10}{10}0.1^{10}(1-0.1)^{10-10} \approx 0
$$

c. 
$$
P(X = 4) = \binom{10}{4}0.1^4(1-0.1)^{10-4} \approx 0.0112 
$$

d. 
$$
P(5 ≤ X ≤ 7) = P(X=6) = \binom{10}{6}0.1^6(1-0.1)^{10-6} \approx 0.000137781 
$$

### Problem 3.5.5
The cumulative distriuvtion function of this random variable is given as:
$$
F(X) = \sum_x \binom{n}{x}p^x(1-p)^{n-x}
$$
with $n = 3$ and $p = 1/4$.

### Problem 3.5.6
The probability that the product operates (when there is no defective circuit in the product) is computed as:
$$
P(X = 0) = \binom{n}{x}p^x(1-p)^{n-x} = \binom{40}{0}(0.01)^0(1-0.01)^{40-0} \approx 0.669
$$
with $X$ is the number of defective circuits in the product, and $p$ is the probability that a single circuit becomes defective.

### Problem 3.5.10

a. 

The probability that three individuals have conditions caused by outside factors is computed as:
$$
P(X = 3) = \binom{20}{3}(0.13)^3(0.87)^{20-3} \approx 0.2347
$$

b. 

The probability that three or more individuals have conditions caused by outside factors is computed as:
$$
\begin{aligned}
P(X\geq 3) &= 1 - P(X=0) - P(X=1) - P(X=2) \\
&= 1 - \binom{20}{0}(0.13)^0(0.87)^{20-0} - \binom{20}{1}(0.13)^1(0.87)^{20-1} - \binom{20}{2}(0.13)^2(0.87)^{20-2} \\
&\approx 0.4920
\end{aligned}
$$

c. 

The mean and standard deviation of the number of individuals with conditions caused by outside factors is given as:
$$
\begin{aligned}
E(X) &= np = 20\times0.13 = 2.6 \\
V(X) &= np(1-p) = 20\times0.13\times0.87 = 2.262
\end{aligned}
$$

### Problem 3.5.12
Let $X$ denote the number of parts in the sample of 20 that require rework. Since $X$ is a binomial random variable, we can agree that its probability mass function is given as:
$$
f(X) = \binom{20}{x}p^x(1-p)^{20-x}
$$
with $p$ is the probability that a part needs rework. In this scenario, 1% of the parts typically require rework means that $E(X) = np = 0.2$. Therefore, $p = 0.2/20 = 0.01$ and $V(X) = np(1-p) = (20)(0.01)(0.99) = 0.198$.

a. 

The value that equals to 3 standard deviations of the mean is $x = 0.2 + 3\times\sqrt{0.198} \approx 1.5349$. Thus, the probability that X exceeds its mean by more than 3 standard deviations can be computed as:
$$
P(X > 1.5349) \equiv P(X>2) = \binom{20}{2}0.01^2(1-0.01)^{20-2} \approx 0.0159 
$$
since $X$ is always an integer, i.e., $X\in \mathbb{N}$.

b. 

If the rework percentage increases to 4%, the new value for $p$ will be: $p = 0.8/20 = 0.04$. Therefore, the probability that $X$ exceeds 1 is given as:
$$
\begin{aligned}
P(X>1) = 1 - P(X = 0) - P(X = 1) = 1 - \binom{20}{0}0.04^0(1-0.04)^{20} - \binom{20}{1}0.04^1(1-0.04)^{20-1}\approx 0.3536
\end{aligned} 
$$

c. 

If the rework percentage increases to 4%, the probability that $X$ exceeds 1 in at least one of the next five hours of samples is given as
$$
P(X>1|r\geq1) = 1 - P(X\leq1|r=0) = 1 - P(X\leq1)^5 = 1 -\Big(\binom{20}{0}0.04^0(1-0.04)^{20}\Big)^5 \approx 0.9831   
$$
with $r$ is the number of hour-samples.


### Problem 3.5.13
a.

The probability that every passenger who shows up can take the flight is computed as:
$$
P(X = 120) = \binom{120}{120}(1 - 0.1)^{120}(0.1)^0 \approx 0.000003 
$$

b. 
The probability that the flight departs with empty seats is computed as:
$$
P(X = 0) = \binom{120}{0}(1 - 0.1)^{0}(0.1)^{120} \approx 0.0
$$


## Section 3.8
### Problem 3.8.1
Recall that the probability mass function of a random variable that follows a Poisson distribution is given as:
$$
f_X(x) = \frac{e^{-\lambda T}(\lambda T)^x}{x!}
$$
with $E_X(x) = \lambda T$.

In the scenario that $E_X(x) = \lambda T = 4$

a.

$$
P(X = 0) = \frac{e^{-4}(4)^0}{0!} \approx 0.0183 
$$

b. 
$$
P(X \leq 2) = P(X = 0) + P(X = 1) + P(X = 2)= \frac{e^{-4}(4)^0}{0!} + \frac{e^{-4}(4)^1}{1!} + \frac{e^{-4}(4)^2}{2!} \approx 0.2381 
$$

c.
$$
P(X = 4) = \frac{e^{-4}(4)^4}{4!} \approx 0.1954
$$

d.
$$
P(X = 8) = \frac{e^{-4}(4)^8}{8!} \approx 0.0298
$$

### Problem 3.8.2
Recall that the probability mass function of a random variable that follows a Poisson distribution is given as:
$$
f_X(x) = \frac{e^{-\lambda T}(\lambda T)^x}{x!}
$$
with $E_X(x) = \lambda T$. In this case, $\lambda = 10$ since on average there 10 calls per hour.

a. 

The probability that there are exactly 5 calls in one hour is computed as:
$$
P(X = 5) = \frac{e^{-10}(10)^5}{5!} \approx 0.0378
$$
with $\lambda T = 10\times 1 = 10$

b.

The probability that there are 3 or fewer calls in one hour is computed as:
$$
\begin{aligned}
P(X \leq 3) &= P(X = 0) + P(X = 1) + P(X = 2) + P(X = 3) \\
&= \frac{e^{-10}(10)^0}{0!} + \frac{e^{-10}(10)^1}{1!} + \frac{e^{-10}(10)^2}{2!} + \frac{e^{-10}(10)^3}{3!} \\
&\approx 0.0103 \\
\end{aligned}
$$
with $\lambda T = 10\times 1 = 10$

c.

The probability that there are exactly 15 calls in two hours is computed as:
$$
P(X = 15) = \frac{e^{-20}(20)^15}{15!} \approx 0.0516
$$
with $\lambda T = 10\times 2 = 20$ since on average there are 20 calls per two hours.

d. 

The probability that there are exactly 5 calls in 30 minutes is computed as:
$$
P(X = 5) = \frac{e^{-5}(5)^5}{5!} \approx 0.1755
$$
with $\lambda T = 10\times 0.5 = 5$ since on average there are 5 calls per 30 minutes (0.5 hours).

### Problem 3.8.3
Recall that a Poisson random variable has the following probability mass distribution:
$$
f_X(x) = \frac{e^{-\lambda T}(\lambda T)^x}{x!}
$$
with $\lambda T$ is the product of the rate parameter $\lambda$ and the unit size $T$.

Given that $P(X=0)=0.05$, we can calculate $\lambda T$ as follows:
$$
P(X = 0) = \frac{e^{-\lambda T}(\lambda T)^0}{0!} = 0.05 \rightarrow \lambda T \approx 0.0513
$$

Therefore, the mean and variance of this random variable, which is  the number of customers who enter a
store in an hour, is given as: $E_(X) = 0.0513$ and $V(X) = 0.0513$.

### Problem 3.8.5
Recall that a Poisson random variable has the following probability mass distribution:
$$
f_X(x) = \frac{e^{-\lambda T}(\lambda T)^x}{x!}
$$
with $\lambda T$ is the product of the rate parameter $\lambda$ and the unit size $T$. In this scenario, the density is one star per 16 cubic light years. Hence, $\lambda T = 1$ since the density is the reciprocal of the mean $E(X) = \lambda T$.

a.

The probability of two or more stars in 16 cubic
light-years is computed as:
$$
P(X \geq 2) = 1 - P(X=0) - P(X=1) = 1 - \frac{e^{-1}(1)^0}{0!} - \frac{e^{-1}(1)^1}{1!} = 0.2642
$$

b.
From the probability of one or more stars exceeds 0.95, we can calculate the new mean as follows:
$$
P(X\geq1) = 1 - P(X = 0) = 1 - \frac{e^{-\lambda T}(\lambda T)^0}{0!} = 0.95 \rightarrow \lambda T \approx 2.9957 \approx 3
$$
Therefore, the equivalent number of cubic light years is $16\times3 = 48$.

### Problem 3.8.9
Recall that a Poisson random variable has the following probability mass distribution:
$$
f_X(x) = \frac{e^{-\lambda T}(\lambda T)^x}{x!}
$$
with $E(X) = \lambda T$ is the mean of the Poisson random variable. In this scenario, the mean is 0.05 flaw per square foot, and the area under interest is 10 square feet. Therefore, the mean covering the entire area is $0.05\times10 = 0.5$.

a.

The probability that there are no surface flaws in an auto’s interior is computed as:
$$
P(X = 0) = \frac{e^{-0.5}(0.5)^0}{0!} \approx 0.6065 
$$
b. 

If 10 cars are sold to a rental company, The probability that none of the 10 cars has any surface flaws is computed as:
$$
P(Y = 0) = \binom{10}{0}p^{10}(1 - p)^{0} = p^{10} = 0.6065 ^{10} \approx 0.00673
$$
given that $p$ is the probability that there are no surface flaws in an auto’s interior, and the number of flaws in each car is independent.

c. 

If 10 cars are sold to a rental company, the probability that at most 1 car has any surface flaws is computed as:
$$
P(Y \leq 1) \begin{aligned}
&= \binom{10}{0}p^{10}(1 - p)^{0} = p^{10}  + \binom{10}{1}p^{10}(1 - p)^{1} \\
&= \binom{10}{0}(0.6065)^{10}(1 - 0.6065)^{0} + \binom{10}{1}(0.6065)^{9}(1 - 0.6065)^{1} \\
&\approx 0.0504 
\end{aligned}
$$

### Problem 3.8.10
Recall that a Poisson random variable has the following probability mass distribution:
$$
f_X(x) = \frac{e^{-\lambda T}(\lambda T)^x}{x!}
$$
with $E(X) = \lambda T$ is the mean of the Poisson random variable. In this scenario, the mean is given as 2.5 per cubic millimeter; hence, $\lambda T = 2.5$.

a.

The probability of at least one inclusion in a cubic millimeter is computed as:
$$
P(X\geq1) = 1 - P(X=0)= 1-\frac{e^{-2.5}(2.5)^0}{0!} \approx 0.9197
$$

b. 

The probability of at least five inclusions in 5.0 cubic millimeters is computed as
$$
\begin{aligned}
P(X\geq5) &= 1- P(X=0)-P(X=1)-P(X=2)-P(X=3)-P(X=4) \\
&= 1 - \frac{e^{-12.5}(12.5)^0}{0!} - \frac{e^{-12.5}(12.5)^1}{1!} - \frac{e^{-12.5}(12.5)^2}{2!} - \frac{e^{-12.5}(12.5)^3}{3!} - \frac{e^{-12.5}(12.5)^4}{4!} \\
&\approx 0.9447
\end{aligned}
$$
with $E_{5}(X) = \lambda_{5}T_{5} = 2.5\times5 = 12.5$ is the mean number of inclusions per 5 cubic millimeters.

c. 

To find the volume of material to inspect such that the probability of
at least one inclusion is 0.99, we need to find the new mean.
$$
P(X\geq1) = 1 - \frac{e^{-\lambda T}(\lambda T)^0}{0!} = 0.99 \rightarrow \lambda T \approx 4.60517
$$

Therefore, such volume is $4.60517/2.5\approx1.8421$.

d. 

We can find the new mean from the given probability as follows:
$$
= 1 - \frac{e^{-\lambda T}(\lambda T)^0}{0!} = 0.95 \rightarrow \lambda T \approx 2.99573
$$
Therefore, $E'(X) = 2.99573 \approx 3$.
