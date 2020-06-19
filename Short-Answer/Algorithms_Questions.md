# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

n = 1, runs = 1, a = 1
n = 5, runs = 5, a = 125
n = 10, runs = 10, a = 1000
O(n)

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

O(n log n)

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

n = 1, runs = 2, return = 2
n = 5, runs = 6, return = 10
n = 10, runs = 11, return = 20
O(n+1)

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.
