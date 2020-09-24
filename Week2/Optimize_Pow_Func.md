# Power function
Use can calculate power by using `for` loop
```python
def multiply (a, b):
    a = a * b

def power (a, n):
    for _ in range(n):
        multiply(a, a)
```
**Time Complexity:** $O(n)$
# Optimze power function
Above function can be optimized to $O(logn)$ by divides the problem into subproblems of size $n/2$ and call the subproblems recursively.
```python
def power (a, n):
    if (n == 1 or n == 0):
        return
    a_origin = a
    power(a, n // 2)
    multiply(a, a)
    if (n%2 != 0):
        multiply(a, a_origin)
```
You can see source code [here](pow_func.py)
