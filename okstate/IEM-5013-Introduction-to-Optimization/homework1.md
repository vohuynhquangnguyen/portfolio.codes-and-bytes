### Problem 1
A company sells many household products through an online catalog. The com-
pany needs substantial warehouse space for storing its goods. Plans are now being made
for leasing warehouse storage space over the next 5 months. Just how much space will be
required in each of these months is listed in the table below.

|Month | Space required in sq-ft |
|------|-------------------------|
|1 | 30,000 |
|2 | 20,000 |
|3 | 40,000 |
|4 | 10,000 |
|5 | 50,000 |

| Leasing period in months | Cost per sq-ft leased |
|--------------------------|-----------------------|
| 1 | $65 |
| 2 | $100 |
| 3 | $135 |
| 4 | $160 |
| 5 | $190 |

Assume that several leases of different durations, over different time windows, and different
amounts warehouse space can be held concurrently, over the planning horizon. Formulate a
linear optimization model to help the company identify an optimal combination of leases that
meets its needs.

***
**Answer:**
1. In this scenario:
  * Decision variables: $x_{i,j}$ the number of $j$ leasing months starting from month $i$.
  * Objective function: we need to minimize the leasing cost:
    * 65x_{1,1} + 100x_{1,2} 

### Problem 2
A round-the-clock manufacturing company has minimal daily requirements for
workers in each of its 4-hour periods as listed in Table 1. Workers may be employed to work
in a shift consisting of either two consecutive periods, or three consecutive periods. Period 1
follows immediately after period 6. Formulate a linear optimization model to find a schedule
that minimizes total labor cost, assuming worker salary is proportional to the number of
periods worked in a shift.

*** 
**Answer:**
