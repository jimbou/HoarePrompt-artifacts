#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (the number of elements in the list) and then a list of integers. The integer is a positive integer and greater or equal to 2. The integers in the list are positive integers and less or equal to 10^9.
    for _ in range(int(input())):
        n = int(input())
        
        ar = map(str, sorted(list(map(int, input().split()))))
        
        print(' '.join(ar))
        
    #State: n is an integer, ar is a map object containing a sorted list of strings representing integers, stdin is empty, and a string of space-separated integers is printed, where the integers are the sorted values from the map object ar.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer (n) and a list of positive integers. It sorts the list of integers in ascending order, converts them to strings, and prints the sorted list as a string of space-separated integers. The function repeats this process until all test cases have been read from standard input, leaving the input stream empty.

