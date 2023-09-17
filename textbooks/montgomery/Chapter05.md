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