#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains a single integer t (1 <= t <= 10^3) — the number of test cases. Each test case contains a single integer n (3 <= n <= 10^5) — the length of the permutation p.
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(a)
    #This is printed: a list of integers from 1 to t where all elements at even indices are reversed

#Overall this is what the function does:Reverses elements at even indices in a list of integers from 1 to a given number t, and prints the modified list.

