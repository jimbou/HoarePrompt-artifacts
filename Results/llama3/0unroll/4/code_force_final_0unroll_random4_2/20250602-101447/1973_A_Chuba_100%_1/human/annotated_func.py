#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers p_1, p_2 and p_3 (0 <= p_1 <= p_2 <= p_3 <= 30) — the scores of the three players, sorted non-decreasingly.
    t = int(input())
    for _ in range(t):
        v = list(map(int, input().split()))
        
        if (v[0] + v[1] + v[2]) % 2 == 1:
            print('-1')
        else:
            result = (v[0] + v[1] + v[2] - max(0, v[2] - v[0] - v[1])) // 2
            print(result)
        
    #State: The output state will be a list of integers, where each integer is the result of the calculation for each test case. The result will be either -1 or a positive integer, depending on whether the sum of the three scores is odd or even, respectively. The output state will have the same number of elements as the number of test cases minus one.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers representing the scores of three players. It then calculates and prints the result for each test case. If the sum of the three scores is odd, it prints -1. If the sum is even, it calculates the result as half of the sum of the scores minus the maximum of 0 and the difference between the highest and lowest scores. The function outputs a list of integers, where each integer is the result of the calculation for each test case, with the same number of elements as the number of test cases.

