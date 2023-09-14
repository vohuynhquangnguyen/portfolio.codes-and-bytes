# Exercises for Section 2.5

## Section 2.5

### Problem 2.5.1
Denote $T$ as the event a leaf completes a textual transformation and $C$ as the event a leaf completes a color transformation.

a.

The probability that a leaf will complete the textural transformation given that it completes the color transformation is computed as:
$$
P(T|C) = \frac{P(T,C)}{P(C)} = \frac{\frac{243}{243 + 26 + 13 +18}}{\frac{243 + 26}{243 + 26 + 13 +18}} \approx 0.9033 
$$

b.

The probability a leaf will complete the color
transformation given that it does not complete the textural transformation is computed as:
$$
P(C|T^C) = \frac{P(C,T^C)}{P(T^C)} = \frac{\frac{26}{243 + 26 + 13 +18}}{\frac{26 + 18}{243 + 26 + 13 +18}} \approx 0.5909 
$$

### Problem 2.5.2
Let $A$ denote the event that a sample has low melanin content, and
let $B$ denote the event that a sample has high moisture content.

a. 
$$
P(A) = \frac{7+32}{100} = 0.39
$$

b.
$$
P(B) = \frac{13+7}{100} = 0.5
$$

c. 
$$
P(A|B) = \frac{P(A,B)}{P(B)} = \frac{7/100}{0.5} = 0.14
$$

d. 
$$
P(B|A) = \frac{P(B,A)}{P(A)} = \frac{7/100}{0.39} \approx 0.1795
$$

### Problem 2.5.3
Denote $A$ as the event deceased beetles are under high autolysis, and $P$ as the event  the deceased beetles are under high putrefaction.

a. 

The probability that the putrefaction is low given that the autolysis of a sample is high is computed as:
$$
P(P^C|A) = \frac{P(P^C,A)}{P(A)} = \frac{\frac{18}{14 + 18 + 59 + 9}}{\frac{14 + 18}{14 + 18 + 59 + 9}} = 0.5625
$$

b. The probability that the autolysis is high given that the putrefaction of a sample is high is computed as:
$$
P(A|P) = \frac{P(A,P)}{P(P)} = \frac{\frac{14}{14 + 18 + 59 + 9}}{\frac{14+59}{14 + 18 + 59 + 9}} = 0.1918
$$

c. The probability that the autolysis is low given that the putrefaction of a sample is low is computed as:
$$
P(A^C|P^C) = \frac{\frac{9}{14 + 18 + 59 + 9}}{\frac{18+9}{14 + 18 + 59 + 9}} \approx 0.3333
$$

### Problem 2.5.6
A batch of 500 containers for frozen orange juice contains 5 that are defective. Three are selected, at random, without
replacement from the batch.

Denote $D$ as the event where a selected batch is defective, and $X_1$, $X_2$, $X_3$ are each of the selected batch, respectively.

a.

The probability that the second one selected is defective given that the first one was defective:
$$
P(X_2 = D|X_1 = D) = \frac{4}{499}
$$
since when the batch is selected in the first pick and is defective, 499 batches would remain, 4 of which are defective, and the rest are acceptable.

b. 

The probability that the first two selected are defective is computed as:
$$
P(X_1 = D, X_2 = D) = \frac{5}{500}\times\frac{4}{499}
$$

c. 

The probability that the first two selected are both
acceptable is computed as:
$$
P(X_1 = D^C, X_2 = D^C)=\frac{500 -5}{500}\times\frac{499 - 5}{499}
$$

d. 

The probability that the third one selected is
defective given that the first and second ones selected were defective is computed as:
$$
P(X_3 = D|X_1 = D, X_2 = D) = \frac{5}{500}\times\frac{4}{499}
$$

e. 

The probability that the third one selected is defective given that the first one selected was defective and the
second one selected was okay
$$
P(X_3 = |X_1 = D, X_2 = D^C) = \frac{5}{500}\times\frac{499 - 4}{499}
$$

f. 

The probability that all three selected ones are defective is computed as:
$$
P(X_1 = D, X_2 = D, X_3 = D) = \frac{5}{500}\times\frac{4}{499}\times\frac{3}{498}
$$

### Problem 2.5.8
a. 

The probability that an egg survies to adulthood is computed as:
$$
P(\text{adulthood}) = \frac{31}{421}
$$

b. 

The probability of survival to adulthood given survival to the late larvae stage is computed as:
$$
P(\text{adulthood}|\text{late larvae}) = \frac{31}{306}
$$

c.

The probability of survival from one stage to another is computed as:
$$
\begin{cases}

\end{cases}
$$

## Section 2.6
### Problem 2.6.1
a.
$$
P(A\cap B) = P(A|B)\times P(B) = 0.4\times0.5 = 0.2
$$

b.
$$
P(A^C\cap B) = P(A^C|B)\times P(B) = \Big(1 - P(A|B)\Big)P(B) = (1 - 0.4)0.5 = 0.3
$$

### Problem 2.6.2
$$
P(A|B) = \frac{P(A,B)}{P(B)}
$$
$$
P(A|B^C) = \frac{P(A,B^C)}{P(B^C)}
$$
According to the rule of total probability, $P(A,B^C) + P(A,B) = P(A)$. Therefore, $P(A)$ is computed as:
$$
P(A) = P(A|B)\bullet P(B) + P(A|B^C)\times P(B^C) = 0.2\times0.8 + 0.3\times(1-0.8)=0.22
$$

### Problem 2.6.3
Denote $C$ as the condition of the connector, whose outcomes are either dry (0) or wet (1), and $S$ as the status of the connector, whose outcomes are either failure (1) or functional (0). Therefore,
* The probability that the connector fails when it is kept dry can be denoted as $P(S = 1|C = 0)$, and $P(S = 1|C = 0) = 0.01$.
* The probability that the connector fails when it is wet can be denoted as $P(S = 1|C = 1)$, and $P(S = 1, C = 1) = 0.05$.
* The probability that the connectors are kept dry can be denoted as $P(C = 0)$, and $P(C = 0) = 0.9$
* The probability that the connectors are wet can be denoted as $P(C = 1)$, and $P(C = 1) = 0.1$

Thus, the probability that the connectors fail is computed as:
$$
P(S = 1) = P(S =1|C = 0)\times P(C=0) + P(S =1 |C = 1)\times P(C = 1) = 0.01\times0.9 + 0.05\times0.1 = 0.014
$$

### Problem 2.6.4
Denote $H$ as the event where a heart failure occurs, whose outcomes are either $NC$ (due to natural occurances), and $OF$ (due to outside factors). Within $NC$, there are three possible outcomes namely arterial blockage $NC_1$, disease $NC_2$ and infection $NC_3$. On the other hand, within $OF$, there are two possible outcomes namely induced substances $OF_1$ and foreign objects $OF_2$.

a.

The probability that a failure is due to an induced substance is computed as:
$$
P(H = OF_1) = P(H = OF)\times P(OF_1) = 0.13\times 0.73 = 0.0949
$$

b.

The probability that a failure is due to disease or infection. 
$$
\begin{aligned}
P(H = NC_2 \cup H = NC_3) &= P(H = NC_2) +  P(H = NC_3) \\
&= P(H = NC)\times P(NC_2) + P(H = NC)\times P(NC_3) \\
&= 0.87\times0.27 + 0.87\times0.17 = 0.3828
\end{aligned} 
$$

### Problem 2.6.5
Denote $K$ as the condition of the knife, whose outcomes are new $K_1$, average $K_2$, and dull $K_3$. Meanwhile, denote $ER$ as the condition of the edge roughness, whose outcomes are either not exhibiting $ER_1$ or exhibiting $ER_2$. Therefore, the proportion of paper products that exhibit edge roughness is computed as:
$$
\begin{aligned}
P(ER = ER_2) &= P(ER_2|K_1)\times P(K_1) + P(ER_2|K_2)\times P_(K_2) + P(ER_2|K_3)\times P(K_3) \\
&= 0.01\times0.25 + 0.03\times0.6+ 0.5\times0.15 \\
&= 0.0955
\end{aligned}
$$

### Problem 2.6.6
a.

The probability that second chip selected to be defective is computed as:
$$
P(X_2 = 1) = P(X_2 = 1|X_1 = 0) + P(X_2 = 1|X_1 = 1) = \frac{20}{99}\times\frac{100-20}{100} + \frac{19}{99}\times\frac{20}{100} = 0.2
$$

b. 
The probability that all are defective is computed as:
$$
P(X_1 = 1, X_2 = 1, X_3 = 1) = \frac{20}{100}\times\frac{19}{99}\times\frac{18}{98} \approx 0.0070
$$

### Problem 2.6.7

### Problem 2.6.8

## Section 2.7
### Problem 2.7.1
$B$ and $A^C$ are independent when $P(A^C,B) = P(B)\times P(A^C)$. Hence, we need to check whether this relationship is true.
* In this case, $P(B) = 0.8$ and $P(A^C) = 1 - P(A) = 1 - 0.3 = 0.7$. Therefore, $P(A^C)\times P(B) = 0.7\times0.8 = 0.56$.
* Meanwhile, $P(A|B) = 1 - P(A^C|B)$. Thus, $P(A^C|B) = 1 - 0.3 = 0.7$. Therefore, $P(A^C,B) = P(A^C|B)\times P(B) = 0.56$
As a result, these events $B$ and $A^C$ are independent.


### Problem 2.7.2
In this case, $A$ and $B$ are mutually exclusive events, so $P(A,B) = 0$. For $A$ and $B$ to be independent from one to another, $P(A,B) = P(A)\times P(B)$. Since  $P(A,B) = 0 \neq P(A)\times P(B)$, these events are not independent.

### Problem 2.7.3
Denote $A$ and $B$ as events that the first and second containers selected are defective, respectively.

a.

For $A$ and $B$ to be independent events, these relationship have to hold true:
$$
\begin{cases}
P(A,B) = P(A)\times P(B) \\ 
P(A|B) = P(A|B^C) = P(A) \\
P(B|A) = P(B|A^C) = P(B) 
\end{cases}
$$

In this scenario, the probability that the first container is defective is given as $P(A) = \frac{5}{500}$. Meanwhile, the probability that the second container is defective is given as $P(B) = \frac{4}{499}$ as one defective container is already selected. Since the presence of $A$ influences the presence of $B$, $A$ and $B$ are not independent.

b.
When sampling were done with replacement, $A$ and $B$ would be independent because:
* The probability that the first container is defective is $P(A) = \frac{5}{500}$.
* The probability that the second container is defective is still $P(B) = \frac{5}{500}$ as even though the first selected container is defective, it is placed back into the batch for the next sample.

### Problem 2.7.11
Denote
* $A_1$,$A_2$ are elements in the first combination.
* $B_1$,$B_2$ are elements in the second combination.
* $C_1$, $C_2$ are elements in the third combination.

In this circuitry,
* The first combination works when either $A_1$ or $A_2$ works. Hence, the probability that the first combination works is computed as:
$$
\begin{aligned}
P(A) &= P(A_1,A_2) + P(A_1^C,A_2) + P(A_1,A_2^C) \\
&= 0.9\times0.95 + (1-0.9)\times0.95 + 0.9\times(1-0.95) \\
&= 0.995
\end{aligned}
$$

* The second combination works when either $B_1$ or $B_2$ works. Hence, the probability that the second combination works is computed as:
$$
\begin{aligned}
P(B) &= P(B_1,B_2) + P(B_1^C,B_2) + P(B_1,B_2^C) \\
&= 0.9\times0.95 + (1-0.9)\times0.95 + 0.9\times(1-0.95) \\
&= 0.995
\end{aligned}
$$
* The third combination works when either $C_1$ or $C_2$ works. Hence, the probability that the third combination works is computed as:
$$
\begin{aligned}
P(C) &= P(C_1,C_2) + P(C_1^C,C_2) + P(C_1,C_2^C) \\
&= 0.8\times0.9 + (1-0.8)\times0.9 + 0.8\times(1-0.9) \\
&= 0.98
\end{aligned}
$$

* The circuit works when all these combinations work, hence
$$
P = P(A)\times P(B) \times P(C) \approx 0.9702
$$

### Problem 2.7.12