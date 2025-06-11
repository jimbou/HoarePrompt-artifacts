#State of the program right berfore the function call: d is a non-negative integer.
    print(f'? {d}')
    #This is printed: ? [d] (where d is a non-negative integer)
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns two integers, v and u.

#Overall this is what the function does:The function reads a non-negative integer d from the standard output, prints a message with the value of d, waits for user input of two integers, and returns these two integers.

#State of the program right berfore the function call: n is a positive integer greater than or equal to 2, and func_1 is a function that takes an integer d as input and returns a tuple of two integers (v, u) as output.
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
        
    #State: n is a positive integer greater than or equal to 2, func_1 is a function that takes an integer d as input and returns a tuple of two integers (v, u) as output, path is a list containing the values of v, remaining_vertices is an empty set.
    print(f"! {' '.join(map(str, path))}")
    #This is printed: ! [values of v in the path list]
    sys.stdout.flush()

#Overall this is what the function does:The function generates a path by iteratively selecting vertices from a set of remaining vertices, using the provided function func_1 to determine the next vertex to add to the path. The function continues this process until all vertices have been selected, at which point it prints the generated path and flushes the output buffer. The function assumes that func_1 will eventually return a non-zero vertex for each degree d, and that the number of vertices n is a positive integer greater than or equal to 2.

