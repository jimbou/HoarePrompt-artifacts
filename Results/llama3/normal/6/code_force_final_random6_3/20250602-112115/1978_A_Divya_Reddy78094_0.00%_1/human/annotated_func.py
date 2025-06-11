#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (the number of books Alice has) and then a list of integers (the number of pages in each book). The number of books is between 2 and 100 inclusive. The number of pages in each book is between 1 and 10^9 inclusive.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        nums.sort(reverse=True)
        
        print(nums[0] + nums[1])
        
    #State: _ is t-1, t is an integer between 2 and 100 inclusive and is greater than or equal to 0, n is an integer, nums is a list of integers sorted in descending order, and the sum of the first two elements of the list nums which are the largest two numbers in the list is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer (number of books) and a list of integers (number of pages in each book). It sorts the list of pages in descending order and prints the sum of the two largest numbers (i.e., the number of pages in the two largest books). The function processes all test cases and outputs the results for each case.

