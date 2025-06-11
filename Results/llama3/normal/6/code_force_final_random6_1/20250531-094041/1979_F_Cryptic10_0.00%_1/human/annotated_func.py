#State of the program right berfore the function call: d is a non-negative integer
    print(f'? {d}')
    #This is printed: ? [d] (where d is a non-negative integer)
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns a tuple containing two integers, v and u.

#Overall this is what the function does:The function reads a non-negative integer d from the standard output, prints a message with the value of d, waits for user input of two integers v and u, and returns them as a tuple.

#State of the program right berfore the function call: n is a positive integer greater than or equal to 2, and func_1 is a function that takes an integer d as input and returns a tuple of two integers (v, u).
    path = []
    remaining_vertices = set(range(1, n + 1))
    while remaining_vertices:
        for d in range(n - 1, -1, -1):
            v, u = func_1(d)
            if v == 0:
                continue
            if v in remaining_vertices:
                path.append(v)
                remaining_vertices.remove(v)
                break
        
    #State: n is a positive integer greater than or equal to 2, func_1 is a function that takes an integer d as input and returns a tuple of two integers (v, u), path is a list containing all integers from 1 to n (inclusive) in the order they were removed from remaining_vertices, remaining_vertices is an empty set.
    print(f"! {' '.join(map(str, path))}")
    #This is printed: ! [all integers from 1 to n in the order they were removed from remaining_vertices]
    sys.stdout.flush()

#Overall this is what the function does:This function generates a list of integers from 1 to n (inclusive) in a specific order determined by the input function func_1, and prints this list in the format "! [list of integers]" followed by a flush of the standard output buffer. The function does not return any value.

