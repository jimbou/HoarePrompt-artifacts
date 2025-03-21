#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, x and y are integers such that 0 ≤ x, y ≤ 9.
def func():
    t = input()
    x = []
    y = []
    for i in range(10):
        xylist = input().split(' ')
        
        x.append(int(xylist[0]))
        
        y.append(int(xylist[1]))
        
    #State: Output State: `t` is an integer between 1 and 100 inclusive, `x` is a list with 10 integers, `y` is a list with 10 integers.
    for i in range(10):
        if x[i] < y[i]:
            print(x[i], ' ', y[i])
        else:
            print(y[i], ' ', x[i])
        
    #State: Output State: The output state will consist of 10 lines, each containing two integers separated by a space. For each iteration `i` from 0 to 9, if the value at index `i` in list `x` is less than the value at the same index in list `y`, it will print the value from `x` followed by the value from `y`. Otherwise, it will print the value from `y` followed by the value from `x`.
#Overall this is what the function does:The function reads an integer `t` and two lists of integers `x` and `y` from the input. It then compares the corresponding elements of `x` and `y` and prints 10 lines, each containing two integers. If the element in `x` is less than the corresponding element in `y`, it prints the element from `x` followed by the element from `y`. Otherwise, it prints the element from `y` followed by the element from `x`. The function does not return any value.

