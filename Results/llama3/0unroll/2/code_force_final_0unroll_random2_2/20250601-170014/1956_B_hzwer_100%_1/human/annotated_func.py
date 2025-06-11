#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (n) and then a space-separated list of n integers. The integer (n) is a positive integer and less or equal than 2 * 10^5. The list of integers contains integers from 1 to n, and each integer from 1 through n appears in the sequence at most 2 times.
    input = sys.stdin.readline
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        cnt = [0] * (n + 1)
        
        for x in a:
            cnt[x] += 1
        
        ans = 0
        
        for x in cnt:
            ans += max(0, x - 1)
        
        print(ans)
        
    #State: The number of pairs of identical integers in each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer (n) and a list of n integers. It then counts the occurrences of each integer in the list and calculates the number of pairs of identical integers by summing the maximum of 0 and the count minus 1 for each integer. Finally, it prints the total number of pairs for each test case.

