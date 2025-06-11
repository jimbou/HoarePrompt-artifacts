#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer, then two binary strings of the same length as the integer.
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
        
    #State: The output state after the loop executes all the iterations is the number of test cases (t) is reduced to 0, stdin is empty, and the output contains the concatenated binary strings for each test case and the maximum consecutive count of '1's in the concatenated string.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer and two binary strings of the same length. It then concatenates the binary strings in a specific order, based on the values of the strings, and prints the concatenated string. Additionally, it counts the maximum consecutive occurrences of '1's in the concatenated string and prints this count. The function processes all test cases and produces the concatenated strings and maximum consecutive '1' counts as output.

