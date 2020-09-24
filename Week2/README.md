<a href="https://colab.research.google.com/github/dxv2k/CS112.L12.KHCL/blob/master/Week2/Algae_Solution.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

Please use Google Colab to view for better render!
# [Algae Problem](./Algae.md)
![Algae Evolved](https://user-images.githubusercontent.com/48788781/94126485-df5ef500-fe81-11ea-8d3d-a7636531ebd1.png)
We have create a table that calculate individuals day by day with `n = 1`
| DAY | $a_1$ | $a_2$ | $a_3$ | $a_4$ | $a_5$ | Total_individuals |
|:---:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----------------:|
|  0  |   1   |  None |  None |  None |  None |         1         |
|  1  |   1   |   1   |  None |  None |  None |         3         |
| 2   |   3   |   1   |   1   |  None |  None |         5         |
| 3   |   8   |   3   |   1   |   1   |  None |         13        |
| 4   |   21  |   8   |   3   |   1   |   1   |         34        |

We recognize that `Total_individuals` looks like an array of Fibonancci. Let's look at the Fibonancci array below:
| n                 | 0 | 1 | 2 |  3 |  4 |  5 |  6  |  7 |  8 |  9 |
|-------------------|:-:|:-:|:-:|:--:|:--:|:--:|:---:|:--:|:--:|:--:|
| Fib(n)            | 0 | 1 | 1 |  2 |  3 |  5 |  8  | 13 | 21 | 34 |
| Fib($2k+1$)       | 1 | 3 | 5 | 13 | 34 | 89 | 233 |    |    |    |
| Total_individuals | 1 | 3 | 5 | 13 | 34 |    |     |    |    |    |

With the table above we can recognize that the `Total_individuals` array are same as `Fib(2k+1)` array so the total individuals in the k-th day is the (2k+1)-th Fibonancci number. If `n != 1`, we multiply `n` with `Fib(2k+1)` to calculate that.

## Abstraction
- Find the (2k + 1)-th Fibonacci number.
- Calculate `n * Fibonacci(2k + 1)`
## Pattern Recognition
1. [Recursion](#method-1-use-recursion)
2. [Use Fibonacci Q-Matrix](#method-2-use-fibonacci-q-matrix-on)

## Algorithm designed
- **Input**
  - `n`: Number of individual in the first day.
  - `k`: The day that we have to calculate how many individuals in the environment
- **Output**
  - Number of individual in k-th day, which can be calculate by the function $n * Fibonacci(2k + 1)$
### **Method 1:** Use Recursion
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
We can observe that does a lot of repeated work and this is the bad method if we have to find out n-th fibonacci number for very large 'n'. With a large input size (10^18) and as we know Fibonacci can growth exponentially at 1000th which lead to insufficient memory, so we can't use this method to solve problem.  

**Time complexity:** $O(2^n)$
### **Method 2:** Use Fibonacci Q-Matrix O(n)
$$\begin{pmatrix}
1 & 1\\
1 & 0
\end{pmatrix} ^ n = 
\begin{pmatrix}
F_{n+1} & F_n\\
F_n & F_{n-1}
\end{pmatrix}
$$
[The Fibonacci Q-Matrix](https://mathworld.wolfram.com/FibonacciQ-Matrix.html) can help us find out the n-th Fubonancci number by calculate `power(Q-Matrix, n)`, then we get the (n+1)-th Fibonacci number as the element at row and column (0, 0) in the resultant matrix.

- **Time complexity:** $O(n)$
- **Space complexity:** $O(1)$

```python
def fib(n): 
    F = [[1, 1], 
         [1, 0]] 
    if (n == 0): 
        return 0
    power(F, n - 1) 
      
    return F[0][0] 
  
def multiply(F, M):
  
    x = (F[0][0] * M[0][0] + 
         F[0][1] * M[1][0]) 
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1]) 
    z = (F[1][0] * M[0][0] + 
         F[1][1] * M[1][0]) 
    w = (F[1][0] * M[0][1] + 
         F[1][1] * M[1][1]) 
      
    F[0][0] = x  %1000000007
    F[0][1] = y  %1000000007
    F[1][0] = z  %1000000007
    F[1][1] = w  %1000000007
  
def power(F, n): 
  
    if( n == 0 or n == 1): 
        return; 

    M = [[1, 1],
         [1, 0]]
  
    # n - 1 times multiply the 
    # matrix to {{1,0},{0,1}} 
    for i in range(2, n + 1):
        multiply(F, M)

```

Above `power(F, n)` function can be optimized to $O(log(n))$ like [this](Optimize_Pow_Func.md) by divides the problem into subproblems of size $n/2$ and call the subproblems recursively.
```python
def power(F, n): 
  
    if( n == 0 or n == 1): 
        return; 
    M = [[1, 1], 
         [1, 0]]; 
          
    power(F, n // 2) 
    multiply(F, F) 
          
    if (n % 2 != 0): 
        multiply(F, M)
```