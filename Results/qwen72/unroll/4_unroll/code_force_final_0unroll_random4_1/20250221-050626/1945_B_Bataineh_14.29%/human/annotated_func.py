#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, a, b, and m are integers such that 1 <= a, b, m <= 10^18.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a or m < b:
            print(2)
        else:
            print(m // a + m // b + 2)
        
    #State: The loop has finished executing all t iterations. For each iteration, if m is less than a or b, the output is 2. Otherwise, the output is the sum of m divided by a, m divided by b, and 2. The values of t, a, b, and m are unchanged after each iteration.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `m` from the input. If `m` is less than either `a` or `b`, the function prints `2`. Otherwise, it prints the sum of `m` divided by `a`, `m` divided by `b`, and `2`. After processing all `t` test cases, the function completes, and the values of `t`, `a`, `b`, and `m` are not modified within the function.

