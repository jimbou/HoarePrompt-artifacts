#State of the program right berfore the function call: stdin contains one input: two space-separated integers n and k, where k is even and 2 <= k <= n <= 2 * 10^5.
    n, k = map(int, input().split(' '))
    permutation = [0] * n
    idx = 0
    idx_v = 1
    curr_v = 1
    for i in range(k):
        multiples_of_k_plus_i = i
        
        while multiples_of_k_plus_i < len(permutation):
            permutation[multiples_of_k_plus_i] = curr_v
            curr_v += 1
            multiples_of_k_plus_i += k
        
    #State: The permutation array is filled with values from 1 to k in a cyclic manner, starting from index 0 and incrementing by k each time. The value of curr_v is k + 1. All other variables remain unchanged.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: 1 2 3 ... k (where k is the value of k and the elements are separated by spaces)

#Overall this is what the function does:Generates a permutation of numbers from 1 to n, where the first k numbers are arranged in a cyclic manner, and prints the resulting permutation as a space-separated string. The function takes two space-separated integers n and k as input from stdin, where k is even and 2 <= k <= n <= 2 * 10^5, and does not return any value.

#State of the program right berfore the function call: stdin contains one input: an integer (greater than 0).
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: t is 0, stdin contains no input

#Overall this is what the function does:Repeats a function call (func_1) a specified number of times based on user input, until no more input is available.

