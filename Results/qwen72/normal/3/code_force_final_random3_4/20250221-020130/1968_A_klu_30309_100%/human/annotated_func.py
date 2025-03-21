#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and test_cases is a list of integers where each integer x in the list satisfies 2 <= x <= 1000.
def func_1(t, test_cases):
    results = []
    for x in test_cases:
        max_sum = 0
        
        best_y = 1
        
        for y in range(x - 1, 0, -1):
            gcd_val = math.gcd(x, y)
            current_sum = gcd_val + y
            if current_sum > max_sum:
                max_sum = current_sum
                best_y = y
                break
        
        results.append(best_y)
        
    #State: t is an integer such that 1 <= t <= 1000, test_cases is a list of integers where each integer x in the list satisfies 2 <= x <= 1000, results is a list of integers where each integer is the largest y (1 <= y < x) such that the sum of y and the greatest common divisor (gcd) of x and y is maximized for each x in test_cases.
    return results
    #The program returns the list 'results' where each element is the largest integer y (1 <= y < x) for each x in the list 'test_cases', such that the sum of y and the greatest common divisor (gcd) of x and y is maximized.
#Overall this is what the function does:The function `func_1` accepts an integer `t` and a list of integers `test_cases`. For each integer `x` in `test_cases`, it finds the largest integer `y` (1 <= y < x) such that the sum of `y` and the greatest common divisor (gcd) of `x` and `y` is maximized. The function returns a list `results` containing these values of `y` for each `x` in `test_cases`. The input parameters `t` and `test_cases` remain unchanged after the function execution.

