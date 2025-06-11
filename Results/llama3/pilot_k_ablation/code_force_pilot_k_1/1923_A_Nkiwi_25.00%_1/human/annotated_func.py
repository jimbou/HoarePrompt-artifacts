#State of the program right berfore the function call: stdin contains t+2t lines. The first line contains one integer t (1 ≤ t ≤ 1000). Each of the following t pairs of lines contains an integer n (2 ≤ n ≤ 50) and a list of n space-separated integers (0 ≤ a_i ≤ 1).
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
        
    #State: `t` is an integer between 1 and 1000, `stdin` is empty, `length`, `arrs`, `cnt0`, `cnt1`, and `ans` are no longer defined as they are local variables within the loop, `_` is `t-1`.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the minimum number of zeros required to separate blocks of ones and zeros in a given list of binary numbers. It takes no arguments and returns no value, instead printing the result directly. The function iterates over multiple test cases, each consisting of a list of binary numbers, and for each test case, it calculates and prints the minimum number of zeros required to separate the blocks.

