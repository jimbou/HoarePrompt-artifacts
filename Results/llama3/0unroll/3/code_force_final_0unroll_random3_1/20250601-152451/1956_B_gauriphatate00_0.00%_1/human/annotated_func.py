#State of the program right berfore the function call: n is a positive integer, a is a list of n integers, each integer in a is between 1 and n (inclusive), and each integer from 1 to n appears in a at most 2 times.
    counter = Counter(a)
    pairs = sum(1 for count in counter.values() if count == 2)
    return min(pairs, n // 2)
    #The program returns the minimum value between the number of integers in list 'a' that appear exactly twice and half of the total number of integers in list 'a'.

#Overall this is what the function does:This function calculates and returns the minimum value between the number of integers in the input list 'a' that appear exactly twice and half of the total number of integers in 'a'. The function accepts a list of integers as input and returns an integer value.

#State of the program right berfore the function call: data is a list of strings where each string is a number, idx is a non-negative integer such that idx < len(data), t is a positive integer, n is a positive integer, and a is a list of positive integers.
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
        
    #State: Output State: data is an empty list, idx is t + 1, t is a positive integer equal to the first number in the original data list, results is a list of t elements where each element is the result of func_1(n, a) for each iteration, and a is a list of positive integers (unchanged).
    for result in results:
        print(result)
        
    #State: Output State: data is an empty list, idx is t + 1, t is a positive integer equal to the first number in the original data list, results is an empty list, and a is a list of positive integers (unchanged).

#Overall this is what the function does:Reads input from standard input, parses it into a list of strings, and then processes the input data in a loop. In each iteration, it extracts a positive integer 'n' and a list of 'n' positive integers 'a' from the input data, passes them to the 'func_1' function, and appends the result to the 'results' list. After processing all input data, it prints each result from the 'results' list. The function does not return any value, and its output is solely through printing the results.

