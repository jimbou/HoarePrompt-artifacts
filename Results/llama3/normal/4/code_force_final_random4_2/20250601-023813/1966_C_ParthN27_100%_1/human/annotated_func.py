#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains a single integer n (1 <= n <= 2*10^5). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). The number of test cases is given in the first line of the input.
    for _ in range(int(input())):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        s = set()
        
        for i in range(n):
            s.add(arr[i])
        
        s = list(s)
        
        s.sort()
        
        s = [0] + s
        
        ans = 1
        
        n = len(s)
        
        if n == 2:
            print('Alice')
        else:
            for i in range(1, n - 1):
                if s[i] - s[i - 1] > 1:
                    break
                else:
                    ans ^= 1
            if ans:
                print('Alice')
            else:
                print('Bob')
        
    #State: n is the number of elements in s plus 1, s is the sorted list of integers from the original set s with a 0 prepended to it, ans is 1, arr is a list of integers, i is undefined, _ is the number of test cases, stdin contains no inputs. If n is 2, 'Alice' is printed. If n is at least 3, 'Alice' is printed if the number of times the loop executes is even, otherwise 'Bob' is printed.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of a list of integers. It removes duplicates from the list, sorts the remaining integers, and then determines the winner of a game based on the number of consecutive integers in the sorted list. If there are only two unique integers, the function prints 'Alice'. Otherwise, it prints 'Alice' if the number of times it iterates through the list is even, and 'Bob' otherwise. The function repeats this process for each test case in the input.

