#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 676) followed by t lines, each containing two integers n (1 ≤ n ≤ 26) and k (1 ≤ k ≤ 26).
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        print('abcdefghijklmnopqrstuvwxyz'[:k] * n)
        
    #State: `t` is an integer between 1 and 676, `i` is `t-1`, `n` is an integer between 1 and 26, `k` is an integer between 1 and 26, stdin contains `t-t` lines, each containing two integers `n` (1 ≤ `n` ≤ 26) and `k` (1 ≤ `k` ≤ 26), and the string 'abcdefghijklmnopqrstuvwxyz' sliced up to the kth character repeated n times is being printed, and this is printed: 'abcdefghijklmnopqrstuvwxyz' sliced up to the kth character repeated n times, where n is an integer between 1 and 26, and k is an integer between 1 and 26, and 'abcdefghijklmnopqrstuvwxyz' sliced up to the kth character repeated n times is being printed, and this is printed: 'abcdefghijklmnopqrstuvwxyz' sliced up to the kth character repeated n times, where n is an integer between 1 and 26, and k is an integer between 1 and 26, and ... (t times)

#Overall this is what the function does:The function reads an integer t from standard input, followed by t lines, each containing two integers n and k. It then prints the string 'abcdefghijklmnopqrstuvwxyz' sliced up to the kth character repeated n times for each line. The function does not return any value, but instead prints the results directly to the console.

