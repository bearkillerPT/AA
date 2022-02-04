# Practical Work Number 2

For this assignmente it was required to build an exact counter and two non deterministic counters:
    - Fixed probability counter. Prob = 1/4
    - Decreasing probability counter. Prob[char] *= 1/sqrt(3)

# ExactCounter.py
A simple module that counts every char in the file provided!
```
    python3 ExactCounter.py filename
```
# LossyCounter.py
This module counts with a fixed probability, set to 1/4. With this probability it counts every character.
```
    python3 LossyCounter.py filename k
```
# CounterStats.py
This module runs serves to simulate n_tests, 1000 by default, of the counter_type given the file. It calculates statistics such as max, min, avg, abs error, relative error and expected values.
In this specific counter (LossyCounter) the runs will all produce the same results since the k is static so there«s no need for multiple runs.
```
     python3 CounterStats.py counter_type filename k 
        k - k paramether for the LossyCounter.
```
