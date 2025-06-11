#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines: the first line contains two space-separated integers n and m (1 <= n <= m <= 2 * 10^5), the second line contains n space-separated integers a_i (1 <= a_i <= 10^9), and the third line contains m space-separated integers b_i (1 <= b_i <= 10^9). The sum of m over all test cases does not exceed 2 * 10^5.
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
            
        #State: t is 0, stdin is empty, a1 is n, a2 is -1, b1 is m, b2 is -1, ans is not defined, n is a positive integer, m is a positive integer, a is a sorted list of n integers, b is a sorted list of m integers, and the sum of the absolute differences between the elements of a and b that are closest to each other for each test case is printed
    #State: The program processes multiple test cases from standard input. For each test case, it reads two positive integers n and m, followed by n and m space-separated integers, respectively. The program then calculates the sum of the absolute differences between the closest elements in the two sorted lists of integers and prints this sum for each test case. If the program is run as the main module, it executes this process; otherwise, it does not perform any actions.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of two positive integers n and m, followed by n and m space-separated integers, respectively. It calculates the sum of the absolute differences between the closest elements in the two sorted lists of integers and prints this sum for each test case. The function iterates through the test cases, sorting the input lists and comparing the differences between the closest elements to determine the sum of absolute differences. The function does not modify the input lists or the standard input stream, but rather processes the test cases and prints the results.

