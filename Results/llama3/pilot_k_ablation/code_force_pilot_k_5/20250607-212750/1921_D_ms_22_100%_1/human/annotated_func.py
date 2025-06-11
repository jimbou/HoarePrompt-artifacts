#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines. The first line contains two integers n and m (1 <= n <= m <= 2 * 10^5). The second line contains n integers a_i (1 <= a_i <= 10^9). The third line contains m integers b_i (1 <= b_i <= 10^9).
    if (__name__ == '__main__') :
        t = int(input())
        while t > 0:
            t -= 1
            
            n, m = map(int, input().split())
            
            a = list(map(int, input().split()))
            
            b = list(map(int, input().split()))
            
            a1 = 0
            
            a2 = n - 1
            
            b1 = 0
            
            b2 = m - 1
            
            ans = 0
            
            b.sort()
            
            a.sort()
            
            while a1 <= a2:
                dif1 = abs(a[a1] - b[b1])
                dif2 = abs(a[a1] - b[b2])
                dif3 = abs(a[a2] - b[b1])
                dif4 = abs(a[a2] - b[b2])
                if dif1 > dif2:
                    if dif3 > dif4:
                        if dif3 > dif1:
                            ans += dif3
                            a2 -= 1
                            b1 += 1
                        else:
                            ans += dif1
                            a1 += 1
                            b1 += 1
                    elif dif4 > dif1:
                        ans += dif4
                        a2 -= 1
                        b2 -= 1
                    else:
                        ans += dif1
                        a1 += 1
                        b1 += 1
                elif dif3 > dif4:
                    if dif3 > dif2:
                        ans += dif3
                        a2 -= 1
                        b1 += 1
                    else:
                        ans += dif2
                        a1 += 1
                        b2 -= 1
                elif dif4 > dif2:
                    ans += dif4
                    a2 -= 1
                    b2 -= 1
                else:
                    ans += dif2
                    a1 += 1
                    b2 -= 1
            
            print(ans)
            
        #State: t is 0, n and m are integers where 1 <= n <= m <= 2 * 10^5, a is a sorted list of n integers where 1 <= a_i <= 10^9, b is a sorted list of m integers where 1 <= b_i <= 10^9, stdin contains no test cases, a1 is equal to a2, ans is the sum of the maximum of the absolute differences between a[a1] and b[b1], a[a1] and b[b2], a[a2] and b[b1], a[a2] and b[b2] for all iterations of the loop, and the sum of the maximum of the absolute differences between a[a1] and b[b1], a[a1] and b[b2], a[a2] and b[b1], a[a2] and b[b2] for all iterations of the loop is printed.
    #State: *stdin contains multiple test cases. Each test case contains three lines. The first line contains two integers n and m (1 <= n <= m <= 2 * 10^5). The second line contains n integers a_i (1 <= a_i <= 10^9). The third line contains m integers b_i (1 <= b_i <= 10^9). If the program is run as the main module, then t is 0, n and m are integers where 1 <= n <= m <= 2 * 10^5, a is a sorted list of n integers where 1 <= a_i <= 10^9, b is a sorted list of m integers where 1 <= b_i <= 10^9, stdin contains no test cases, a1 is equal to a2, ans is the sum of the maximum of the absolute differences between a[a1] and b[b1], a[a1] and b[b2], a[a2] and b[b1], a[a2] and b[b2] for all iterations of the loop, and the sum of the maximum of the absolute differences between a[a1] and b[b1], a[a1] and b[b2], a[a2] and b[b1], a[a2] and b[b2] for all iterations of the loop is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: two integers n and m, followed by n integers a_i and m integers b_i. It then calculates the sum of the maximum absolute differences between corresponding elements in the sorted lists a and b, and prints this sum for each test case. The function continues to process test cases until all input has been read.

