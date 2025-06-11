#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains three space-separated integers: the number of elements in the array, the limit on the number of elements of the array that Alice can remove, and the limit on the number of elements of the array that Bob can multiply -1 to. The second line contains a space-separated list of integers representing the elements of the array. The number of test cases, the number of elements in the array, the limit on the number of elements of the array that Alice can remove, and the limit on the number of elements of the array that Bob can multiply -1 to are all positive integers. The elements of the array are positive integers.
    """
    Created on Fri Sep  6 21:42:15 2024
     
    @author: dehon
    """
    t = int(input())
    for _ in range(t):
        n, k, x = map(int, input().split())
        
        a = sorted(list(map(int, input().split())), reverse=True)
        
        ans1 = sum(a)
        
        for i in range(x):
            ans1 -= a[i] * 2
        
        ans2 = ans1
        
        for i in range(k):
            ans1 += a[i]
            if i + x < n:
                ans1 -= a[i + x] * 2
            ans2 = max(ans1, ans2)
        
        print(ans2)
        
    #State: The maximum possible sum of the array elements after Alice and Bob have performed their operations for all test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an array of positive integers and two limits for operations that can be performed on the array. For each test case, it calculates the maximum possible sum of the array elements after applying the operations, which involve removing elements and multiplying some elements by -1, within the given limits. The function then prints the maximum possible sum for each test case.

