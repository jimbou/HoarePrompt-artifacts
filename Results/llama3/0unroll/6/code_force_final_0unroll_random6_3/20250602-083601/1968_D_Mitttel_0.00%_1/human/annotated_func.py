#State of the program right berfore the function call: n is a positive integer, k is a positive integer, PB and PS are positive integers such that 1 <= PB <= n and 1 <= PS <= n, p is a list of n positive integers such that 1 <= p[i] <= n for all i, and a is a list of n positive integers.
    bodya_score = calculate_score(PB)
    sasha_score = calculate_score(PS)
    if (bodya_score > sasha_score) :
        return 'Bodya'
        #The program returns the string 'Bodya'.
    else :
        if (sasha_score > bodya_score) :
            return 'Sasha'
            #The program returns the string 'Sasha'.
        else :
            return 'Draw'
            #The program returns the string 'Draw'

#Overall this is what the function does:Determines the winner of a game between 'Bodya' and 'Sasha' based on their scores, which are calculated by the 'calculate_score' function. The function takes no parameters and returns a string indicating the winner ('Bodya' or 'Sasha') or a 'Draw' if their scores are equal.

#State of the program right berfore the function call: start_pos is a positive integer, k is a positive integer, p is a list of positive integers representing a permutation, and a is a list of non-negative integers. The length of p and a is equal to the maximum value in p (or a), and start_pos is less than or equal to the length of p (or a).
    score = 0
    current_pos = start_pos
    steps = 0
    visited = {}
    cycle_start = -1
    while steps < k:
        if current_pos in visited:
            cycle_start = visited[current_pos]
            break
        
        visited[current_pos] = steps
        
        score += a[current_pos - 1]
        
        steps += 1
        
        if steps >= k:
            return score
        
        current_pos = p[current_pos - 1]
        
    #State: score is the sum of the first k elements of a, current_pos is the kth element of p, steps is k, visited is a dictionary with keys from 1 to k and values from 0 to k-1, cycle_start is -1, start_pos is unchanged, k is unchanged, p is unchanged, and a is unchanged.
    if (cycle_start != -1) :
        cycle_length = steps - cycle_start
        cycle_score = 0
        cycle_pos = current_pos
        for _ in range(cycle_length):
            cycle_score += a[cycle_pos - 1]
            
            cycle_pos = p[cycle_pos - 1]
            
        #State: Output State: score is the sum of the first k elements of a, current_pos is the kth element of p, steps is k, visited is a dictionary with keys from 1 to k and values from 0 to k-1, start_pos is unchanged, k is unchanged, p is unchanged, a is unchanged, cycle_start is unchanged, cycle_length is steps - cycle_start, cycle_score is the sum of the elements of a at the positions specified by the cycle, cycle_pos is the position after the last element of the cycle.
        remaining_steps = k - steps
        full_cycles = remaining_steps // cycle_length
        remainder_steps = remaining_steps % cycle_length
        score += full_cycles * cycle_score
        for _ in range(remainder_steps):
            score += a[current_pos - 1]
            
            current_pos = p[current_pos - 1]
            
        #State: Output State: The score is increased by the sum of the elements of a at the positions specified by the remaining steps, the current position is updated to the position after the last element of the remaining steps, and the remaining steps are reduced to 0.
    #State: *The score is the sum of the first k elements of a, current_pos is the kth element of p, steps is k, visited is a dictionary with keys from 1 to k and values from 0 to k-1, cycle_start is -1, start_pos is unchanged, k is unchanged, p is unchanged, and a is unchanged. If cycle_start is not -1, the score is increased by the sum of the elements of a at the positions specified by the remaining steps, the current position is updated to the position after the last element of the remaining steps, and the remaining steps are reduced to 0.
    return score
    #The program returns the score, which is the sum of the first k elements of list a, plus the sum of the elements of a at the positions specified by the remaining steps if a cycle is detected, and the current position is updated to the position after the last element of the remaining steps.

#Overall this is what the function does:Calculates the score by traversing a permutation (p) and accumulating values from a list (a) for a specified number of steps (k), handling cycles in the permutation by adding the score of the cycle and remaining steps.

#State of the program right berfore the function call: data is a list of strings where each string represents an integer or a space-separated list of integers, index is a non-negative integer such that index < len(data), t is a non-negative integer, n is a non-negative integer, k is a non-negative integer, PB and PS are non-negative integers such that 1 <= PB, PS <= n, p is a list of non-negative integers of length n, a is a list of non-negative integers of length n.
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        
        k = int(data[index + 1])
        
        PB = int(data[index + 2])
        
        PS = int(data[index + 3])
        
        index += 4
        
        p = list(map(int, data[index:index + n]))
        
        index += n
        
        a = list(map(int, data[index:index + n]))
        
        index += n
        
        result = func_1(n, k, PB, PS, p, a)
        
        results.append(result)
        
    #State: Output State: data is an empty list, index is 1 + 4 * t + 2 * n * t, t is a non-negative integer, n is a non-negative integer, k is a non-negative integer, PB and PS are non-negative integers such that 1 <= PB, PS <= n, p is a list of non-negative integers of length n, a is a list of non-negative integers of length n, results is a list of length t containing the results of func_1 for each iteration, sys.stdin is empty.
    for result in results:
        print(result)
        
    #State: Output State: The output state is the same as the initial state, except that the variable "result" has been updated to the last value in the "results" list.

#Overall this is what the function does:This function reads input from standard input, processes it, and prints the results. It expects the input to be a list of strings representing integers or space-separated lists of integers. The function iterates over the input data, extracting parameters such as the number of test cases (t), the size of the input arrays (n), and other integers (k, PB, PS). It then calls another function (func_1) with these parameters and stores the results in a list. Finally, it prints each result from the list. The function modifies the input data by consuming it and updates the results list with the output of func_1 for each iteration.

