#State of the program right berfore the function call: stdin contains one input: two space-separated integers n and k, where k is even and 2 <= k <= n <= 2 * 10^5.
    n, k = map(int, input().split(' '))
    permutation = [0] * n
    bottom_v = 1
    top_v = n
    idx = 0
    while idx < k:
        multiples_of_k_plus_idx = idx
        
        while multiples_of_k_plus_idx < len(permutation):
            if idx % 2 == 0:
                permutation[multiples_of_k_plus_idx] = bottom_v
                bottom_v += 1
            else:
                permutation[multiples_of_k_plus_idx] = top_v
                top_v -= 1
            multiples_of_k_plus_idx += k
        
        idx += 1
        
    #State: idx is equal to k, permutation is a list of n integers, the length of permutation is greater than or equal to the final value of multiples_of_k_plus_idx, stdin is empty, k is greater than or equal to the final value of idx, and multiples_of_k_plus_idx is equal to the final value of idx + (number of iterations of the loop) * k. If idx is even, the value at index multiples_of_k_plus_idx in permutation is bottom_v and bottom_v is incremented by the number of iterations of the loop. If idx is odd, the value at index multiples_of_k_plus_idx in permutation is top_v - (number of iterations of the loop) and top_v is decreased by the number of iterations of the loop.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: A space-separated list of n integers, where each integer is either bottom_v + i (if idx is even) or top_v - i (if idx is odd), for i ranging from 0 to n-1

#Overall this is what the function does:This function generates a permutation of n integers based on the input parameters n and k, where k is even and 2 <= k <= n <= 2 * 10^5. It constructs the permutation by iterating k times, assigning values to the permutation list in a specific pattern. The pattern alternates between assigning values from the bottom (starting from 1) and top (starting from n) of the range, incrementing or decrementing the values accordingly. The function then prints the resulting permutation as a space-separated list of n integers.

#State of the program right berfore the function call: stdin contains one input: an integer (greater than 0).
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: t is 0, stdin contains no input.

#Overall this is what the function does:This function reads an integer from standard input, repeatedly calls another function (`func_1`) a number of times equal to the input integer, and then terminates when the input integer reaches 0, leaving the standard input empty.

