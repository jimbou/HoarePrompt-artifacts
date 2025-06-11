#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains the number of test cases t (1 <= t <= 10^4). Each test case contains two positive integers n, m (1 <= n, m <= 2 * 10^6).
    T = int(input())
    for t in range(T):
        info = input().split()
        
        a, b = int(info[0]), int(info[1])
        
        suma = 0
        
        for i in range(1, b + 1):
            x = (a - i * (i - 1)) // i ** 2 + 1
            if (a - i * (i - 1)) // i ** 2 + 1 > 0:
                suma += x
                if (a - i * (i - 1)) % i ** 2 == 0 and i * (i - 1) % i ** 2 == 0:
                    suma += 1
        
        print(suma - 2)
        
    #State: Output State: The loop will execute T times, and for each execution, it will read two positive integers n and m from stdin, calculate the value of suma based on the given formula, and print the result of suma - 2. After all T executions, the loop will finish, and the program will terminate. The state of T, n, and m will be unchanged, as they are not modified within the loop.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two positive integers n and m. For each test case, it calculates a value 'suma' based on a given formula and prints the result of 'suma - 2'. The function executes this process T times, where T is the number of test cases provided in the input, and then terminates without modifying the input values.

