#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        print(x + y)
        
    #State: After processing all `t` test cases, the program will have printed the sum of occurrences of "map" and "pie" for each test case. The variables `t`, `a`, and `s` will not retain any specific value as they are re-assigned in each iteration.
#Overall this is what the function does:The function reads multiple test cases, where each test case consists of an integer `n` and a string `s` of length `n`. For each test case, it calculates the total number of non-overlapping occurrences of the substrings "map" and "pie" in the string `s` and prints this count.

