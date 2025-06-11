#State of the program right berfore the function call: n is a positive integer and a is a list of integers such that 1 <= a[i] <= n for all i and each integer from 1 to n appears in the list a at most 2 times.
    counter = Counter(a)
    pairs = sum(1 for count in counter.values() if count == 2)
    return min(pairs, n // 2)
    #The program returns the minimum value between the number of elements in list 'a' that appear exactly twice and half of the positive integer 'n'.

#Overall this is what the function does:This function calculates and returns the minimum value between the number of pairs of identical elements in a given list and half of a given positive integer. It takes a list of integers and a positive integer as input, where each integer in the list appears at most twice, and returns an integer representing the minimum value between these two quantities.

#State of the program right berfore the function call: n is a positive integer, a is a list of integers, and 1 <= a_i <= n for all i, and the length of a is n.
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
        
    #State: n is an integer equal to the value at data[idx+t-1], a is a list of n integers from data[idx+t:idx+t+n-1], idx is t*n positions ahead of its original value, results is a list containing t elements: the original result of func_1(n, a), the new result of func_1(n, a), and so on, stdin is empty, _ is t-1
    for result in results:
        print(result)
        
    #State: `n` is an integer equal to the value at data[idx+t-1], `a` is a list of n integers from data[idx+t:idx+t+n-1], `idx` is t*n positions ahead of its original value, `results` is a list containing t results, `result` is the last result in the list, `stdin` is empty, `_` is t-1, and the last result in the list which is `result` is being printed.

#Overall this is what the function does:Reads input from standard input, processes it into a list of integers, and then calls another function `func_1` with the processed input, storing the results in a list. The function then prints each result in the list.

