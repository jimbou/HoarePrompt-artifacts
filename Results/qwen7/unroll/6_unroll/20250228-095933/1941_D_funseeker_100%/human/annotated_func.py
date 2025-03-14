#State of the program right berfore the function call: t is an integer representing the number of test cases, where 1 ≤ t ≤ 10^4. For each test case, n, m, and x are integers such that 2 ≤ n ≤ 1000, 1 ≤ m ≤ 1000, and 1 ≤ x ≤ n. The list of throws consists of m tuples, each containing an integer r_i (1 ≤ r_i ≤ n - 1) and a character c_i ('0', '1', or '?'), indicating the distance and the direction of the throw, respectively.
def func_1():
    return sys.stdin.readline().strip()
    #The program reads a line from standard input, strips any trailing whitespace, and returns it as a string.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing whitespace, and returns it as a string.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 2 ≤ n ≤ 1000, m is an integer such that 1 ≤ m ≤ 1000, x is an integer such that 1 ≤ x ≤ n, r_i is an integer such that 1 ≤ r_i ≤ n - 1, and c_i is a character that can be '0', '1', or '?'.
def func_2():
    return int(func_1())
    #The program returns an integer value generated by the function `func_1()` based on the given initial conditions.
#Overall this is what the function does:The function returns an integer value generated by calling another function `func_1()`, which is based on the initial conditions provided (t, n, m, x, r_i, and c_i).

#State of the program right berfore the function call: t is an integer representing the number of test cases, where 1 ≤ t ≤ 10^4. For each test case, n, m, and x are integers such that 2 ≤ n ≤ 1000, 1 ≤ m ≤ 1000, and 1 ≤ x ≤ n. The list of throws consists of m pairs of integers and characters, where each pair represents the distance r_i (1 ≤ r_i ≤ n - 1) and the direction c_i ('0', '1', or '?') for the i-th throw.
def func_3():
    return list(map(int, func_1().split()))
    #The program returns a list of integers obtained by splitting the string returned by func_1() and converting each element to an integer.
#Overall this is what the function does:The function accepts no parameters and returns a list of integers. This list is derived by first obtaining a string from `func_1()`, then splitting this string into individual elements, and finally converting each element into an integer.

#State of the program right berfore the function call: n is an integer representing the number of players (2 <= n <= 1000), m is an integer representing the number of throws made (1 <= m <= 1000), x is an integer representing the initial player who has the ball (1 <= x <= n), and ans is a set initialized with the player x. The function func_1() returns a string containing the distance r and direction c of a throw, and func_3() returns a tuple (n, m, x).
def func_4():
    n, m, x = func_3()
    ans = {x}
    for _ in range(m):
        r, c = func_1().split()
        
        r = int(r)
        
        temp = set()
        
        for q in ans:
            if c == '0' or c == '?':
                temp.add((q + r) % n)
            if c == '1' or c == '?':
                temp.add((q - r) % n)
        
        ans = temp
        
    #State: Output State: The set `ans` contains the possible positions of the ball after `m` throws, where each throw can either add or subtract a random value `r` (determined by `func_1()`) from the current player's position, wrapping around using modulo operation with `n`. The value `x` remains unchanged as it is the starting player, and `m` represents the total number of throws. The set `ans` will contain all possible positions the ball could be at after `m` throws, considering both addition and subtraction operations based on the value of `c` returned by `func_1()`.
    if (0 in ans) :
        ans.discard(0)
        ans.add(n)
    #State: The set `ans` contains the possible positions of the ball after `m` throws, where each throw can either add or subtract a random value `r` determined by `func_1()`, and the value `x` remains unchanged as the starting player. If 0 is in `ans`, then `ans` is updated to include `n` added to the possible positions in `ans`, excluding 0. Otherwise, `ans` remains unchanged.
    print(len(ans))
    #This is printed: len(ans) (where len(ans) is the length of the set ans after the described operations)
    print(*sorted(ans))
    #This is printed: sorted elements of ans with 0 removed and n added to the remaining elements (if 0 is in ans)
#Overall this is what the function does:The function processes a series of throws (determined by `func_1()` calls) among `n` players, starting from player `x`. For each throw, it updates the possible positions of the ball based on the distance `r` and direction `c` provided by `func_1()`. After `m` throws, it calculates and prints the number of distinct possible positions the ball could be in, along with these positions sorted and adjusted to exclude 0 and include `n` if 0 is present.

