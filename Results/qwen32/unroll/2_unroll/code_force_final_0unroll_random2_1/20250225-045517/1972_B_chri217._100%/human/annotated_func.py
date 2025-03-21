#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 100, n is a positive integer such that 1 <= n <= 100 for each test case, and s is a string of length n containing only the characters "U" and "D".
def func_1():
    t = int(sys.stdin.readline().strip())
    cases = []
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        
        s = sys.stdin.readline().strip()
        
        cases.append((n, s))
        
    #State: `t` is the integer read from the input (1 <= t <= 100), `n` is the integer from the last iteration of the loop (1 <= n <= 100), `s` is the string from the last iteration of the loop containing only the characters "U" and "D", `cases` is a list of tuples, where each tuple contains the `n` and `s` values from each iteration of the loop.
    return cases
    #The program returns a list of tuples, where each tuple contains the `n` and `s` values from each iteration of the loop.
#Overall this is what the function does:The function reads multiple test cases from the standard input, where each test case consists of an integer `n` and a string `s` of length `n` containing only "U" and "D". It returns a list of tuples, each containing the `n` and `s` values from each test case.

#State of the program right berfore the function call: case is a tuple where the first element is an integer n (1 <= n <= 100) representing the number of coins, and the second element is a string of length n consisting of characters 'U' and 'D', where 'U' represents a coin facing up and 'D' represents a coin facing down.
def func_2(case):
    ups = sum(1 for c in case[1] if c == 'U')
    return 'YES' if ups % 2 else 'NO'
    #The program returns 'YES' if the count of 'U' characters in the string part of `case` is even, otherwise it returns 'NO'
#Overall this is what the function does:The function takes a tuple as input, where the first element is an integer representing the number of coins and the second element is a string of 'U' and 'D' characters indicating the orientation of each coin. It returns 'YES' if the number of 'U' characters in the string is even, otherwise it returns 'NO'.

