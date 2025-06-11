#State of the program right berfore the function call: n and k are positive integers such that k <= n <= 200000, lista_A is a list of n positive integers, lista_B is a list of n positive integers.
    n, k = map(int, input().split())
    lista_A = list(map(int, input().split()))
    lista_A.reverse()
    lista_B = list(map(int, input().split()))
    lista_B.reverse()
    soma_b = 0
    pref = 0
    for i in range(n - k):
        if lista_A[i] < lista_B[i]:
            pref += soma_b
            pref += lista_A[i]
            soma_b = 0
        else:
            soma_b += lista_B[i]
        
    #State: Output State: pref is the sum of the first n-k elements of lista_A and the sum of the elements of lista_B that are greater than the corresponding elements in lista_A, soma_b is 0, and the rest of the variables remain unchanged.
    resultado = float('inf')
    for i in range(n - k, n):
        resultado = min(resultado, pref + soma_b + lista_A[i])
        
        soma_b += lista_B[i]
        
    #State: Output State: `pref` is the sum of the first n-k elements of lista_A and the sum of the elements of lista_B that are greater than the corresponding elements in lista_A, `soma_b` is the sum of the last k elements of lista_B, `resultado` is the minimum value between the initial value of `resultado` and the sum of `pref`, `soma_b`, and each of the last k elements of lista_A, and the rest of the variables remain unchanged.
    print(resultado)
    #This is printed: minimum value between the initial value of resultado and the sum of pref, soma_b, and each of the last k elements of lista_A

#Overall this is what the function does:This function calculates the minimum value that can be obtained by summing the first n-k elements of lista_A, the sum of the elements of lista_B that are greater than the corresponding elements in lista_A, and one of the last k elements of lista_A. It takes as input two positive integers n and k, and two lists of n positive integers lista_A and lista_B, and returns the minimum value.

#State of the program right berfore the function call: stdin contains an integer (number of test cases) followed by 3 lines for each test case: two integers (n and m) and two lists of integers (a and b) separated by spaces. The integer is a positive integer, n and m are positive integers such that 1 <= m <= n <= 200,000, and the lists a and b contain n positive integers each.
    numero_testes = int(input())
    for _ in range(numero_testes):
        func_1()
        
    #State: The loop will execute `numero_testes` times, and for each iteration, it will call the function `func_1()` without passing any arguments. The state of the variables `numero_testes`, `n`, `m`, `a`, and `b` will remain unchanged, as they are not modified within the loop. The output state will be the same as the initial state, with the only difference being that the function `func_1()` will have been called `numero_testes` times.

#Overall this is what the function does:The function reads an integer from standard input, representing the number of test cases, and then iterates that many times, calling another function (`func_1`) without passing any arguments. The function does not modify the input variables or produce any output; its sole purpose is to execute `func_1` a specified number of times based on the input.

