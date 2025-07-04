#State of the program right berfore the function call: No variables are present in the function signature. The function `func_1` is likely a helper function to read input values and return them as a map of integers.
def func_1():
    return map(int, input().split())
    #The program returns a map object that contains integers converted from the input string, where the input string is split by spaces.
#Overall this is what the function does:The function `func_1` reads a line of input from the user, splits it into substrings based on spaces, converts each substring into an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: There are no variables in the function signature of `func_2`. This function reads a line of input and returns a list of integers.
def func_2():
    return list(map(int, input().split()))
    #The program returns a list of integers that were provided as input, split by spaces.
#Overall this is what the function does:The function `func_2` reads a line of input from the user, splits the input by spaces, and returns a list of integers.

#State of the program right berfore the function call: n is an integer representing the number of sides of the polygon, and v is a list of integers representing the vertices Bessie has chosen. The length of v is x, where 2 ≤ x ≤ min(n, 2 · 10^5).
def func_3(n, v):
    return [v for i in range(n)]
    #The program returns a list that contains the list `v` repeated `n` times. Each element in the returned list is a copy of `v`.
#Overall this is what the function does:The function takes an integer `n` and a list `v`, and returns a new list where the list `v` is repeated `n` times. Each element in the returned list is a separate copy of `v`.

#State of the program right berfore the function call: n is an integer representing the number of sides of the polygon (4 ≤ n ≤ 10^9), m is an integer representing the number of vertices Bessie has chosen (2 ≤ m ≤ min(n, 2 · 10^5)), and v is a value that will be used to fill an n by m matrix.
def func_4(n, m, v):
    return [[v for i in range(m)] for i in range(n)]
    #The program returns an n by m matrix where each element is filled with the value v.
#Overall this is what the function does:The function generates and returns an n by m matrix where each element is filled with the specified value v.

#State of the program right berfore the function call: n is an integer representing the number of sides of the polygon (4 <= n <= 10^9), and m is an integer representing the number of edges or connections to be added to the graph (0 <= m <= min(n, 2 * 10^5)).
def func_5(n, m):
    l = [[] for i in range(n + 1)]
    for i in range(m):
        x, y = func_1()
        
        l[x].append(y)
        
        l[y].append(x)
        
    #State: `n` is an integer representing the number of sides of the polygon (4 <= n <= 10^9), `m` is an integer representing the number of edges or connections to be added to the graph (0 <= m <= min(n, 2 * 10^5)), `l` is a list of `n + 1` lists where each list contains the indices of the vertices that are directly connected to the corresponding vertex.
    return l
    #The program returns the list `l` which contains `n + 1` lists, where each list contains the indices of the vertices that are directly connected to the corresponding vertex.
#Overall this is what the function does:The function accepts two integer parameters, `n` representing the number of vertices in a polygon and `m` representing the number of edges to be added. It returns a list `l` containing `n + 1` lists, where each inner list contains the indices of the vertices directly connected to the corresponding vertex.

#State of the program right berfore the function call: n is an integer representing the number of sides of the polygon (4 ≤ n ≤ 10^9), and m is an integer representing the number of vertices that can be used to form diagonals (2 ≤ m ≤ min(n, 2 · 10^5)).
def func_6(n, m):
    l = [[(0) for i in range(n + 1)] for i in range(n + 1)]
    for i in range(m):
        x, y = func_1()
        
        l[x][y] = 1
        
        l[y][x] = 1
        
    #State: `n` is an integer representing the number of sides of the polygon (4 ≤ n ≤ 10^9), and `m` is an integer representing the number of vertices that can be used to form diagonals (2 ≤ m ≤ min(n, 2 · 10^5)). `l` is a 2D list with dimensions (n+1) x (n+1) where `l[x][y]` and `l[y][x]` are set to 1 for `m` unique pairs `(x, y)` returned by `func_1()`, and all other elements are 0.
    return l
    #The program returns a 2D list `l` with dimensions (n+1) x (n+1) where `l[x][y]` and `l[y][x]` are set to 1 for `m` unique pairs `(x, y)` returned by `func_1()`, and all other elements are 0.
#Overall this is what the function does:The function accepts two integer parameters, `n` representing the number of sides of a polygon and `m` representing the number of vertices that can be used to form diagonals. It returns a 2D list `l` with dimensions (n+1) x (n+1) where `l[x][y]` and `l[y][x]` are set to 1 for `m` unique pairs `(x, y)` obtained from `func_1()`, and all other elements are 0.

#State of the program right berfore the function call: l is a list of integers.
def func_7(l):
    d = {}
    for i in l:
        d[i] = d.get(i, 0) + 1
        
    #State: `l` is a list of integers; `d` is a dictionary where each key is a unique integer from the list `l` and its value is the count of how many times that integer appears in the list.
    return d
    #The program returns a dictionary `d` where each key is a unique integer from the list `l` and its value is the count of how many times that integer appears in the list.
#Overall this is what the function does:The function takes a list of integers as input and returns a dictionary where each key is a unique integer from the list, and its value is the count of how many times that integer appears in the list.

#State of the program right berfore the function call: l is a 2D list of integers, n is the number of rows in l, and m is the number of columns in l.
def func_8(l):
    n = len(l)
    m = len(l[0])
    p = [[(0) for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            p[i][j] = p[i - 1][j] + p[i][j - 1] + l[i - 1][j - 1] - p[i - 1][j - 1]
        
    #State: `p` is a 2D list where `p[i][j]` is the sum of all elements in the submatrix `l[0:i, 0:j]` for `1 <= i <= n` and `1 <= j <= m`.
    return p
    #The program returns the 2D list `p` where `p[i][j]` is the sum of all elements in the submatrix `l[0:i, 0:j]` for `1 <= i <= n` and `1 <= j <= m`.
#Overall this is what the function does:The function accepts a 2D list `l` of integers and returns a 2D list `p` where each element `p[i][j]` represents the sum of all elements in the submatrix from the top-left corner (0,0) to the position (i-1,j-1) in the original list `l`.

#State of the program right berfore the function call: x is an integer such that 2 <= x <= min(n, 2 * 10^5) where n is the number of sides of the polygon.
def func_9(x):
    return max(1 - (x & x - 1), 0)
    #The program returns 1 if x is a power of 2, otherwise it returns 0.
#Overall this is what the function does:The function accepts an integer `x` and returns 1 if `x` is a power of 2; otherwise, it returns 0.

#State of the program right berfore the function call: l is a list of integers.
def func_10(l):
    a = 0
    for i in l:
        a = gcd(a, i)
        
    #State: `a` is the GCD of all elements in `l`.
    return a
    #The program returns the GCD of all elements in list `l`.
#Overall this is what the function does:The function accepts a list of integers and returns their greatest common divisor (GCD).

#State of the program right berfore the function call: num is a non-negative integer.
def func_11(num):
    prime = [(True) for i in range(num + 1)]
    Highest_Prime = [(0) for i in range(num + 1)]
    Lowest_Prime = [(0) for i in range(num + 1)]
    prime[0] = prime[1] = False
    p = 2
    while p <= num:
        if prime[p] == True:
            Lowest_Prime[p] = p
            Highest_Prime[p] = p
            for i in range(2 * p, num + 1, p):
                prime[i] = False
                Highest_Prime[i] = p
                if Lowest_Prime[i] == 0:
                    Lowest_Prime[i] = p
        
        p += 1
        
    #State: `prime` is a list where each index `i` (from 2 to `num`) is `True` if `i` is a prime number and `False` otherwise; `Highest_Prime` is a list where each index `i` (from 2 to `num`) contains the largest prime factor of `i`; `Lowest_Prime` is a list where each index `i` (from 2 to `num`) contains the smallest prime factor of `i`; `p` is `num + 1`.
    p = []
    for i in range(num + 1):
        if prime[i]:
            p.append(i)
        
    #State: `prime` is a list where each index `i` (from 2 to `num`) is `True` if `i` is a prime number and `False` otherwise; `Highest_Prime` is a list where each index `i` (from 2 to `num`) contains the largest prime factor of `i`; `Lowest_Prime` is a list where each index `i` (from 2 to `num`) contains the smallest prime factor of `i`; `p` is a list containing all prime numbers from 2 to `num`.
    return p
    #The program returns a list `p` containing all prime numbers from 2 to `num`.
#Overall this is what the function does:The function accepts a non-negative integer `num` and returns a list of all prime numbers from 2 to `num`.

#State of the program right berfore the function call: num is a positive integer greater than 1, and Prime_array is a list where Prime_array[i] is the smallest prime factor of i for all i from 2 to num.
def func_12(num, Prime_array):
    d = {}
    while num != 1:
        x = Prime_array[num]
        
        d[x] = d.get(x, 0) + 1
        
        num //= x
        
    #State: `num` is 1, `Prime_array` remains the same, `d` is a dictionary with prime factors of the original `num` as keys and their counts as values.
    return d
    #The program returns an empty dictionary `{}`
#Overall this is what the function does:The function accepts a positive integer `num` greater than 1 and a list `Prime_array` where each element at index `i` is the smallest prime factor of `i` for all `i` from 2 to `num`. It returns a dictionary with the prime factors of `num` as keys and their respective counts as values.

#State of the program right berfore the function call: n is an integer greater than or equal to 2.
def func_13(n):
    d = {}
    x = 2
    while x * x <= n:
        while n % x == 0:
            d[x] = d.get(x, 0) + 1
            n //= x
        
        x += 1
        
    #State: 
    if (n > 1) :
        d[n] = d.get(n, 0) + 1
    #State: `n` is an integer. If `n` is greater than 1, `d[n]` is incremented by 1. If `n` is less than or equal to 1, `d[n]` remains unchanged.
    return d
    #The program returns the dictionary `d` where if `n` is greater than 1, `d[n]` is incremented by 1. If `n` is less than or equal to 1, `d[n]` remains unchanged.
#Overall this is what the function does:The function accepts an integer parameter `n` which is greater than or equal to 2. It returns a dictionary `d` representing the prime factorization of `n`, where the keys are the prime factors and the values are their respective counts in the factorization.

#State of the program right berfore the function call: d is a dictionary where keys are integers greater than 1 and values are positive integers.
def func_14(d):
    s = 0
    for i in d:
        s += pow(i, d[i] - 1) * (i - 1)
        
    #State: d is {2: 3, 3: 2}, s is 10.
    return s
    #The program returns 10
#Overall this is what the function does:The function accepts a dictionary `d` where keys are integers greater than 1 and values are positive integers. It calculates a specific sum based on the keys and values in the dictionary and returns the result. The provided example shows that for the input `{2: 3, 3: 2}`, the function returns 10, but the actual return value can vary depending on the input dictionary.

#State of the program right berfore the function call: n is a positive integer, and mod is an integer used for modulo operations.
def func_15(n, mod):
    f = [1]
    for i in range(1, n + 1):
        f.append(f[i - 1] * i % mod % mod)
        
    #State: `f` is `[1] + [i! % mod for i in range(1, n + 1)]
    return f
    #The program returns a list starting with 1, followed by the factorials of integers from 1 to n, each taken modulo mod.
#Overall this is what the function does:The function takes a positive integer `n` and an integer `mod`, and returns a list starting with 1, followed by the factorials of integers from 1 to `n`, each taken modulo `mod`.

#State of the program right berfore the function call: n is a positive integer, and mod is an integer where mod can be -1 or any other integer value.
def func_16(n, mod):
    if (mod == -1) :
        dearr = [1, 0]
        for i in range(2, n + 1):
            dearr.append((i - 1) * (dearr[i - 1] + dearr[i - 2]))
            
        #State: `n` is a positive integer, `mod` is -1, `dearr` is `[1, 0, 1, 2, 9, ..., (n-1) * (dearr[n-1] + dearr[n-2])]`
    else :
        dearr = [1, 0]
        for i in range(2, n + 1):
            dearr.append((i - 1) % mod * (dearr[i - 1] + dearr[i - 2]) % mod % mod)
            
        #State: `dearr` is a list of `n + 1` elements starting with `[1, 0]` and followed by the computed values for each `i` from `2` to `n` using the formula `((i - 1) % mod) * (dearr[i - 1] + dearr[i - 2]) % mod`.
    #State: `n` is a positive integer, and `mod` is an integer where `mod` can be -1 or any other integer value. If `mod` is -1, `dearr` is `[1, 0, 1, 2, 9, ..., (n-1) * (dearr[n-1] + dearr[n-2])]`. Otherwise, `dearr` is a list of `n + 1` elements starting with `[1, 0]` and followed by the computed values for each `i` from `2` to `n` using the formula `((i - 1) % mod) * (dearr[i - 1] + dearr[i - 2]) % mod`.
    return dearr
    #The program returns `dearr`, which is a list starting with `[1, 0]` and followed by computed values based on the formula `(i - 1) * (dearr[i - 1] + dearr[i - 2])` if `mod` is -1, or `((i - 1) % mod) * (dearr[i - 1] + dearr[i - 2]) % mod` if `mod` is any other integer value.
#Overall this is what the function does:The function `func_16` takes two parameters: `n`, a positive integer, and `mod`, an integer that can be -1 or any other integer value. It returns a list `dearr` starting with `[1, 0]`. If `mod` is -1, the subsequent values in the list are computed using the formula `(i - 1) * (dearr[i - 1] + dearr[i - 2])`. If `mod` is any other integer value, the subsequent values are computed using the formula `((i - 1) % mod) * (dearr[i - 1] + dearr[i - 2]) % mod`.

#State of the program right berfore the function call: p is a sorted list of integers, and x is an integer.
def func_17(p, x):
    i = bisect_left(p, x)
    if (i != len(p) and p[i] == x) :
        return i
        #The program returns `i`, which is the index where `x` is located in the sorted list `p`.
    else :
        return -1
        #The program returns -1
#Overall this is what the function does:The function `func_17` takes a sorted list of integers `p` and an integer `x` as input. It returns the index of `x` in `p` if `x` is present in the list. If `x` is not found, it returns -1.

#State of the program right berfore the function call: p is a sorted list of integers, and x is an integer such that x is within the range of the smallest and largest values in p.
def func_18(p, x):
    n = len(p)
    l, r = 0, n - 1
    if (p[0] > x) :
        return -1
        #The program returns -1
    #State: `p` is a sorted list of integers, `x` is an integer such that `x` is within the range of the smallest and largest values in `p`; `n` is the length of the list `p`; `l` is 0; `r` is `n - 1`. Additionally, the first element of `p` is less than or equal to `x`.
    while l <= r:
        mid = (l + r) // 2
        
        if p[mid] <= x:
            if mid != n - 1:
                if p[mid + 1] > x:
                    break
                else:
                    l = mid + 1
            else:
                mid = n - 1
                break
        else:
            r = mid - 1
        
    #State: `mid` is the last index where `p[mid] <= x`, `l` is greater than `r`.
    return mid
    #The program returns `mid` which is the last index where `p[mid] <= x`.
#Overall this is what the function does:The function `func_18` takes a sorted list of integers `p` and an integer `x` as input. It returns the last index in `p` where the element is less than or equal to `x`. If `x` is less than the smallest element in `p`, it returns -1.

#State of the program right berfore the function call: p is a sorted list of integers, and x is an integer such that x is within the range of possible values in p or just above the maximum value in p.
def func_19(p, x):
    n = len(p)
    l, r = 0, n - 1
    if (p[-1] < x) :
        return n
        #The program returns the length of the list `p`, which is `n`.
    #State: `p` is a sorted list of integers, `x` is an integer such that `x` is within the range of possible values in `p` or just above the maximum value in `p`, `n` is the length of the list `p`, `l` is 0, `r` is `n - 1`. Additionally, the last element of `p` is greater than or equal to `x`.
    while l <= r:
        mid = (l + r) // 2
        
        if p[mid] >= x:
            if mid != 0:
                if p[mid - 1] < x:
                    break
                else:
                    r = mid - 1
            else:
                mid = 0
                break
        else:
            l = mid + 1
        
    #State: `mid` is the smallest index such that `p[mid] >= x`, `l` and `r` are modified to reach the termination condition.
    return mid
    #The program returns `mid`, which is the smallest index such that `p[mid] >= x`.
#Overall this is what the function does:The function `func_19` takes a sorted list of integers `p` and an integer `x` as input. It returns the smallest index in `p` where the element is greater than or equal to `x`. If `x` is greater than all elements in `p`, it returns the length of the list `p`.

#State of the program right berfore the function call: x is a non-negative integer such that 0 <= x <= 2 * 10^5.
def func_20(x):
    if (x == 0 or x == 1) :
        return x
        #The program returns x, which is either 0 or 1.
    #State: x is a non-negative integer such that 0 <= x <= 2 * 10^5, and x is not 0 and x is not 1
    l = 1
    r = x
    while l <= r:
        mid = (l + r) / 2
        
        y = mid * mid
        
        if y > x:
            r = mid - 1
        elif y == x:
            return mid
        elif (mid + 1) * (mid + 1) > x:
            return mid
        else:
            l = mid + 1
        
    #State: the integer square root of `x`.
#Overall this is what the function does:The function accepts a non-negative integer `x` such that 0 <= x <= 2 * 10^5 and returns the integer square root of `x`.

#State of the program right berfore the function call: a is an integer, b is a non-negative integer, and mod is a positive integer.
def func_21(a, b, mod):
    ans = 1
    a %= mod
    while b:
        if b & 1:
            ans = ans * a % mod
        
        a = a * a % mod
        
        b >>= 1
        
    #State: 
    return ans
    #The program returns the value of 'ans'
#Overall this is what the function does:The function calculates and returns the result of \( a^b \mod \text{mod} \).

#State of the program right berfore the function call: a and b are lists of integers.
def func_22(a, b):
    dp = [([0] * (len(b) + 1)) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
    #State: `dp` is a 2D list where `dp[i][j]` contains the length of the longest common subsequence of the first `i` elements of `a` and the first `j` elements of `b`. The final value `dp[len(a)][len(b)]` gives the length of the longest common subsequence of the entire lists `a` and `b`.
    i, j = len(a), len(b)
    l = []
    while i != 0 and j != 0:
        if dp[i][j] == dp[i][j - 1]:
            j -= 1
        elif dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            i -= 1
            j -= 1
            l.append(a[i])
        
    #State: `i` is 0, `j` is 0, `l` contains the longest common subsequence of `a` and `b` in reverse order.
    s = ''.join(l)
    return s[::-1]
    #The program returns the longest common subsequence of `a` and `b` in reverse order.
#Overall this is what the function does:The function accepts two lists of integers, `a` and `b`, and returns the longest common subsequence of `a` and `b` in reverse order.

#State of the program right berfore the function call: arr is a list of integers.
def func_23(arr):
    l = []
    for i in arr:
        pos = bisect_left(l, i)
        
        if pos == len(l):
            l.append(i)
        else:
            l[pos] = i
        
    #State: `arr` is a list of integers; `l` is a sorted list containing the smallest possible elements from `arr` in non-decreasing order.
    return len(l)
    #The program returns the length of the list `l`, which contains the smallest possible elements from `arr` in non-decreasing order.
#Overall this is what the function does:The function accepts a list of integers and returns the length of a list that contains the smallest possible elements from the input list in non-decreasing order.

#State of the program right berfore the function call: ver is an integer representing a vertex in the graph, stack is a list used to keep track of vertices to visit, and vis is a list or dictionary used to mark visited vertices where vis[node] is 1 if the node has been visited and 0 otherwise.
def func_24(ver):
    stack = []
    stack.append(ver)
    vis[ver] = 1
    while len(stack):
        ver = stack.pop()
        
        print(ver, end=' ')
        
        for node in graph[ver]:
            if not vis[node]:
                stack.append(node)
                vis[node] = 1
        
    #State: `stack` is an empty list, `vis` has all reachable nodes marked as 1, and `ver` holds the last visited vertex.
    #
    #Output State:
#Overall this is what the function does:The function `func_24` performs a depth-first traversal of a graph starting from a given vertex `ver`. It uses a stack to keep track of vertices to visit and a list or dictionary `vis` to mark vertices as visited. After the traversal, all reachable nodes from `ver` are marked as visited in `vis`, and the function prints each visited vertex. The stack is empty at the end of the function's execution.

#State of the program right berfore the function call: ver is an integer representing a vertex in the graph, graph is a dictionary or list of lists where graph[ver] contains all the adjacent vertices to ver, and vis is a list or dictionary used to keep track of visited vertices such that vis[node] is 1 if the node has been visited and 0 otherwise.
def func_25(ver):
    q = deque()
    q.append(ver)
    vis[ver] = 1
    while len(q):
        ver = q.popleft()
        
        print(ver, end=' ')
        
        for node in graph[ver]:
            if not vis[node]:
                q.append(node)
                vis[node] = 1
        
    #State: `q` is an empty deque, `vis` has 1s for all vertices that were visited during the BFS traversal, and all reachable vertices from `ver` have been printed in BFS order.
#Overall this is what the function does:The function `func_25` performs a Breadth-First Search (BFS) traversal starting from a given vertex `ver` in a graph. It prints each visited vertex in BFS order and updates a `vis` list or dictionary to mark all reachable vertices as visited.

