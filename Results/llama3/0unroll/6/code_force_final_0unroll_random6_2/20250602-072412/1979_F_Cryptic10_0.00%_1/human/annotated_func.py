#State of the program right berfore the function call: d is a non-negative integer
    print(f'? {d}')
    #This is printed: ? [d] (where d is a non-negative integer)
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns two values: v and u, where v is an integer and u is an integer.

#Overall this is what the function does:The function reads two integers from the standard input and returns them as a pair of integers, v and u.

#State of the program right berfore the function call: n is a positive integer greater than 1, func_1 is a function that takes an integer d as input and returns a tuple of two integers (v, u) as output.
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
    #This is printed: ! [1 to n] (where [1 to n] are the elements of the path list, which are integers from 1 to n in some order, separated by spaces)
    sys.stdout.flush()

#Overall this is what the function does:Generates a permutation of integers from 1 to n (inclusive) and prints it in a specific order, potentially using an external function func_1 to guide the ordering process. The function takes an integer n and a function func_1 as input, and returns no value, instead printing the permutation directly to the console.

