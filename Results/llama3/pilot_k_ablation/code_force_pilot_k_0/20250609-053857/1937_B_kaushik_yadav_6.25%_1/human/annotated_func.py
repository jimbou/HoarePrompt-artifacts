#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer, then two binary strings of the same length as the integer. The integer is greater or equal to 2 and less or equal to 2 * 10^5. The sum of the integers over all test cases does not exceed 2 * 10^5.
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
            if a[j + 1] == '0' and b[j] == '1':
                counter = 1
        
        print(counter)
        
    #State: The output state contains the results of t test cases. Each test case contains two lines. The first line is a binary string that is the result of the concatenation of the binary strings a and b. The second line is an integer that represents the maximum number of consecutive '1's in the binary string a that are followed by '0's in the binary string b.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer and two binary strings of the same length. It then processes each test case by concatenating the binary strings in a specific order, based on certain conditions, and prints the resulting binary string. Additionally, it counts the maximum number of consecutive '1's in the first binary string that are followed by '0's in the second binary string and prints this count. The function repeats this process for all test cases and outputs the results in a specific format.

