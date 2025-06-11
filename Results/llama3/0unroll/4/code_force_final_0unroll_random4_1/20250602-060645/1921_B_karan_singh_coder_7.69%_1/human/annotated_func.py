#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three lines. The first line contains a single integer n (1 <= n <= 10^5). The second line contains a string s of n characters, where the i-th character is '1' if there is a cat in the i-th box and '0' otherwise. The third line contains a string f of n characters, where the i-th character is '1' if there should be a cat in the i-th box and '0' otherwise. The sum of n over all test cases does not exceed 10^5.
    for _ in range(int(input())):
        n = int(input())
        
        s = input()
        
        t = input()
        
        s1 = s.count('1')
        
        t1 = t.count('1')
        
        cnt = 0
        
        for i in range(n):
            cnt += s[i] != t[i]
        
        if s1 == t1:
            print(s1 if cnt else 0)
        else:
            d = abs(s1 - t1)
            print((cnt - d) // 2 + d)
        
    #State: The output state will be the number of cats in the boxes after all the iterations of the loop have finished. The number of cats will be the sum of the number of cats in the boxes where the initial state and the target state are the same, and the number of cats that need to be moved to achieve the target state.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: the number of boxes, the initial state of the boxes (cats or no cats), and the target state of the boxes. It then calculates and prints the minimum number of cats that need to be moved to achieve the target state, considering the cases where the number of cats in the initial and target states are equal or different. The function iterates through all test cases and outputs the result for each case.

