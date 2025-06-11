#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer n (2 <= n <= 2 * 10^5), then two binary strings a_11 a_12 ... a_1n and a_21 a_22 ... a_2n (a_1i and a_2i are either 0 or 1). The number of test cases t (1 <= t <= 10^4) is given before the test cases.
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = input().strip()
        
        b = input().strip()
        
        ans = ''
        
        i = 0
        
        work = True
        
        while i < len(a):
            if work:
                ans += a[i]
                if i + 1 < len(a) and b[i] < a[i + 1]:
                    work = False
                elif i + 1 == len(a):
                    ans += b[i]
                    break
                else:
                    i += 1
            else:
                ans += b[i]
                i += 1
        
        print(ans)
        
        counter = 1
        
        for j in range(len(a) - 1):
            if a[j + 1] == b[j]:
                counter += 1
            elif a[j + 1] == '0' and b[j] == '1':
                counter = 1
            else:
                break
        
        print(counter)
        
    #State: The output state is a series of strings and integers, where each string represents the merged binary string from the two input strings a and b, and each integer represents the maximum number of consecutive positions where a[j + 1] equals b[j]. The number of strings and integers in the output state is equal to the number of test cases t. The state of the variable t remains unchanged.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and two binary strings a and b. It merges the two binary strings into a single string, prioritizing string a unless a condition is met, and then prints the merged string. Additionally, it calculates and prints the maximum number of consecutive positions where a[j + 1] equals b[j]. The function processes all test cases and outputs the merged strings and maximum consecutive positions for each case.

