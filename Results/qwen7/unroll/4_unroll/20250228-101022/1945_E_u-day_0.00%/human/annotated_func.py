#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2⋅10^4. Each test case consists of two integers n and x such that 1 ≤ x ≤ n ≤ 2⋅10^5, followed by a list of n integers representing the permutation p where each integer in p is unique and within the range 1 to n.
def func_1():
    return map(int, input().split())
    #The program returns a map object containing two integers, which are the result of splitting the input string on spaces. The first integer is the value of t (1 ≤ t ≤ 2⋅10^4), and the second integer is the value of x (1 ≤ x ≤ n ≤ 2⋅10^5).
#Overall this is what the function does:The function reads a line of input from the standard input, splits it into two integers based on spaces, and returns a map object containing these two integers. The first integer represents the value of t (1 ≤ t ≤ 2⋅10^4), and the second integer represents the value of x (1 ≤ x ≤ n ≤ 2⋅10^5).

#State of the program right berfore the function call: t is a positive integer representing the number of test cases. Each test case consists of two integers n and x, where 1 ≤ x ≤ n ≤ 2⋅10^5, and a permutation p of size n consisting of distinct integers from 1 to n.
def func_2():
    return list(func_1())
    #The program returns a list generated by func_1(), which is not defined in the given information.
#Overall this is what the function does:The function does not accept any direct parameters. It relies on another function `func_1()` to generate a list, which is then returned by this function. The final state of the program is that it returns a list of elements generated by `func_1()`.

