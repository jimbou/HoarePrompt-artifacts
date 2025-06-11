#State of the program right berfore the function call: test_cases is a list of lists of integers, where the first element of each sublist is an integer (1 ≤ n ≤ 3*10^5) and the second element is a list of n integers (0 ≤ a_i ≤ n).
    results = []
    for _ in range(test_cases):
        n = int(input())
        
        num_list = list(map(int, input().split()))
        
        num_of_lens = {}
        
        for x in num_list:
            if x in num_of_lens:
                num_of_lens[x] += 1
            else:
                num_of_lens[x] = 1
        
        res = 0
        
        total_count = 0
        
        for cnt in num_of_lens.values():
            if cnt >= 3:
                res += cnt * (cnt - 1) * (cnt - 2) // 6
            if cnt >= 2:
                res += cnt * (cnt - 1) // 2 * total_count
            total_count += cnt
        
        results.append(res)
        
    #State: `test_cases` is an empty list, `results` is a list containing the sum of the products of each value in `num_of_lens` and the sum of the products of each value in `num_of_lens` minus 1 and the sum of the products of each value in `num_of_lens` minus 2 divided by 6 for each iteration of the loop, `n` is an integer, `num_list` is a list that must have at least 2 elements, `x` is not defined, `num_of_lens` is a dictionary that contains all elements in `num_list` as keys and their values are the number of times each element appears in `num_list` and has at least 2 values, `total_count` is the sum of all values in `num_of_lens`, `res` is the sum of the products of each value in `num_of_lens` and the sum of the products of each value in `num_of_lens` minus 1 and the sum of the products of each value in `num_of_lens` minus 2 divided by 6, and `stdin` contains no input.
    for result in results:
        print(result)
        
    #State: The loop has finished executing, and all elements in the `results` list have been printed. The `result` variable is no longer defined, and the loop has terminated.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a list of n integers. It then calculates the sum of the products of each value in the list and the sum of the products of each value minus 1 and the sum of the products of each value minus 2 divided by 6. The results are stored in a list and printed out one by one. The function does not return any value, but rather prints the results directly to the console.

