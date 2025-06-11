#State of the program right berfore the function call: d is a non-negative integer
    print(f'? {d}')
    #This is printed: ? [d] (where d is the value of the non-negative integer d)
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns two integers, v and u.

#Overall this is what the function does:The function reads a non-negative integer d, prints it to the console, reads two integers v and u from the input, and returns them.

#State of the program right berfore the function call: n is a positive integer greater than or equal to 2, func_1 is a function that takes an integer d as input and returns a tuple of two integers (v, u), where v and u are vertices in the graph.
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
        
    #State: path is a list of integers from 1 to n (inclusive) in some order, remaining_vertices is an empty set.
    print(f"! {' '.join(map(str, path))}")
    #This is printed: ! [1 2 3 ... n] (where 1, 2, 3, ..., n are the integers in the path list, in some order)
    sys.stdout.flush()

#Overall this is what the function does:The function generates a path of integers from 1 to n (inclusive) in some order and prints it, ensuring that all integers are included exactly once. The function does not modify the input variables, but rather uses them to compute and output the path. Upon completion, the function has printed a single line starting with '!' followed by a space-separated list of integers from 1 to n in some order.

