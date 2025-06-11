#State of the program right berfore the function call: stdin contains a sequence of test cases. Each test case consists of four inputs: first an integer, then a list of unique integers in ascending order, then an integer, and finally a list of pairs of unique integers. The first integer is the number of cities, the list of integers represents the coordinates of the cities, the second integer is the number of queries, and the list of pairs of integers represents the queries. The number of cities and the number of queries are positive integers. The coordinates of the cities are non-negative integers. The queries are unique pairs of city indices (1-indexed).
    for i in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        d1 = defaultdict(int)
        
        d2 = defaultdict(int)
        
        d1[2] = 1
        
        for i in range(1, n - 1):
            if l[i + 1] - l[i] < l[i] - l[i - 1]:
                d1[i + 2] = 1 + d1[i + 1]
            else:
                d1[i + 2] = l[i + 1] - l[i] + d1[i + 1]
        
        d2[n - 1] = 1
        
        for i in range(n - 2, 0, -1):
            if l[i] - l[i - 1] < l[i + 1] - l[i]:
                d2[i] = 1 + d2[i + 1]
            else:
                d2[i] = l[i] - l[i - 1] + d2[i + 1]
        
        m = int(input())
        
        for j in range(m):
            x, y = map(int, input().split())
            if y > x:
                print(d1[y] - d1[x])
            else:
                print(d2[y] - d2[x])
        
    #State: The output state will be a sequence of integers, each representing the total distance between two cities for each query. The distance is calculated based on the differences between the coordinates of the cities and the number of cities between them.

#Overall this is what the function does:This function reads a sequence of test cases from standard input, where each test case consists of a number of cities, their coordinates, a number of queries, and query pairs of city indices. It calculates the total distance between each pair of cities in the queries, considering the differences between city coordinates and the number of cities in between. The function then prints the total distance for each query.

