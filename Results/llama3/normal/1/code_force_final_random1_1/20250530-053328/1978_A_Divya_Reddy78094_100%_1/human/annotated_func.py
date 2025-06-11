#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t test cases. Each test case consists of an integer n (2 <= n <= 100) followed by n space-separated integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        print(max(nums[:-1]) + nums[-1])
        
    #State: t is an integer between 1 and 500 (inclusive) and greater than or equal to the number of iterations, _ is t-1, n is an integer, nums is a list of integers, and the sum of the maximum of all elements in the list nums except the last one and the last element in the list nums has been printed t times

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output. It accepts no parameters and returns no value. It reads an integer t, then for each test case (t times), it reads an integer n and a list of n space-separated integers. For each test case, it prints the sum of the maximum of all elements in the list except the last one and the last element. The function modifies the state of the program by consuming input from stdin and producing output. The final state of the program is that the input has been processed, and the results have been printed t times.

