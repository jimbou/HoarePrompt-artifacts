#State of the program right berfore the function call: The function should accept a list of test cases, where each test case is a list of four tuples, each tuple containing two integers (x_i, y_i) representing the coordinates of the corners of a square. The coordinates are within the range -1000 <= x_i, y_i <= 1000, and the square has a positive area with sides parallel to the coordinate axes. The number of test cases, t, is an integer such that 1 <= t <= 100.
def func():
    t = int(input())
    for steps in range(t):
        a, b = map(int, input().split())
        
        c, d = map(int, input().split())
        
        e, f = map(int, input().split())
        
        g, h = map(int, input().split())
        
        n = (a - e) * (a - e) + (b - f) * (b - f)
        
        x = (c - g) * (c - g) + (d - h) * (d - h)
        
        if x > n:
            print(n)
        else:
            print(x)
        
    #State: `t` is an integer such that 1 <= t <= 100, `steps` is `t-1`, `a`, `b`, `c`, `d`, `e`, `f`, `g`, and `h` are the last set of integers provided by the user, `n` is equal to (a - e) * (a - e) + (b - f) * (b - f), `x` is equal to (c - g) * (c - g) + (d - h) * (d - h). If `x` > `n`, then `x` is greater than `n`. Otherwise, `x` is less than or equal to `n`.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, representing the number of test cases. For each test case, it reads four pairs of integers (coordinates) from the user. It calculates the squared distances `n` and `x` between the first and third pairs, and the second and fourth pairs, respectively. It then compares these distances and prints the smaller of the two. After processing all test cases, the function ends, and the program state is such that `t` test cases have been processed, and the smaller squared distance for each test case has been printed.

