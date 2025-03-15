# Algo2. Home work 2
## "Greedy algorithms and dynamic programming"

### Task 1. Optimization of the 3D printer queue in a university laboratory

Develop a program to optimize the 3D printing queue in a university laboratory, taking into account task priorities and technical limitations of the printer, using the greedy algorithm.

### Task description

1. Use the input data in the form of a list of tasks for printing, where each task contains: ID, model volume, priority, and printing time.

2. Implement the main function optimize_printing, which will:

 - Take into account task priorities.
 - Group models for simultaneous printing.
 - Check volume and quantity limitations.
 - Calculate the total printing time.
 - Return the optimal printing order.

3. Print the optimal printing order and the total time required to complete all tasks.


### Task 2. Optimal rod cutting for maximum profit (Rod Cutting Problem)

Develop a program to find the optimal way to cut a rod to get the maximum profit. It is necessary to implement two approaches: using recursion with memoization and using tabulation.

### Task description

1. The input is the length of the rod and the array of prices, where `price[i]` is the price of the rod of length `i+1` .

2. It is necessary to determine how to cut the rod to get the maximum profit.

3. Implement both approaches of dynamic programming.

4. Output the optimal way of cutting and the maximum profit.
