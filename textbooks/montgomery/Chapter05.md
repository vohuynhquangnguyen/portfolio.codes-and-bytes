## Section 5.1
### Problem 5.1.1
Recall that $f_{X,Y}(x,y)$ is a joint probability distribution function of two random variables $X$ and $Y$ when it has the following properties:
* $f_{X,Y}\geq 0, \quad \forall x,y$
* $\sum_x\sum_y = 1, \quad \forall x,y$

According to the table, it is clear that these properties are satisfied. Hence, $f_{X,Y}(x,y)$ is a joint probability distribution function of $X$ and $Y$.

a. 
$$
P(X < 2.5, Y < 3) = f_{X,Y}(1.0, 1) + f_{X,Y}(1.5, 2) = 1/4 + 1/8 = 3/8
$$

b. 
$$
P(X < 2.5) = f_{X,Y}(1.0, 1) + f_{X,Y}(1.5, 2) + f_{X,Y}(1.5, 3) = 1/4 + 1/8 + 1/4 = 5/8
$$

c. 
$$
P(Y < 3) = f_{X,Y}(1.0, 1) + f_{X,Y}(1.5, 2) = 1/4 + 1/8 = 3/8
$$

d. 
$$
P(X > 1.8, Y > 4.7) = f_{X,Y}(2.5,4) + f_{X,Y}(3.0,5) = 1/4 + 1/8 = 3/8
$$

e. 
$$
\begin{aligned}
E(X) &= \sum_xxf_{X}(x,y) = (1.0)(1/4) + (1.5)(1/8 + 1/4) + (2.5)(1/4) + (3.0)(1/8) = 1.8125 \\
V(X) &= E(X^2) - [E(X)]^2 = (1.0)^2(1/4) + (1.5)^2(1/8 + 1/4) + (2.5)^2(1/4) + (3.0)^2(1/8) - 1.8125^2 \approx 0.4961 \\
E(Y) &= \sum_yyf_{Y}(x,y) = (1)(1/4) + (2)(1/8) + (3)(1/4) + (4)(1/4) + (5)(1/8) = 2.875 \\
V(Y) &= E(Y^2) - [E(Y)]^2 = (1)^2(1/4) + (2)^2(1/8) + (3)^2(1/4) + (4)^2(1/4) + (5)^2(1/8) - 2.875^2 \approx 1.8594 
\end{aligned}
$$

f.

The marginal probability distribution of $X$ is given as:
$$
\begin{cases}
f_X(X = 1) = 1/4 \\
f_X(X = 1.5) = 1/4 + 1/8 = 3/8 \\
f_X(X = 2.5) = 1/4 \\
f_X(X = 3.0) = 1/8 \\
\end{cases}
$$

### Problem 5.1.2
Recall that $f_{X,Y}(x,y)$ is a joint probability distribution function of two random variables $X$ and $Y$ when it has the following properties:
* $f_{X,Y}\geq 0, \quad \forall x,y$
* $\sum_x\sum_y = 1, \quad \forall x,y$

According to the table, it is clear that these properties are satisfied. Hence, $f_{X,Y}(x,y)$ is a joint probability distribution function of $X$ and $Y$.
a. 
$$
P(X < 0.5, Y < 1.5) = f_{X,Y}(-1.0,-2) + f_{X,Y}(-0.5,-1) = 1/8 + 1/4 = 3/8
$$ 

b. 
$$
P(X < 0.5) = f_{X,Y}(-1.0,-2) + f_{X,Y}(-0.5,-1) = 1/8 + 1/4 = 3/8
$$

c. 
$$
P(Y < 1.5) = f_{X,Y}(-1.0,-2) + f_{X,Y}(-0.5,-1) + f_{X,Y}(0.5, 1)= 1/8 + 1/4 + 1/2 = 7/8
$$

d. 
$$
P(X > 0.25, Y < 4.5) = f_{X,Y}(0.5,-1) + f_{X,Y}(1.0,2) = 1/2 + 1/8 = 5/8
$$

e. 
$$
\begin{aligned}
E(X) &= \sum_xxf_{X}(x,y) = (-1.0)(1/8) + (-0.5)(1/4) + (0.5)(1/2) + (1.0)(1/8) = 0.125 \\
V(X) &= E(X^2) - [E(X)]^2 = (-1.0)^2(1/8) + (-0.5)^2(1/4) + (0.5)^2(1/2) + (1.0)^2(1/8) - 0.125^2 \approx 0.3125 \\
E(Y) &= \sum_yyf_{Y}(x,y) = (-2)(1/8) + (-1)(1/4) + (1)(1/2) + (2)(1/8) = 0.25 \\
V(Y) &= E(Y^2) - [E(Y)]^2 = (1)^2(1/4) + (2)^2(1/8) + (3)^2(1/4) + (4)^2(1/4) + (5)^2(1/8) - 0.25^2 \approx 1.6875
\end{aligned}
$$

f.

The marginal probability distribution of $X$ is given as: 
$$
\begin{cases}
f_X(X = -1.0) = 1/8 \\
f_X(X = -0.5) = 1/4 \\
f_X(X = 0.5) = 1/2 \\
f_X(X = 1.0) = 1/8 \\
\end{cases}
$$

### Problem 5.1.3
Let $X$ and $Y$ denote the number of bits with high and moderate distortion out of the three, respectively.

a. 

In this scenario, $f_{X,Y}$ is the multinomial distribution having the following probability mass function:
$$
f_{X,Y}(x,y) = \frac{3!}{x!y!(3-x-y)!}p_X^{x}p_Y^y(1-p_X-p_Y)^{3-x-y}
$$
with $p_X = 0.01$ and $p_Y = 0.04$ 

b.

The marginal distribution of $X$ is given as:
$$
f_X(x,y) = \sum_y^{3-x}f_{X,Y}(x,y)
$$

c.

The expected value of $X$ is given as:
$$
E(X) = \sum_y^{3-x}xf_{X,Y}(x,y)
$$

### Problem 5.1.4
Let $X$ and $Y$ denote the number of pages in the sample with moderate and high graphics output, respectively.

a.

In this scenario, $f_{X,Y}$ is the multinomial distribution having the following probability mass function:
$$
f_{X,Y}(x,y) = \frac{100!}{x!y!(100-x-y)!}p_X^{x}p_Y^y(1-p_X-p_Y)^{3-x-y}
$$
with $p_X = 0.3$ and $p_Y = 0.1$ 

b.

The marginal distribution of $X$ is given as:
$$
f_X(x,y) = \sum_y^{100-x}f_{X,Y}(x,y)
$$

c.

The expected value of $X$ is given as:
$$
E(X) = \sum_y^{100-x}xf_{X,Y}(x,y)
$$

### Problem 5.1.7

### Problem 5.1.8
The function $f_{X,Y}(x,y)$ is a joint probability density function over the range $0<x<3$ and $x<y<x+2$ if it satisfies:
$$
\int_{0}^3\int_x^{x+2}c(x+y)dydx = 1
$$

Evaluating the double integral:
$$
\int_x^{x+2}c(x+y)dy = c\int_x^{x+2}(x+y)dy = cx + (1/2)c\Big[y^2\Big]_{x}^{x+2} = cx + (1/2)c\Big((x+2)^2-x^2\Big) = 0.5cx^2 + 4cx + 4c
$$
$$
\int_{0}^3(0.5cx^2 + 4cx + 4c)dx = \frac{1}{6}c\times3^3 + 2c\times3^2 + 4c\times3 - (\frac{1}{6}c\times0^3 + 2c\times0^2 + 4c\times0) = (69/2)c
$$
Now, we can find $c$:
$$
\int_{0}^3\int_x^{x+2}c(x+y)dydx = 1 \rightarrow (69/2)c =1  \rightarrow c = \frac{2}{69}
$$

a. 
$$
P(X < 1, Y < 2)
$$ 

b. 
$$
P(1 < X < 2)
$$ 

c. 
$$
P(Y > 1)
$$

d. 
$$
P(X < 2, Y < 2)
$$ 

e. 
$$
E(X) = \int_0^3\int_x^{x-2} xf_{X,Y}(x,y)dydx = \int_0^3\int_x^{x-2} x\frac{2}{69}(x+y)dydx
$$ 

f. 
$$
V(X)
$$

### Problem 5.1.9
a. P(X < 2, Y < 3) b. P(X < 2.5)
c. P(1 < Y < 2.5) d. P(X > 1.8, 1 < Y < 2.5)
e. E(X) f. P(X < 0, Y < 4)
g. Marginal probability distribution of X

### Problem 5.1.10
a. P(X < 1, Y < 2) b. P(1 < X < 2)
c. P(Y > 3) d. P(X < 2, Y < 2)
e. E(X) f. E(Y)
g. Marginal probability distribution of X

## Section 5.2
### Problem 