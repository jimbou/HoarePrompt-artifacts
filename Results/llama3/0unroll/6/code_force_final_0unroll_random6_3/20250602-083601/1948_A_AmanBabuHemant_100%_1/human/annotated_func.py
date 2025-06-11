#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 ≤ t ≤ 50) and then t integers n (1 ≤ n ≤ 50).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        if n % 2:
            print('NO')
        else:
            s = 'AAB' * (n // 2)
            if len(s) < 200:
                print('YES')
                print(s)
            else:
                print('NO')
        
    #State: The output state is a series of 'YES' or 'NO' responses, followed by a string of 'AAB' repeated n/2 times, for each input integer n. The responses are determined by whether n is even or odd, and whether the length of the string is less than 200. The initial value of t is not changed, and the input integers n are consumed by the loop.

#Overall this is what the function does:This function reads a series of integers from standard input, determines whether each integer is even or odd, and prints 'YES' or 'NO' accordingly. If the integer is even and the length of a string of 'AAB' repeated n/2 times is less than 200, it prints the string; otherwise, it only prints 'NO'. The function processes multiple inputs based on an initial count provided by the user.

