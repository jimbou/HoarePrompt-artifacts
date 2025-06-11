#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 3 * 10^5) followed by a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= n) that form a beautiful array.
    for _ in range(int(input())):
        n = int(input())
        
        ar = list(map(int, input().split()))
        
        same = 1
        
        num = ar[0]
        
        minn = inf
        
        i = 1
        
        while i < len(ar):
            if ar[i] == num:
                same += 1
            else:
                i += 1
                num = ar[i]
                minn = min(minn, same)
                same = 1
            i += 1
        
        minn = min(minn, same)
        
        if minn == inf or minn == len(ar):
            print(-1)
        else:
            print(minn)
        
    #State: `n` is an integer, `ar` is a list of integers, `same` is 1, `num` is the last integer in `ar`, `i` is equal to the length of `ar`, and `minn` is the minimum of its previous value and 1, and stdin is empty. If `minn` is either infinity or equal to the length of `ar`, then -1 is printed. Otherwise, `minn` is neither infinite nor equal to the length of `ar`, and the value of `minn` which is 1 is printed.

#Overall this is what the function does:This function reads input from stdin, processes a series of test cases, and prints the minimum length of a subarray that contains all unique elements in a given array. For each test case, it reads an integer n followed by a list of n integers, and then finds the minimum length of a subarray with all unique elements. If no such subarray exists or the entire array has unique elements, it prints -1. Otherwise, it prints the minimum length of the subarray.

