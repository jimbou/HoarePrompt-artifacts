#State of the program right berfore the function call: stdin contains t+2t lines, where t is a positive integer. The first line contains one positive integer t. Each of the following t blocks of two lines contains one positive integer n and then n non-negative integers, respectively.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        num_of_lens = {}
        
        nums = list(map(int, input().split()))
        
        for x in nums:
            num_of_lens[x] = num_of_lens.get(x, 0) + 1
        
        res = 0
        
        for cnt in num_of_lens.values():
            if cnt >= 3:
                res += math.comb(cnt, 3)
            if cnt >= 2:
                total_sum = sum(i for i in num_of_lens.values() if i != cnt)
                res += math.comb(cnt, 2) * total_sum
        
        print(res)
        
    #State: The output state is a list of `t` integers, where each integer represents the number of triplets that can be formed from the corresponding block of `n` non-negative integers.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the number of triplets that can be formed from each block of non-negative integers. It accepts no parameters and returns no value, instead printing the results directly. The function takes in a series of blocks, where each block consists of a positive integer n followed by n non-negative integers. It calculates the number of triplets that can be formed from each block by considering all possible combinations of three numbers, including duplicates, and prints the result for each block. The final state of the program is the output of the calculated triplet counts for each block, printed to stdout.

