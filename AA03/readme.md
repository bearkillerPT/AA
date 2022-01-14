# Practical Work Number 2

For this assignmente it was required to build an exact counter and two non deterministic counters:
    - Fixed probability counter. Prob = 1/4
    - Decreasing probability counter. Prob[char] *= 1/sqrt(3)

# ExactCounter.py
A simple module that counts every char in the file provided!
```
    python3 ExactCounter.py filename
```
# FixedProbCounter.py
This module counts with a fixed probability, set to 1/4. With this probability it counts every character.
```
    python3 FixedProbCounter.py filename
```
# DecreasingProbCounter.py
This module counts with a decreasing probability of factor sqrt(3). Every character begins with probability 1 and gets multiplied by 1/sqrt(3) every time the char is counted.
```
    python3 DecreasingProbCounter.py filename
```
# CounterStats.py
This module runs serves to simulate n_tests, 1000 by default, of the counter_type given the file. It calculates statistics such as max, min, avg, abs error, relative error and expected values.
```
     python3 CounterStats.py counter_type filename [n_tests]
        counter_type := exact | fixed_prob | decreasing_prob
        n_tests - optional. The number of tests.
```
