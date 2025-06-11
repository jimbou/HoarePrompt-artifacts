#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines. The first line contains two integers n and m (1 ≤ n ≤ m ≤ 2 * 10^5). The second line contains n integers a_i (1 ≤ a_i ≤ 10^9). The third line contains m integers b_i (1 ≤ b_i ≤ 10^9).
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
            
        #State: t is 0, n is an integer between 1 and 2 * 10^5, m is an integer between 1 and 2 * 10^5 and greater than or equal to n, a is a list of n integers, b is a sorted list of m integers between 1 and 10^9, max_heap is an empty list, tp1 is m, tp2 is 0, ans is the sum of the minimum absolute differences between each integer in list a and the integers in list b, diff1 is the absolute difference between the last integer in list a and the first integer in list b, diff2 is the absolute difference between the last integer in list a and the last integer in list b, and the sum of the minimum absolute differences between each integer in list a and the integers in list b which is ans is printed, and stdin contains no test cases.
    #State: The program reads multiple test cases from stdin, each containing two integers n and m, and two lists of integers a and b. If the program is run as the main module, it calculates the sum of the minimum absolute differences between each integer in list a and the integers in list b, and prints this sum. After processing all test cases, stdin contains no test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, each containing two integers n and m, and two lists of integers a and b. It calculates the sum of the minimum absolute differences between each integer in list a and the integers in list b, and prints this sum for each test case. The function processes all test cases and then terminates, leaving the standard input empty.

