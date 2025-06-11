#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 ≤ n ≤ 2*10^5) and then a list of n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ n).
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        a, b = float('inf'), float('inf')
        
        c = 0
        
        for x in range(n):
            if a > b:
                a, b = b, a
            if l[x] <= a:
                a = l[x]
            elif l[x] <= b:
                b = l[x]
            else:
                a = l[x]
                c += 1
        
        print(c)
        
    #State: The number of times the smallest number in the list was replaced by a larger number, for each test case.

#Overall this is what the function does:For each test case, this function determines the number of times the smallest number in a list of integers is replaced by a larger number, and prints this count. It iterates through the list, maintaining the two smallest numbers encountered so far, and increments the count whenever a larger number forces the replacement of the smallest number.

