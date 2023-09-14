## Section 3.1

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