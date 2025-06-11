#State of the program right berfore the function call: stdin contains one input: an integer (t) (1 <= t <= 10^3) representing the number of test cases. For each test case, stdin contains one input: an integer (n) (2 <= n <= 10^4).
    I = lambda : list(map(int, input().split(' ')))
    R = lambda : int(input())
    for kp in range(int(input())):
        n = int(input())
        
        g = 0
        
        v1 = 0
        
        for i in range(1, n):
            v2 = i
            print(f'? {v1} {v1} {v2} {v2}')
            sys.stdout.flush()
            r = input('')
            if r == '<':
                v1 = v2
        
        prev = 0
        
        for i in range(1, n):
            print(f'? {v1} {i} {v1} {prev}')
            sys.stdout.flush()
            r = input()
            if r == '>':
                prev = i
        
        print(f'! {prev} {v1}')
        
        sys.stdout.flush()
        
    #State: The loop will output the maximum value and its index for each test case. The maximum value is the largest number in the range from 1 to n (inclusive), and its index is the position of this maximum value in the range. The output will be in the format '! index maximum_value' for each test case.

#Overall this is what the function does:The function accepts a number of test cases (t) and for each test case, it accepts an integer (n) representing the number of elements in a range. It then finds the maximum value and its index in the range from 1 to n (inclusive) and outputs the result in the format '! index maximum_value' for each test case.

