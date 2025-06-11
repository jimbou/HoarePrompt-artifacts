#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines: the first line contains two space-separated integers n and m (1 <= n <= m <= 2 * 10^5), the second line contains n space-separated integers a_i (1 <= a_i <= 10^9), and the third line contains m space-separated integers b_i (1 <= b_i <= 10^9). The number of test cases is given by a single integer t (1 <= t <= 100) on the first line of the input.
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
            
        #State: t is 0, n is an integer, m is an integer, a is not empty, b is a sorted list of integers, stdin contains 0 inputs, i is the last element in the list a, max_heap is empty, tp1 is m, tp2 is 0, and ans is the sum of the absolute differences between the elements of a and the elements of b that are closest to them.
    #State: *stdin contains multiple test cases. Each test case contains three lines: the first line contains two space-separated integers n and m (1 <= n <= m <= 2 * 10^5), the second line contains n space-separated integers a_i (1 <= a_i <= 10^9), and the third line contains m space-separated integers b_i (1 <= b_i <= 10^9). The number of test cases is given by a single integer t (1 <= t <= 100) on the first line of the input. If t is 0, n is an integer, m is an integer, a is not empty, b is a sorted list of integers, stdin contains 0 inputs, i is the last element in the list a, max_heap is empty, tp1 is m, tp2 is 0, and ans is the sum of the absolute differences between the elements of a and the elements of b that are closest to them.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: two space-separated integers n and m, followed by n space-separated integers a_i, and then m space-separated integers b_i. It calculates the sum of the absolute differences between each element in a_i and the closest element in b_i, and prints this sum for each test case. The function continues to process test cases until the input is exhausted.

