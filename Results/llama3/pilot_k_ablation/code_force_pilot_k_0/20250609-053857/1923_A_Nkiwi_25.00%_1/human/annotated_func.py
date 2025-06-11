#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (2 <= n <= 50) followed by n integers a_1, a_2, ..., a_n (0 <= a_i <= 1).
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
        
    #State: The output state is a list of integers, where each integer represents the number of zeros in the corresponding test case that are not adjacent to the first element or the last element, or the number of zeros in the test case if the first element is 1. The list has a length of t, where t is the number of test cases.

#Overall this is what the function does:This function takes a series of test cases as input, where each test case consists of a list of binary digits (0s and 1s). It then calculates and prints the minimum number of zeros that need to be moved to create a contiguous block of zeros and ones, or the number of zeros in the test case if the first element is 1. The function processes multiple test cases and outputs the result for each case.

