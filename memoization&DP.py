# Dictionary to store calculated Fibonacci numbers
fib_cache = {}

def fibonacci(n):
    if n in fib_cache:
        # If the value is already calculated, return it from the cache
        return fib_cache[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Calculate the Fibonacci number recursively
        fib_value = fibonacci(n - 1) + fibonacci(n - 2)
        # Cache the result for future use
        fib_cache[n] = fib_value
        return fib_value

# Example usage
num = 10
print(f"Fibonacci({num}): {fibonacci(num)}")

            #  DYNAMIC PROGRAMMING
# Dynamic programming is a method for solving complex problems by breaking them down into simpler subproblems. It is particularly useful for optimization problems where you need to find the best solution among many possible solutions. Dynamic programming is based on the principle of overlapping subproblems, which means that the same subproblems are solved multiple times in the process of solving the main problem.

# The key idea behind dynamic programming is to solve each subproblem only once and store the solution in a table (usually an array or a matrix). Then, when you encounter the same subproblem again, you can simply look up the solution in the table, rather than recomputing it. This allows dynamic programming algorithms to achieve better time complexity compared to naive recursive approaches.

#       There are two main approaches to dynamic programming:

# (i)Top-down approach (memoization): In this approach, you start from the top (the original problem) and recursively solve the subproblems, storing the solutions in a table (memoization). This way, you avoid solving the same subproblem multiple times.

# (ii)Bottom-up approach (tabulation): In this approach, you start from the bottom (the simplest subproblems) and iteratively build up the solutions to larger subproblems. You use a table to store the solutions to subproblems, and each entry in the table depends only on the solutions to smaller subproblems.

# USING DYNAMIC PROGRAMMING 
fibtable = {}
def fib(n):
    fibtable[0] = 0
    fibtable[1] = 1
    for i in range(2,n+1):
        fibtable[i] = fibtable[i-1] + fibtable[i-2]
    return(fibtable[n])

print(fib(10))