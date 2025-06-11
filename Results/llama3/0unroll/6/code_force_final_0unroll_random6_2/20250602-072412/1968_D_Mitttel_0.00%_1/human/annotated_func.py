#State of the program right berfore the function call: n is a positive integer, k is a positive integer, PB and PS are positive integers such that 1 <= PB <= n and 1 <= PS <= n, p is a list of n positive integers such that 1 <= p[i] <= n for all i, and a is a list of n positive integers.
    bodya_score = calculate_score(PB)
    sasha_score = calculate_score(PS)
    if (bodya_score > sasha_score) :
        return 'Bodya'
        #The program returns the string 'Bodya'
    else :
        if (sasha_score > bodya_score) :
            return 'Sasha'
            #The program returns the string 'Sasha'
        else :
            return 'Draw'
            #The program returns the string 'Draw'.

#Overall this is what the function does:Determines the winner of a game between 'Bodya' and 'Sasha' based on their scores, which are calculated using the 'calculate_score' function. The function takes no explicit parameters but uses the global variables PB and PS to calculate the scores. It returns the winner as a string, either 'Bodya', 'Sasha', or 'Draw' if the scores are equal.

#State of the program right berfore the function call: start_pos is a positive integer, k is a positive integer, p is a list of positive integers representing a permutation, a is a list of positive integers, and the length of p and a is equal to the maximum value in p and a.
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
        
    #State: score is the sum of the first k elements of a, current_pos is the kth element of p, steps is k, visited is a dictionary containing the first k elements of p as keys and their corresponding indices as values, cycle_start is -1, start_pos is unchanged, k is unchanged, p is unchanged, and a is unchanged.
    if (cycle_start != -1) :
        cycle_length = steps - cycle_start
        cycle_score = 0
        cycle_pos = current_pos
        for _ in range(cycle_length):
            cycle_score += a[cycle_pos - 1]
            
            cycle_pos = p[cycle_pos - 1]
            
        #State: Output State: The score remains the sum of the first k elements of a, current_pos remains the kth element of p, steps remains k, visited remains a dictionary containing the first k elements of p as keys and their corresponding indices as values, cycle_start remains unchanged, start_pos remains unchanged, k remains unchanged, p remains unchanged, a remains unchanged, cycle_length is 0, cycle_score is the sum of the elements of a in the cycle, and cycle_pos is the element of p that is the last element of the cycle.
        remaining_steps = k - steps
        full_cycles = remaining_steps // cycle_length
        remainder_steps = remaining_steps % cycle_length
        score += full_cycles * cycle_score
        for _ in range(remainder_steps):
            score += a[current_pos - 1]
            
            current_pos = p[current_pos - 1]
            
        #State: Output State: The score is increased by the sum of the elements of a in the remainder steps, current_pos is the element of p that is the last element of the remainder steps, steps remains k, visited remains a dictionary containing the first k elements of p as keys and their corresponding indices as values, cycle_start remains unchanged, start_pos remains unchanged, k remains unchanged, p remains unchanged, a remains unchanged, cycle_length is 0, cycle_score is the sum of the elements of a in the cycle, and cycle_pos is the element of p that is the last element of the cycle.
    #State: *The score, current_pos, steps, visited, cycle_start, start_pos, k, p, and a are updated based on the value of cycle_start. If cycle_start is not -1, the score is increased by the sum of the elements of a in the remainder steps, current_pos is the element of p that is the last element of the remainder steps, steps remains k, visited remains a dictionary containing the first k elements of p as keys and their corresponding indices as values, cycle_start remains unchanged, start_pos remains unchanged, k remains unchanged, p remains unchanged, a remains unchanged, cycle_length is 0, cycle_score is the sum of the elements of a in the cycle, and cycle_pos is the element of p that is the last element of the cycle. If cycle_start is -1, the state of the variables remains unchanged.
    return score
    #The program returns the score, which is either the initial score if cycle_start is -1, or the initial score plus the sum of the elements of list a in the remainder steps if cycle_start is not -1.

#Overall this is what the function does:Calculates the score by traversing a permutation list 'p' and accumulating values from list 'a' for 'k' steps, handling cycles in the permutation by adding the score of full cycles and remaining steps, and returns the total score.

#State of the program right berfore the function call: data is a list of strings where each string is a space-separated list of integers, index is a non-negative integer such that index < len(data).
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
        
    #State: Output State: The loop has executed t iterations, and the results list now contains t elements, each representing the result of the func_1 function call for the corresponding iteration. The index variable has been incremented by 4 + 2n for each iteration, where n is the value of the variable n in each iteration. The data list remains unchanged, as does the stdin variable.
    for result in results:
        print(result)
        
    #State: Output State: The loop has executed t iterations, and the results list now contains t elements, each representing the result of the func_1 function call for the corresponding iteration. The index variable has been incremented by 4 + 2n for each iteration, where n is the value of the variable n in each iteration. The data list remains unchanged, as does the stdin variable.

#Overall this is what the function does:This function reads input from standard input, processes it, and prints the results. It expects the input to be a list of space-separated integers, where the first integer represents the number of test cases (t). For each test case, it reads in additional integers representing the size of an array (n), a value k, and two more integers PB and PS. It then reads in two arrays of integers, p and a, each of size n. The function calls another function, func_1, with these inputs and appends the result to a list of results. After processing all test cases, it prints each result in the results list.

