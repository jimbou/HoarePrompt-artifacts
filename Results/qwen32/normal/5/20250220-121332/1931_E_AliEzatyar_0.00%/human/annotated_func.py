#State of the program right berfore the function call: num is a list of integers where the first integer t (1 ≤ t ≤ 10^4) represents the number of test cases. Each test case consists of two lines: the first line contains two integers n (1 ≤ n ≤ 2 · 10^5) and m (0 ≤ m ≤ 2 · 10^6), and the second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9). The sum of n across all test cases does not exceed 2 · 10^5.
def func_1(num):
    counter = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] == '0':
            counter += 1
        else:
            break
        
    #State: `counter` is the number of trailing '0's in `num`, and `i` is the index of the first non-zero element from the end of the list, or -1 if the entire list consists of '0's.
    return counter
    #The program returns the number of trailing '0's in `num`
#Overall this is what the function does:The function `func_1` accepts a list of integers `num` and returns the number of trailing '0's in that list.

