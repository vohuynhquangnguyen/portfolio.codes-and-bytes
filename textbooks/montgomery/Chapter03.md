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
