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
            
        #State: t = 0, n = 0, m = 0, a = [], b = [], max_heap = [], tp1 = 0, tp2 = -1, ans = 0
    #State: *The program processes multiple test cases from stdin, where each test case contains two integers n and m, followed by n integers a_i and m integers b_i. If the program is run as the main module, it initializes variables t, n, m, a, b, max_heap, tp1, tp2, and ans to 0, 0, 0, empty lists, empty lists, empty lists, 0, -1, and 0, respectively. Otherwise, no action is taken.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case contains two integers n and m, followed by n integers a_i and m integers b_i. It calculates the minimum sum of absolute differences between each a_i and its closest element in the sorted array b_i, considering the constraints that the closest element must be within the range [tp1, tp2] and updates the range boundaries tp1 and tp2 accordingly. The function prints the minimum sum of absolute differences for each test case.

