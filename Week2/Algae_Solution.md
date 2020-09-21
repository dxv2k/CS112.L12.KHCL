# Abstraction
- Find the (2k + 1)-th Fibonacci number.
- Calculate $n * Fibonacci(2k + 1)$
# Pattern Recognition
1. Recursion
2. Dynamic Programing
3. Use Fibonacci Q-Matrix O(n)

# Algorithm designed
- **Input**
  - `n`: Number of individual
  - `k`: The day that we have to calculate how many individuals in the environment
- **Output**
  - Number of individual in the environment, which can be calculate by the function $n * Fibonacci(2k + 1)$
## Method 1: Use Recursion
### Description
The code and the graph below implement for the n-th Fibonancci number.
```python
def fib(n): 
    # First Fibonacci number is 0 
    if n == 0: 
        return 0
    # Second Fibonacci number is 1 
    elif n == 1: 
        return 1
    else: 
        return fib(n - 1) + fib(n - 2)
```
```
                             fib(5)   
                          /         \
                       /             \
                     /                \
               fib(4)                fib(3)   
             /        \              /       \
         fib(3)      fib(2)         fib(2)   fib(1)
        /    \       /    \        /      \
  fib(2)   fib(1)  fib(1) fib(0) fib(1) fib(0)
  /     \
fib(1) fib(0)
```
We can observe that does a lot of repeated work and this is the bad method if we have to find out n-th fibonacci number for very large 'n'. So that we can't use this method to solve this problem.
