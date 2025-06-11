#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines. The first line contains two integers n and m (1 ≤ n ≤ m ≤ 2 × 10^5). The second line contains n integers a_i (1 ≤ a_i ≤ 10^9). The third line contains m integers b_i (1 ≤ b_i ≤ 10^9).
    if (__name__ == '__main__') :
        t = int(input())
        while t > 0:
            t -= 1
            
            n, m = map(int, input().split())
            
            a = list(map(int, input().split()))
            
            b = list(map(int, input().split()))
            
            b.sort()
            
            max_heap = []
            
            tp1 = 0
            
            tp2 = m - 1
            
            ans = 0
            
            for i in a:
                diff1 = abs(i - b[0])
                diff2 = abs(i - b[m - 1])
                if diff1 > diff2:
                    heapq.heappush(max_heap, (-diff1, i, 0))
                else:
                    heapq.heappush(max_heap, (-diff2, i, m - 1))
            
            while max_heap:
                item = heapq.heappop(max_heap)
                if item[2] < tp1 or item[2] > tp2:
                    diff1 = abs(item[1] - b[tp1])
                    diff2 = abs(item[1] - b[tp2])
                    if diff1 > diff2:
                        tp1 += 1
                        ans += diff1
                    else:
                        tp2 -= 1
                        ans += diff2
                else:
                    ans += -item[0]
                    if item[2] == tp1:
                        tp1 += 1
                    else:
                        tp2 -= 1
            
            print(ans)
            
        #State: The program has finished executing all test cases and has printed the minimum sum of absolute differences for each test case. The values of `t`, `n`, `m`, `a`, `b`, `max_heap`, `tp1`, `tp2`, and `ans` have been updated accordingly after each iteration.
    #State: *The program has finished executing all test cases and has printed the minimum sum of absolute differences for each test case. The values of `t`, `n`, `m`, `a`, `b`, `max_heap`, `tp1`, `tp2`, and `ans` have been updated accordingly after each iteration.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two integers n and m, followed by n integers a_i and m integers b_i. It then calculates and prints the minimum sum of absolute differences between each a_i and the closest b_i, considering the constraints that the closest b_i for each a_i can be either the smallest or largest b_i. The function iterates through all test cases, updating the values of variables accordingly, and finally prints the minimum sum of absolute differences for each test case.

