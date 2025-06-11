#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines. The first line contains two integers n and m (1 ≤ n ≤ m ≤ 2⋅10^5). The second line contains n integers a_i (1 ≤ a_i ≤ 10^9). The third line contains m integers b_i (1 ≤ b_i ≤ 10^9).
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
            
        #State: t = 0, stdin is empty, and the output contains the sum of the minimum absolute differences for each test case.
    #State: The program has processed all test cases from stdin, and the output contains the sum of the minimum absolute differences for each test case, or the program has not executed the main block if it was not run as the main module.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two integers n and m, followed by n integers a_i and m integers b_i. It then calculates the sum of the minimum absolute differences between each a_i and the closest b_i, either from the start or end of the sorted b_i list, and prints this sum for each test case. The function processes all test cases and empties the standard input, producing output containing the sum of minimum absolute differences for each test case.

