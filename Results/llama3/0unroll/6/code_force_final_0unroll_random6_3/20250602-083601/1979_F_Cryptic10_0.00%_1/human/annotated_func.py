#State of the program right berfore the function call: d is a non-negative integer less than n, where n is the number of vertices in the graph.
    print(f'? {d}')
    #This is printed: ? [d] (where d is a non-negative integer less than n, the number of vertices in the graph)
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns a tuple containing two integers, v and u. The value of v is an integer, and the value of u is also an integer.

#Overall this is what the function does:The function takes no parameters and returns a tuple containing two integers, v and u, which are obtained from user input. The function does not modify any input variables. The returned integers v and u are not guaranteed to be within any specific range or have any specific relationship with each other or with the number of vertices in the graph (n).

#State of the program right berfore the function call: n is a positive integer greater than or equal to 2, func_1 is a function that takes a non-negative integer d as input and returns a tuple of two integers (v, u).
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
        
    #State: path contains a sequence of distinct integers from 1 to n (inclusive) in non-increasing order, remaining_vertices is an empty set.
    print(f"! {' '.join(map(str, path))}")
    #This is printed: ! [n] [n-1] [n-2] ... [2] [1] (where n is the last element of the path list)
    sys.stdout.flush()

#Overall this is what the function does:The function generates a sequence of distinct integers from 1 to n (inclusive) in non-increasing order and prints it. It uses a helper function `func_1` to determine the next integer in the sequence, and it continues until all integers from 1 to n have been included in the sequence. The function does not return any value, but instead prints the generated sequence and flushes the output buffer.

