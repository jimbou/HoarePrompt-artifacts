#State of the program right berfore the function call: stdin contains two inputs: two space-separated integers n and k, where n and k are positive integers and k is even and k <= n.
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
        
    #State: permutation is a list of n values where permutation[multiples_of_k_plus_idx] is either bottom_v or top_v depending on the parity of idx, bottom_v is n/2 + (multiples_of_k_plus_idx/k) if n is even, otherwise it is (n+1)/2 + (multiples_of_k_plus_idx/k), top_v is n/2 - (multiples_of_k_plus_idx/k) if n is even, otherwise it is (n-1)/2 - (multiples_of_k_plus_idx/k), idx is k, k is greater than idx, and n is greater than idx + (n - idx - 1) // k * k.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: a string containing the elements of permutation separated by spaces, where permutation is a list of n values, with permutation[multiples_of_k_plus_idx] being either bottom_v or top_v depending on the parity of idx, and bottom_v and top_v being calculated based on the given formulas and the values of n, k, and idx

#Overall this is what the function does:This function generates a permutation of numbers from 1 to n, where n is a positive integer, and prints the permutation as a string of space-separated values. The permutation is constructed by iterating through the numbers in a specific pattern, where every k-th number is assigned a value from either the bottom or top half of the range, depending on the parity of the index. The function takes two inputs, n and k, from the standard input, where k is a positive even integer less than or equal to n. The function does not return any value but prints the resulting permutation as a string.

#State of the program right berfore the function call: stdin contains one input: an integer (greater than 0).
    t = int(input())
    while t > 0:
        func_1()
        
        t -= 1
        
    #State: t is an integer greater than or equal to 0, stdin contains no input

#Overall this is what the function does:Repeats a function call (func_1) a specified number of times based on user input, consuming all input from stdin and leaving no input remaining.

