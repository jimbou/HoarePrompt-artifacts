#State of the program right berfore the function call: n is a positive integer, a is a list of integers such that 1 <= a_i <= n and each integer from 1 through n appears in the sequence a at most 2 times.
    counter = Counter(a)
    pairs = sum(1 for count in counter.values() if count == 2)
    return min(pairs, n // 2)
    #The program returns the minimum value between the number of integers that appear exactly twice in list 'a' and half of the positive integer 'n'.

#Overall this is what the function does:This function calculates and returns the minimum value between the number of integers that appear exactly twice in a given list and half of a given positive integer.

#State of the program right berfore the function call: n is a positive integer and a is a list of n integers, each integer in a is between 1 and n (inclusive) and each integer appears at most twice in a.
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
        
    #State: Output State: idx is t * n + 1, results is a list of t elements, each element is the output of func_1(n, a) for the corresponding iteration, n is the last value it was assigned in the loop, a is the last list it was assigned in the loop, data, t are unchanged.
    for result in results:
        print(result)
        
    #State: Output State: idx is t * n + 1, results is a list of t elements, each element is the output of func_1(n, a) for the corresponding iteration, n is the last value it was assigned in the loop, a is the last list it was assigned in the loop, data, t are unchanged.

#Overall this is what the function does:The function reads input from standard input, processes it, and prints the results. It expects the input to be in a specific format, where the first line contains a positive integer t, followed by t lines, each containing a positive integer n and a list of n integers between 1 and n (inclusive), with each integer appearing at most twice in the list. The function then calls another function, func_1, with the input n and list a, and appends the result to a list of results. Finally, it prints each result in the list. The function does not modify the input data or any external state, and its output is solely based on the input provided.

