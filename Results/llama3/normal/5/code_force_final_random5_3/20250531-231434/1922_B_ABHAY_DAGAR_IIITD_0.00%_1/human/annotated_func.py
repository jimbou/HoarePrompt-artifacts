#State of the program right berfore the function call: test_cases is a list of test cases. Each test case is a list of two elements: the first element is an integer n (1 <= n <= 3 * 10^5), and the second element is a list of n integers a_1, a_2, ..., a_n (0 <= a_i <= n).
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
        
    #State: `test_cases` is an empty list, `results` is a list containing the sum of `cnt * (cnt - 1) * (cnt - 2) // 6` for all `cnt` in `num_of_lens` where `cnt >= 3`, plus the sum of `cnt * (cnt - 1) // 2 * total_count` for all `cnt` in `num_of_lens` where `cnt >= 2`, for each test case in the original `test_cases`, `n` is an integer equal to the input value, `num_list` is an empty list, `x` is undefined, `num_of_lens` is a dictionary where each key is an integer from the original `num_list` and each value is the count of that integer in the original `num_list`, `cnt` is the last value in `num_of_lens`, `res` is the sum of `cnt * (cnt - 1) * (cnt - 2) // 6` for all `cnt` in `num_of_lens` where `cnt >= 3`, plus the sum of `cnt * (cnt - 1) // 2 * total_count` for all `cnt` in `num_of_lens` where `cnt >= 2`, and `total_count` is the sum of all `cnt` in `num_of_lens`.
    for result in results:
        print(result)
        
    #State: `test_cases` is an empty list, `results` is an empty list, `n` is an integer equal to the input value, `num_list` is an empty list, `x` is undefined, `num_of_lens` is a dictionary where each key is an integer from the original `num_list` and each value is the count of that integer in the original `num_list`, `cnt` is the last value in `num_of_lens`, `res` is the sum of `cnt * (cnt - 1) * (cnt - 2) // 6` for all `cnt` in `num_of_lens` where `cnt >= 3`, plus the sum of `cnt * (cnt - 1) // 2 * total_count` for all `cnt` in `num_of_lens` where `cnt >= 2`, and `total_count` is the sum of all `cnt` in `num_of_lens`.

#Overall this is what the function does:This function takes a list of test cases as input, where each test case consists of an integer n and a list of n integers. It calculates the sum of combinations of triplets and pairs of identical integers in each test case, and prints the results. The function does not return any value, but instead prints the calculated sums for each test case.

