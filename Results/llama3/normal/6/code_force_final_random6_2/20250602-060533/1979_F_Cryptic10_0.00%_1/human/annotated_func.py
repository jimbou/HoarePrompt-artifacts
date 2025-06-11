#State of the program right berfore the function call: d is a non-negative integer less than n, where n is the number of vertices in the graph.
    print(f'? {d}')
    #This is printed: ? d (where d is a non-negative integer less than n, the number of vertices in the graph)
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns two integers, v and u, where v is an integer and u is an integer.

#Overall this is what the function does:The function prints a query with a non-negative integer d (less than the number of vertices in the graph) and then reads two integers v and u from the input, returning them as a result.

#State of the program right berfore the function call: n is a positive integer greater than or equal to 2.
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
        
    #State: `remaining_vertices` is an empty set, `path` contains all the integers from 1 to `n` (inclusive) in the order they were removed from `remaining_vertices`.
    print(f"! {' '.join(map(str, path))}")
    #This is printed: ! 1 2 3 ... n (where n is the number of vertices and the integers are listed in the order they were removed from remaining_vertices)
    sys.stdout.flush()

#Overall this is what the function does:This function generates a path of integers from 1 to n (inclusive) in a specific order, removes each integer from a set of remaining vertices, and prints the path in the order the integers were removed. The function takes a positive integer n greater than or equal to 2 as input and does not return any value.

