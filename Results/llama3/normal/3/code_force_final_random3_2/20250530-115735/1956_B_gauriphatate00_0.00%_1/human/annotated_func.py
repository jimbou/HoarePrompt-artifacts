#State of the program right berfore the function call: n is a positive integer, a is a list of integers such that 1 <= a_i <= n for all i, and the length of a is equal to n.
    counter = Counter(a)
    pairs = sum(1 for count in counter.values() if count == 2)
    return min(pairs, n // 2)
    #The program returns the minimum value between the number of elements in list 'a' that appear exactly twice and half of the positive integer 'n'.

#Overall this is what the function does:This function calculates and returns the minimum value between the number of elements in the input list 'a' that appear exactly twice and half of the input positive integer 'n'.

#State of the program right berfore the function call: n is a positive integer, a is a list of integers such that 1 <= a_i <= n for all i, and the length of a is equal to n.
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        
        idx += 1
        
        a = list(map(int, data[idx:idx + n]))
        
        idx += n
        
        results.append(func_1(n, a))
        
    #State: n is an integer equal to the value at data[idx], idx is equal to its original value plus the sum of all n values, a is a list of integers such that 1 <= a_i <= n for all i, and the length of a is equal to n, data is a list of strings, t is 0, results is a list containing the result of func_1(n, a) for each iteration, stdin is empty.
    for result in results:
        print(result)
        
    #State: n is an integer equal to the value at data[idx], idx is equal to its original value plus the sum of all n values, a is a list of integers such that 1 <= a_i <= n for all i, and the length of a is equal to n, data is a list of strings, t is 0, results is a list containing all results of func_1(n, a), stdin is empty, and the last result of func_1(n, a) which is result is being printed.

#Overall this is what the function does:Reads input from standard input, processes it in batches, and prints the results of a function (func_1) applied to each batch. The input is expected to be a series of integers, where the first integer in each batch specifies the size of the batch, and the remaining integers in the batch are processed by func_1. The function reads all input, processes it, and prints all results before terminating.

