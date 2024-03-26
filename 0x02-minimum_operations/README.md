# Minimum Operations
`Algorithm` `Python`

## task

In a text file, there is a single character `H`. Your text editor can execute only two operations in this file: `Copy All` and `Paste`. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n H` characters in the file.

Prototype: `def minOperations(n)`
Returns an `integer`
If `n` is impossible to achieve, return `0`
Example:

```bash
n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
```
Number of operations: 6


## Solution

- At first, I took a good look at the problem and thought about what's really going on. It didn't take long for me to realize that the key to solving it lies in simplifying things. That's when I hit upon the idea of using prime factorization.

- To make things easier, I tried to break down the problem into its core elements. What really influences the number of operations we need? That's when I started thinking about prime factorization.

- It suddenly clicked: the sum of those prime factors is actually the minimum number of operations