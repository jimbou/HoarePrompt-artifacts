#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. For each test case, a, b, and m are positive integers such that 1 <= a, b, m <= 10^18.
def func():
    t = int(input())
    for _ in range(t):
        a, b, m = map(int, input().split())
        
        A = int(m / a) + 1
        
        B = int(m / b) + 1
        
        print(A + B)
        
    #State: `t` is 0; `a`, `b`, and `m` are the values from the last iteration; `A` is `int(m / a) + 1` from the last iteration; `B` is `int(m / b) + 1` from the last iteration.
#Overall this is what the function does:The function accepts a positive integer `t` indicating the number of test cases. For each test case, it accepts three positive integers `a`, `b`, and `m`. It then calculates and prints the sum of `int(m / a) + 1` and `int(m / b) + 1`.

