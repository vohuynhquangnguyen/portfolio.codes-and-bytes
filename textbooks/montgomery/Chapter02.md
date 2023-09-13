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

## 