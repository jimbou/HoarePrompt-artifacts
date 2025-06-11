#State of the program right berfore the function call: stdin contains two inputs: two space-separated integers n and k, where k is even and 2 <= k <= n <= 2 * 10^5.
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
        
    #State: n is an integer between k and 2 * 10^5, k is an even integer greater than 0, permutation is a list of n integers where permutation[multiples_of_k_plus_i] is n // k + 1 + (multiples_of_k_plus_i - 1) // k, idx is 0, idx_v is 1, curr_v is n // k + 1 + (n - 1 - k) // k + (n - 2) // k + ... + (n - (k - 1)) // k, multiples_of_k_plus_i is n, i is k - 1, stdin is empty, n is greater than 1 + (n - 1 - k) // k * k + (n - 2) // k * k + ... + (n - (k - 1)) // k * k.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: a string of space-separated integers representing the permutation (where permutation is a list of n integers where permutation[multiples_of_k_plus_i] is n // k + 1 + (multiples_of_k_plus_i - 1) // k)

#Overall this is what the function does:The function generates a permutation of integers from 1 to n, where n is an input integer, and prints the permutation as a string of space-separated integers. The permutation is constructed by assigning values to multiples of k plus i, where k is an even input integer and i ranges from 0 to k-1. The function takes two space-separated integers n and k as input from stdin, where k is even and 2 <= k <= n <= 2 * 10^5. The function does not return any value, but prints the resulting permutation as a string.

#State of the program right berfore the function call: stdin contains one input: an integer (greater than 0).
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: t is an integer less than or equal to 0, stdin contains no input.

#Overall this is what the function does:Reads an integer from standard input and executes the function func_1() that many times, until the input integer reaches 0 or less, at which point the function concludes.

