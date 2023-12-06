# Convex Optimization

## Alternating direction method of multipliers (ADMM)
### Overview
1. Suppose we have the following linear optimization problem:
    * Canonical form:
        $$
        \max \quad \zeta = x_1 + 2x_2 + 4x_3 \\
        s.t.
        \begin{cases}
            3x_1 + x_2 + 5x_3 \leq 10 \\
            x_1 + 4x_2 + x_3 \leq 8 \\
            2x_1 + 0x_2 + 2x_3 \leq 7 \\
        \end{cases}
        $$
    * Standard form (please noted that we can transform a linear program from the canonical form to a standard form by introducing slack/surplus variables on LHS of the constraints):
        $$
        \max \quad \zeta = x_1 + 2x_2 + 4x_3 \\
        s.t.
        \begin{cases}
            3x_1 + x_2 + 5x_3 + w_1 = 10 \\
            x_1 + 4x_2 + x_3 + w_2 =  8 \\
            2x_1 + 0x_2 + 2x_3 + w_3 = 7 \\
        \end{cases}
        $$

2. We can express this problem as a minimization problem:
    $$
    \min \quad \zeta = -x_1 -2x_2 -4x_3 \\
    s.t.
    \begin{cases}
        3x_1 + x_2 + 5x_3 + w_1 = 10 \\
        x_1 + 4x_2 + x_3 + w_2 =  8 \\
        2x_1 + 0x_2 + 2x_3 + w_3 = 7 \\
    \end{cases}
    $$

3. Hence, the matrix notation of this problem is given as:
$$
\min \quad \mathbf{c}^T\mathbf{x} \\
s.t. \quad \mathbf{A}\begin{bmatrix}\mathbf{x} \\ \mathbf{w} \end{bmatrix} = \mathbf{b}
$$
with $\mathbf{c} = \begin{bmatrix} -1 \\ -2 \\ -4 \\ 0 \\ 0 \\ 0 \end{bmatrix}$, $\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ w_1 \\ w_2 \\ w_3 \end{bmatrix}$,
$\mathbf{A} = \begin{bmatrix} 3 & 1 & 5 & 1 & 0 & 0 \\ 1 & 4 & 1 & 0 & 1 & 0 \\ 2 & 0 & 2 & 0 & 0 & 1 \end{bmatrix}$, and $\mathbf{b} = \begin{bmatrix} 10 \\ 8 \\ 7\end{bmatrix}$

For simplification, we can rewrite the slack variables $w_1, w_2, w_3$ as $x_4, x_5, x_6$. Hence, the matrix-form of our problem is now given as:
$$
\min \quad \mathbf{c}^T\mathbf{x} \\
s.t. \quad \mathbf{A}\mathbf{x} = \mathbf{b}
$$

4. To use ADMM to solve this optimization problem, we first need reformulate this problem into the following form:
$$
\min \quad \mathbf{c}^T\mathbf{x} + p(\mathbf{x}) + g(\mathbf{y})\\
s.t. \quad \mathbf{x} = \mathbf{y}
$$
where $\mathbf{y}$ is a newly introduced optimization variable, $p$ and $g$ are indicator functions, with respect to constraint sets $\{\mathbf{x}|\mathbf{A}\mathbf{x}=\mathbf{b}\}$ and $\{\mathbf{y}|\mathbf{y}\geq0\}$,
respectively. As a result, the ADMM steps to solve this problem are:
* **Step 1**: we need to solve this optimization problem: 
$$
\tag{P1}
\min \quad \frac{\rho}{2} ||\mathbf{x} - \alpha||^2_2\\
s.t. \quad \mathbf{A}\mathbf{x} = \mathbf{b}
$$

* Step 2: we need to solve this optimization problem:
$$
\tag{P2}
\min \quad \frac{\rho}{2} ||\mathbf{y} - \beta||^2_2\\
s.t. \quad \mathbf{y} \geq 0
$$

* Step 3: we need to compute:
$$
\tag{P3}
\pmb{\mu}^{\{k+1\}} = \pmb{\mu}^{\{k\}} + \rho\Big(\mathbf{x}^{\{k+1\}} + \mathbf{y}^{\{k+1\}}\Big)
$$

#### Step 1
Basically speaking, what we are doing when solving Problem $\text{(P1)}$ is to find the value $\mathbf{x}$  at the $k+1$ iteration, which is denoted as $\mathbf{x}^{\{k+1\}}$. To do so,
* First, we need to determine the values of $\mathbf{y}$ and $\pmb{\pmb{\mu}}$ at the $k$ iteration, which denoted as $\mathbf{y}^{\{k\}}$ and $\pmb{\pmb{\mu}}^{\{k\}}$, respectively.
* Next, we construct the matrix $\mathbf{C}$ such that: $\mathbf{C} = \begin{bmatrix} \rho\mathbf{I} & \mathbf{A}^T \\ \mathbf{A} & 0  \end{bmatrix}$.
* Finally, we solve the following systems of linear equations to get $\mathbf{x}^{\{k+1\}}$: 
$$
\mathbf{C}\begin{bmatrix}\mathbf{x} \\ \pmb{\lambda} \end{bmatrix}= \begin{bmatrix} \rho\alpha \\ \mathbf{b} \end{bmatrix}
$$
with $\alpha := \mathbf{y}^{\{k\}} - \frac{1}{\rho}\Big(\pmb{\mu}^{\{k\}} + \mathbf{d}\Big)$.

#### Step 2
Basically speaking, what we are doing when solving Problem $\text{P(2)}$ is to find the value of $\mathbf{y}$ at the $k+1$ iteration, which is denoted as $\mathbf{y}^{\{k+1\}}$. To do so,
* First, we need to construct $\pmb{\beta} = \mathbf{x}^{\{k+1\}} + \frac{1}{\rho}\pmb{\mu}^{\{k\}}$.
* Then, we project the recently constructed vector $\pmb{\beta}$ onto the non-negative orthant to find $\mathbf{y}^{\{k+1\}}$: 
$$
\mathbf{y}^{\{k+1\}} = \Big(\pmb{\beta}\Big)_+
$$

#### Step 3
Basically speaking, what we are doing when solving Problem $\text{P(3)}$ is to find $\pmb{\mu}$ at the $k+1$ iteration, denoted as $\pmb{\mu}^{\{k+1\}}$. 

### Example
This demonstration showcases the application of the Alternating Direction Method of Multipliers (ADMM) in solving a variety of linear optimization problems. It is important to note that the problems presented in this demo are known to have optimal solutions.