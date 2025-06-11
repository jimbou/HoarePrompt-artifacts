#State of the program right berfore the function call: stdin contains a line of space-separated integers.
    return map(int, input().split())
    #The program returns a map object that contains a sequence of integers, where each integer is a space-separated integer from the input line in stdin.

#Overall this is what the function does:The function reads a line of space-separated integers from standard input and returns a map object containing the sequence of integers.

#State of the program right berfore the function call: stdin contains a line of space-separated integers.
    return list(map(int, input().split()))
    #The program returns a list of integers that were provided as space-separated input in stdin.

#Overall this is what the function does:The function reads a line of space-separated integers from standard input and returns them as a list of integers.

#State of the program right berfore the function call: n is a non-negative integer, v is a value of any type
    return [v for i in range(n)]
    #The program returns a list of 'n' elements, where each element is 'v'. 'n' is a non-negative integer and 'v' is a value of any type.

#Overall this is what the function does:The function creates and returns a list containing 'n' elements, all of which are the value 'v'. The function accepts two parameters: 'n', a non-negative integer representing the number of elements in the list, and 'v', a value of any type that will be used to populate the list. The function does not modify any external state or have any side effects beyond returning the newly created list.

#State of the program right berfore the function call: n and m are positive integers, v is a value of any type.
    return [[v for i in range(m)] for i in range(n)]
    #The program returns a 2D list (or matrix) with 'n' number of rows and 'm' number of columns, where each element in the list is the value 'v'.

#Overall this is what the function does:Creates a 2D list (or matrix) with a specified number of rows and columns, where every element is initialized with a given value. The function takes three parameters: the number of rows (n), the number of columns (m), and the value to fill the matrix (v), and returns the constructed matrix.

#State of the program right berfore the function call: n is a positive integer and m is a non-negative integer such that m <= n. The function func_1() returns a tuple of two integers.
    l = [[] for i in range(n + 1)]
    for i in range(m):
        x, y = func_1()
        
        l[x].append(y)
        
        l[y].append(x)
        
    #State: n is a positive integer, m is a non-negative integer such that m <= n, l is a list of n + 1 lists where the list at index x contains y and the list at index y contains x, and both lists also contain each other, and the list at index x contains y and the list at index y contains x, and so on, i is m - 1, x and y are the returned values of func_1()
    return l
    #The program returns a list of n + 1 lists where each list contains two elements that are indices of each other in the list, and the list at index x contains y and the list at index y contains x, and so on.

#Overall this is what the function does:The function constructs and returns a list of n + 1 lists, where each list represents a bidirectional connection between two indices. The function accepts two parameters, n and m, where n is a positive integer and m is a non-negative integer such that m <= n. The function iterates m times, calling func_1() to obtain two indices, x and y, and appends these indices to each other's lists in the main list. The function returns the constructed list, where each list at index x contains y and each list at index y contains x, representing a bidirectional connection between the two indices.

#State of the program right berfore the function call: n is a positive integer, m is a non-negative integer such that m <= n.
    l = [[(0) for i in range(n + 1)] for i in range(n + 1)]
    for i in range(m):
        x, y = func_1()
        
        l[x][y] = 1
        
        l[y][x] = 1
        
    #State: n is a positive integer, m is a non-negative integer such that m <= n, l is a 2D list of size (n+1) x (n+1) where l[x][y], l[y][x], l[x][x], and l[y][y] are 1 and all other elements are 0, i is m-1, x and y are the returned values of func_1()
    return l
    #The program returns a 2D list 'l' of size (n+1) x (n+1) where 'n' is a positive integer, 'l[x][y]', 'l[y][x]', 'l[x][x]', and 'l[y][y]' are 1 and all other elements are 0.

#Overall this is what the function does:The function generates a 2D list 'l' of size (n+1) x (n+1) where 'n' is a positive integer, and sets 'l[x][y]', 'l[y][x]', 'l[x][x]', and 'l[y][y]' to 1 for 'm' number of pairs (x, y) obtained from function func_1(), while keeping all other elements as 0.

#State of the program right berfore the function call: l is a list of hashable elements
    d = {}
    for i in l:
        d[i] = d.get(i, 0) + 1
        
    #State: `l` is a list of hashable elements, `d` is a dictionary where each key is an element from `l` and its corresponding value is the number of times that element appears in `l`, `i` is the last element in the list `l`.
    return d
    #The program returns a dictionary `d` where each key is an element from the list `l` and its corresponding value is the number of times that element appears in `l`.

#Overall this is what the function does:Counts the occurrences of each unique element in a list and returns a dictionary where each key is an element from the list and its corresponding value is the number of times that element appears in the list.

#State of the program right berfore the function call: l is a 2D list of integers, where each inner list has the same length.
    n = len(l)
    m = len(l[0])
    p = [[(0) for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            p[i][j] = p[i - 1][j] + p[i][j - 1] + l[i - 1][j - 1] - p[i - 1][j - 1]
        
    #State: `l` is a 2D list of integers, where each inner list has the same length, `n` is the number of inner lists in `l`, `m` is the length of each inner list in `l`, `p` is a 2D list of integers with `n+1` rows and `m+1` columns, where `p[i][j]` is equal to `p[i - 1][j] + p[i][j - 1] + l[i - 1][j - 1] - p[i - 1][j - 1]` for all `i` in range 1 to `n+1` and `j` in range 1 to `m`, `i` is `n+1`, `j` is `m`.
    return p
    #The program returns a 2D list of integers `p` with `n+1` rows and `m+1` columns, where each element `p[i][j]` is the sum of the elements in the sub-matrix of `l` from the top-left corner to the cell at position `(i-1, j-1)`, for all `i` in range 1 to `n+1` and `j` in range 1 to `m`.

#Overall this is what the function does:This function calculates the cumulative sum of a 2D list of integers, returning a new 2D list where each element at position (i, j) represents the sum of all elements in the original list from the top-left corner to the cell at position (i-1, j-1). The function takes a 2D list of integers as input and returns a new 2D list with the cumulative sums, effectively transforming the input data into a new representation that facilitates range sum queries.

#State of the program right berfore the function call: x is an integer
    return max(1 - (x & x - 1), 0)
    #The program returns the number of trailing zeros in the binary representation of the integer x, or 0 if x is 0

#Overall this is what the function does:This function takes an integer x as input and returns the number of trailing zeros in its binary representation. If x is 0, it returns 0.

#State of the program right berfore the function call: l is a list of integers.
    a = 0
    for i in l:
        a = gcd(a, i)
        
    #State: `l` is a list of integers, `a` is the greatest common divisor of 0 and all integers in the list, `i` is the last integer in the list.
    return a
    #The program returns the greatest common divisor of 0 and all integers in the list `l`.

#Overall this is what the function does:This function calculates and returns the greatest common divisor of 0 and all integers in the input list. Since the greatest common divisor of 0 and any number is always 0, the function effectively returns 0 for any input list of integers.

#State of the program right berfore the function call: num is a positive integer.
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
        
    #State: `num` is a positive integer, `prime` is a list of boolean values of length `num + 1` with `prime[0]` and `prime[1]` set to `False`, `Highest_Prime` is a list of integers of length `num + 1` with all elements initialized to `0`, `Lowest_Prime` is a list of integers of length `num + 1` with all elements initialized to `0`, `p` is `num + 1`. If `prime[p]` is `True`, then for all `i` in range(`2 * p`, `num + 1`, `p`), `prime[i]` is set to `False`, `Lowest_Prime[p]` is set to `p` and for all `i` in range(`2 * p`, `num + 1`, `p`), `Lowest_Prime[i]` is set to `p`, `Highest_Prime[p]` is set to `p` and for all `i` in range(`2 * p`, `num + 1`, `p`), `Highest_Prime[i]` is set to `p`.
    p = []
    for i in range(num + 1):
        if prime[i]:
            p.append(i)
        
    #State: `num` is a positive integer, `prime` is a list of boolean values of length `num + 1` with `prime[0]` and `prime[1]` set to `False`, `Highest_Prime` is a list of integers of length `num + 1` with all elements initialized to `0`, `Lowest_Prime` is a list of integers of length `num + 1` with all elements initialized to `0`, `i` is `num`, `p` is a list containing all prime numbers from 2 to `num`.
    return p
    #The program returns a list of all prime numbers from 2 to a positive integer `num`.

#Overall this is what the function does:This function generates a list of all prime numbers from 2 to a given positive integer `num`. It initializes a boolean array `prime` of size `num + 1` to track prime numbers, and two integer arrays `Highest_Prime` and `Lowest_Prime` to store the highest and lowest prime factors of each number. It then iterates through the numbers from 2 to `num`, marking non-prime numbers and updating the prime factors. Finally, it constructs a list `p` of all prime numbers found and returns it.

#State of the program right berfore the function call: num is a positive integer and Prime_array is a list of integers such that Prime_array[i] is a prime factor of i+1 for all i in range(len(Prime_array)).
    d = {}
    while num != 1:
        x = Prime_array[num]
        
        d[x] = d.get(x, 0) + 1
        
        num //= x
        
    #State: num is 1, Prime_array is a list of integers such that Prime_array[i] is a prime factor of i+1 for all i in range(len(Prime_array)), d is a dictionary containing key-value pairs where the keys are prime factors of the original value of num and the values are the number of times each prime factor appears in the prime factorization of the original value of num.
    return d
    #The program returns a dictionary containing key-value pairs where the keys are prime factors of the original value of num (which is 1) and the values are the number of times each prime factor appears in the prime factorization of the original value of num (which is 1). Since 1 has no prime factors, the dictionary is empty.

#Overall this is what the function does:This function takes a positive integer `num` and a list of integers `Prime_array` as input, where `Prime_array[i]` is a prime factor of `i+1` for all `i` in the range of `Prime_array`. It returns a dictionary containing the prime factors of the original value of `num` as keys and their respective counts in the prime factorization of `num` as values. If `num` is 1, the function returns an empty dictionary, as 1 has no prime factors.

#State of the program right berfore the function call: n is a positive integer.
    d = {}
    x = 2
    while x * x <= n:
        while n % x == 0:
            d[x] = d.get(x, 0) + 1
            n //= x
        
        x += 1
        
    #State: n is 1, d is a dictionary with key-value pairs where the keys are all prime factors of the original value of n and the values are the number of times each prime factor divides the original value of n, x is the smallest prime number greater than the square root of the original value of n.
    if (n > 1) :
        d[n] = d.get(n, 0) + 1
    #State: n is 1, d is a dictionary with key-value pairs where the keys are all prime factors of the original value of n and the values are the number of times each prime factor divides the original value of n, except for the key n which has been incremented by 1 if n was greater than 1, x is the smallest prime number greater than the square root of the original value of n.
    return d
    #The program returns a dictionary d where the keys are all prime factors of the original value of n (which is 1) and the values are the number of times each prime factor divides the original value of n, except for the key n which has been incremented by 1 if n was greater than 1 (which is not the case here since n is 1). Since n is 1, it has no prime factors, so the dictionary d is empty.

#Overall this is what the function does:This function takes a positive integer n as input and returns a dictionary containing the prime factors of n and their respective counts. If n is a prime number greater than 1, it is also included in the dictionary with a count of 1. The function effectively performs prime factorization of the input number n.

#State of the program right berfore the function call: d is a dictionary where the keys are integers and the values are integers such that for each key i, d[i] >= 1.
    s = 0
    for i in d:
        s += pow(i, d[i] - 1) * (i - 1)
        
    #State: `d` is a dictionary where the keys are integers and the values are integers such that for each key `i`, `d[i] >= 1` and `d` must have at least 1 key, `i` is the last key in the dictionary `d`, `s` is `n * pow(i, d[i] - 1) * (i - 1)` where `n` is the number of keys in `d`.
    return s
    #The program returns s which is the product of the number of keys in dictionary d, the last key in dictionary d raised to the power of the value of the last key minus 1, and the last key minus 1.

#Overall this is what the function does:Calculates the product of the number of keys in a dictionary, the last key raised to the power of its value minus 1, and the last key minus 1, assuming the dictionary has at least one key and all values are integers greater than or equal to 1.

#State of the program right berfore the function call: n is a positive integer and mod is a positive integer.
    f = [1]
    for i in range(1, n + 1):
        f.append(f[i - 1] * i % mod % mod)
        
    #State: `n` is a positive integer, `mod` is a positive integer, `f` is a list containing `n + 1` elements, which are 1 modulo `mod`, 2 modulo `mod`, 4 modulo `mod`, ..., `n!` modulo `mod` modulo `mod`, `i` is `n`.
    return f
    #The program returns a list `f` containing `n + 1` elements, which are 1 modulo `mod`, 2 modulo `mod`, 4 modulo `mod`, ..., `n!` modulo `mod` modulo `mod`, where `n` is a positive integer and `mod` is a positive integer.

#Overall this is what the function does:Computes and returns a list of factorials modulo a given modulus, up to a specified positive integer n. The list contains n+1 elements, where each element is the factorial of its index modulo the given modulus.

#State of the program right berfore the function call: n is a positive integer, mod is an integer such that mod >= -1.
    if (mod == -1) :
        dearr = [1, 0]
        for i in range(2, n + 1):
            dearr.append((i - 1) * (dearr[i - 1] + dearr[i - 2]))
            
        #State: `n` is greater than or equal to 2, `i` is `n`, `mod` is -1, `dearr` is a list containing the integers 1, 0, and the subsequent elements are the result of the recursive formula `(i - 1) * (dearr[i - 1] + dearr[i - 2])` for `i` ranging from 2 to `n`.
    else :
        dearr = [1, 0]
        for i in range(2, n + 1):
            dearr.append((i - 1) % mod * (dearr[i - 1] + dearr[i - 2]) % mod % mod)
            
        #State: `n` is a positive integer, `mod` is an integer such that `mod` is larger than or equal to 0, `i` is `n + 1`, `dearr` is a list containing the integers 1, 0, and ((k - 1) % mod * (dearr[k - 1] + dearr[k - 2]) % mod % mod) for all integers `k` such that 2 is less than or equal to `k` and `k` is less than or equal to `n + 1`.
    #State: *n is a positive integer, mod is an integer such that mod >= -1. If mod is -1, then n is greater than or equal to 2, i is n, and dearr is a list containing the integers 1, 0, and the subsequent elements are the result of the recursive formula (i - 1) * (dearr[i - 1] + dearr[i - 2]) for i ranging from 2 to n. If mod is not -1, then mod is an integer such that mod is larger than or equal to 0, i is n + 1, and dearr is a list containing the integers 1, 0, and ((k - 1) % mod * (dearr[k - 1] + dearr[k - 2]) % mod % mod) for all integers k such that 2 is less than or equal to k and k is less than or equal to n + 1.
    return dearr
    #The program returns a list of integers, where the first two elements are 1 and 0, and the subsequent elements are calculated using a recursive formula. If mod is -1, the formula is (i - 1) * (dearr[i - 1] + dearr[i - 2]) for i ranging from 2 to n. If mod is not -1, the formula is ((k - 1) % mod * (dearr[k - 1] + dearr[k - 2]) % mod) for all integers k such that 2 is less than or equal to k and k is less than or equal to n + 1. The length of the list is n + 1 if mod is not -1, and n if mod is -1.

#Overall this is what the function does:This function generates a list of integers based on a recursive formula, taking into account two parameters: `n` (a positive integer) and `mod` (an integer greater than or equal to -1). If `mod` is -1, the function calculates the list elements using the formula `(i - 1) * (dearr[i - 1] + dearr[i - 2])` for `i` ranging from 2 to `n`, and returns a list of length `n`. If `mod` is not -1, the function calculates the list elements using the formula `((k - 1) % mod * (dearr[k - 1] + dearr[k - 2]) % mod)` for all integers `k` such that 2 is less than or equal to `k` and `k` is less than or equal to `n + 1`, and returns a list of length `n + 1`. The first two elements of the list are always 1 and 0.

#State of the program right berfore the function call: p is a sorted list and x is a value that can be compared with elements of p.
    i = bisect_left(p, x)
    if (i != len(p) and p[i] == x) :
        return i
        #The program returns the insertion point for `x` in `p` to maintain sorted order, which is equal to the index of the element in `p` that is equal to `x`.
    else :
        return -1
        #The program returns -1, which is an integer value.

#Overall this is what the function does:This function searches for the value `x` in a sorted list `p` and returns the index of `x` if found, or -1 if not found, maintaining the sorted order of the list.

#State of the program right berfore the function call: p is a sorted list of integers and x is an integer.
    n = len(p)
    l, r = 0, n - 1
    if (p[0] > x) :
        return -1
        #The program returns -1
    #State: *p is a sorted list of integers, x is an integer, n is the length of p, l is 0, r is the last index of p, and the first element of p is less than or equal to x
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
        
    #State: l is equal to r, and p[l] is less than or equal to x and p[r] is greater than x or l is equal to r and p[l] is equal to x or l is equal to r + 1.
    return mid
    #The program returns mid, where mid is a value between l and r (inclusive) or equal to l or r, and p[l] is less than or equal to x and p[r] is greater than x, or mid is equal to l and p[l] is equal to x, or mid is equal to l + 1.

#Overall this is what the function does:This function performs a binary search on a sorted list of integers to find the index of the largest element that is less than or equal to a given integer. If the list is empty or the first element is greater than the given integer, it returns -1. Otherwise, it returns the index of the largest element that is less than or equal to the given integer, or the index of the first element that is greater than the given integer if no such element exists.

#State of the program right berfore the function call: p is a sorted list of distinct integers, and x is an integer.
    n = len(p)
    l, r = 0, n - 1
    if (p[-1] < x) :
        return n
        #The program returns the length of the sorted list p, which is the number of distinct integers in the list.
    #State: *p is a sorted list of distinct integers, x is an integer, n is the length of p, l is 0, and r is the last index of p. The last element of p is larger than or equal to x
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
        
    #State: p is a sorted list of distinct integers, x is an integer, n is the length of p, l is the index of the smallest element in p that is greater than or equal to x, and r is the last index of p. If p[mid] is greater than or equal to x, then mid is the index of the smallest element in p that is greater than or equal to x. If p[mid] is less than x, then l is the index of the smallest element in p that is greater than x.
    return mid
    #The program returns the index of the smallest element in the sorted list `p` that is greater than or equal to the integer `x`.

#Overall this is what the function does:This function performs a binary search on a sorted list of distinct integers to find the index of the smallest element that is greater than or equal to a given integer. If the given integer is larger than the last element in the list, the function returns the length of the list. The function takes a sorted list of distinct integers and an integer as input and returns an index or the length of the list, depending on the relationship between the input integer and the list elements.

#State of the program right berfore the function call: x is a non-negative integer.
    if (x == 0 or x == 1) :
        return x
        #The program returns x which is a non-negative integer and its value is either 0 or 1.
    #State: *x is a non-negative integer, and x is neither 0 nor 1
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
        
    #State: l is equal to r, and l is a non-negative integer, and l is neither 0 nor 1, and l is less than or equal to the original value of x, and l is either the square root of x or the largest integer less than the square root of x.

#Overall this is what the function does:This function calculates the integer square root of a non-negative integer x. If x is 0 or 1, it returns x. Otherwise, it returns the largest integer less than or equal to the square root of x.

#State of the program right berfore the function call: a and b are integers, mod is a positive integer, and a and b are non-negative.
    ans = 1
    a %= mod
    while b:
        if b & 1:
            ans = ans * a % mod
        
        a = a * a % mod
        
        b >>= 1
        
    #State: a is the remainder of the original value of a divided by mod raised to the power of 2 to the power of the number of iterations, mod is unchanged, b is 0, ans is the remainder of the original value of a divided by mod raised to the power of the number of 1 bits in the binary representation of the original value of b.
    return ans
    #The program returns the remainder of the original value of a divided by mod raised to the power of the number of 1 bits in the binary representation of the original value of b.

#Overall this is what the function does:Computes the remainder of a raised to the power of b, modulo mod, where a and b are non-negative integers and mod is a positive integer. The function takes three parameters: a, b, and mod, and returns the result of the modular exponentiation.

#State of the program right berfore the function call: a and b are lists of elements of any type and value, and they are not empty.
    dp = [([0] * (len(b) + 1)) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
    #State: `a` and `b` are lists of elements of any type and value, and they are not empty, `dp` is a 2D list of size `(len(a) + 1) x (len(b) + 1)`, where `dp[i][j]` is the length of the longest common subsequence of `a` and `b` ending at index `i - 1` in `a` and `j - 1` in `b`, for all `i` from 1 to `len(a)` and `j` from 1 to `len(b)`.
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
        
    #State: a and b are lists of elements of any type and value, and they are not empty, dp is a 2D list of size (len(a) + 1) x (len(b) + 1), where dp[i][j] is the length of the longest common subsequence of a and b ending at index i - 1 in a and j - 1 in b, for all i from 1 to len(a) and j from 1 to len(b). i is 0, j is 0, and l is a list containing the longest common subsequence of a and b in reverse order.
    s = ''.join(l)
    return s[::-1]
    #The program returns a string that represents the longest common subsequence of lists `a` and `b` in the correct order.

#Overall this is what the function does:This function takes two non-empty lists `a` and `b` as input and returns a string representing the longest common subsequence of the elements in `a` and `b` in the correct order. The function does not modify the input lists `a` and `b`.

#State of the program right berfore the function call: arr is a list of integers
    l = []
    for i in arr:
        pos = bisect_left(l, i)
        
        if pos == len(l):
            l.append(i)
        else:
            l[pos] = i
        
    #State: `arr` is a list of integers, `l` is a sorted list of integers where each element is from `arr` and all duplicates are removed, `i` is the last integer in the list `arr`, and `pos` is the insertion point for the last integer in `arr` in `l` to maintain sorted order.
    return len(l)
    #The program returns the number of unique integers in the list `arr`, which is the length of the sorted list `l` without duplicates.

#Overall this is what the function does:This function takes a list of integers as input, removes duplicates while maintaining sorted order, and returns the count of unique integers. It does not modify the original input list. The function's output represents the number of unique integers present in the input list.

#State of the program right berfore the function call: ver is a node in the graph, graph is a dictionary where each key is a node and its corresponding value is a list of neighboring nodes, and vis is a list where vis[i] represents the visited status of node i.
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
        
    #State: The stack is empty, `vis[node]` is 1 for all nodes in the graph, and the graph remains unchanged.

#Overall this is what the function does:Traverses a graph using Depth-First Search (DFS) starting from a given node, marks all visited nodes, and prints the visited nodes in the order they were visited, without modifying the graph structure.

#State of the program right berfore the function call: ver is a node in the graph, graph is a dictionary where each key is a node and its corresponding value is a list of its neighboring nodes, and vis is a list or dictionary where vis[i] represents whether node i has been visited or not.
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
        
    #State: All nodes in the graph have been visited, the deque `q` is empty, `ver` is assigned the value of the last node in the graph, the last node in the graph which is `ver` has been printed, graph[ver] must have all nodes visited, and all nodes in graph[ver] are marked as visited if they were not visited before, otherwise nothing changes, and this is printed: the value of `ver` (the last node in the graph) followed by a space. Additionally, if the node was not visited before, it is now marked as visited. If the node was not visited before, the deque `q` now contains the node that was previously the last node in graph[ver].

#Overall this is what the function does:This function performs a breadth-first traversal of a graph, starting from a given node, and prints the value of each node as it is visited. It marks each visited node as visited and ensures that all nodes in the graph are visited. The function modifies the input graph by marking all visited nodes and prints the values of all nodes in the graph, including the last node visited.

