#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of two lines: the first line contains an integer n (2 <= n <= 50), and the second line contains n space-separated integers a_1, a_2, ..., a_n (0 <= a_i <= 1) such that at least one a_i is 1.
    """
     
    0 과 1로 이루어진 배열을 받고 난 후 
    0으로만 연속되고 1으로만 연속된 하나의 블록으로 만드는 것이 목표임
    오른쪽에 있는 1을 가장 가까운 왼쪽으로 옮겨서 독립된 0, 1 블록으로 만들어야 함
     
    그냥 중간에 비어있는 0의 갯수가 정답일 듯
     
    """
    t = int(input())
    for _ in range(t):
        length = int(input())
        
        arrs = list(map(int, input().split()))
        
        cnt0 = 0
        
        for idx in range(len(arrs)):
            if arrs[0] == 0 and idx != 0:
                if arrs[idx] == 0:
                    cnt0 += 1
            elif arrs[0] == 1:
                if arrs[idx] == 0:
                    cnt0 += 1
        
        cnt1 = 0
        
        for idx in range(len(arrs)):
            if arrs[idx] == 1:
                cnt1 += 1
        
        if arrs[0] == 0:
            if arrs[len(arrs) - 1] == 0:
                cnt0 -= 1
        
        ans = 0
        
        if cnt1 == 1 or cnt1 == 0:
            ans = 0
        else:
            ans = cnt0
        
        print(ans)
        
    #State: t is an integer between 1 and 1000 and must be greater than or equal to 0, _ is equal to t, length is an integer between 2 and 50 inclusive, arrs is a list of n space-separated integers a_1, a_2, ..., a_n (0 <= a_i <= 1) such that at least one a_i is 1 and must have at least n elements, idx is equal to len(arrs), cnt1 is equal to the number of 1's in arrs, cnt0 is equal to the number of zeros in arrs, stdin contains no input. If cnt1 is 0 or 1, ans is 0. Otherwise, ans is equal to cnt0, and the value of ans is being printed which is either 0 if cnt1 is 0 or 1, otherwise it is equal to cnt0.

#Overall this is what the function does:This function takes an integer t (1 <= t <= 1000) as input, representing the number of test cases. For each test case, it reads an integer n (2 <= n <= 50) and a list of n space-separated integers (0s and 1s) from standard input. The function then counts the number of 1s and 0s in the list and calculates the minimum number of moves required to group all 0s and 1s into separate blocks. If there is only one 1 or no 1s in the list, the function outputs 0. Otherwise, it outputs the number of moves required, which is equal to the number of 0s in the list. The function repeats this process for all test cases and prints the results.

