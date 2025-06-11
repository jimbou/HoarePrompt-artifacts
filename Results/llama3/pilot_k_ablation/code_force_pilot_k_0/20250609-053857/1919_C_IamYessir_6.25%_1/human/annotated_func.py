#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 ≤ n ≤ 2⋅10^5) and then a list of n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ n).
    for _ in range(int(input())):
        n = int(input())
        
        lit = list(map(int, input().split()))
        
        a, b = [lit[0]], []
        
        cp = 0
        
        for i in range(1, n):
            if a[-1] < lit[i]:
                b.append(lit[i])
            else:
                a.append(lit[i])
        
        s = 0
        
        for i in range(1, len(a)):
            if a[i] > a[i - 1]:
                s += 1
        
        for i in range(1, len(b)):
            if b[i] > b[i - 1]:
                s += 1
        
        print(s)
        
    #State: The output state will be the total number of times an element in the list is greater than its previous element, considering only the elements that are in increasing order. This will be printed for each test case.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of an integer n followed by a list of n integers. It separates the list into two lists, 'a' and 'b', based on whether each element is greater than the previous element in 'a'. Then, it counts the number of times an element in both lists is greater than its previous element, considering only the elements in increasing order. Finally, it prints the total count for each test case.

