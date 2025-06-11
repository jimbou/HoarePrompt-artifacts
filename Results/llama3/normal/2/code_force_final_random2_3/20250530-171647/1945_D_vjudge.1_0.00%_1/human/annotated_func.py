#State of the program right berfore the function call: n and k are positive integers such that 1 <= k <= n <= 200,000, lista_A and lista_B are lists of n positive integers each, representing the values a_i and b_i respectively.
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
        
    #State: The final output state after the loop executes all the iterations is: `n` is greater than or equal to `k`, `k` is a positive integer, `i` is `n - k`, lista_A and lista_B are lists of n positive integers each, stdin contains no input. If lista_A[i] is less than lista_B[i] for all i in the range [0, n - k), then pref is equal to the sum of all elements in lista_A and soma_b is 0. If lista_A[i] is not less than lista_B[i] for all i in the range [0, n - k), then pref is 0 and soma_b is equal to the sum of all elements in lista_B. If there exists at least one i in the range [0, n - k) such that lista_A[i] is less than lista_B[i] and at least one j in the range [0, n - k) such that lista_A[j] is not less than lista_B[j], then pref is equal to the sum of all elements in lista_A that are less than the corresponding elements in lista_B plus the sum of all elements in lista_B that are greater than or equal to the corresponding elements in lista_A, and soma_b is 0.
    resultado = float('inf')
    for i in range(n - k, n):
        resultado = min(resultado, pref + soma_b + lista_A[i])
        
        soma_b += lista_B[i]
        
    #State: n is greater than or equal to k, k is a positive integer, i is n - 1, lista_A and lista_B are lists of n positive integers each, stdin contains no input, pref is either the sum of all elements in lista_A, or 0, or the sum of all elements in lista_A that are less than the corresponding elements in lista_B plus the sum of all elements in lista_B that are greater than or equal to the corresponding elements in lista_A, soma_b is the sum of all elements in lista_B, and resultado is the minimum of its original value and pref + soma_b + lista_A[i].
    print(resultado)
    #This is printed: The minimum value between the original value of resultado and the sum of pref, soma_b, and the last element of lista_A

#Overall this is what the function does:This function calculates the minimum possible sum of a subset of elements from two lists, lista_A and lista_B, based on certain conditions. It takes as input two positive integers, n and k, and two lists of n positive integers each, representing the values a_i and b_i respectively. The function first processes the lists to determine the sum of elements in lista_A that are less than the corresponding elements in lista_B and the sum of elements in lista_B that are greater than or equal to the corresponding elements in lista_A. Then, it calculates the minimum possible sum by considering the last k elements of lista_A and the sum of elements in lista_B. The function returns the minimum possible sum.

#State of the program right berfore the function call: stdin contains an integer representing the number of test cases, followed by an unspecified number of lines of input that will be processed by func_1().
    numero_testes = int(input())
    for _ in range(numero_testes):
        func_1()
        
    #State: `numero_testes` is at least `x + 2`, `func_1()` has been executed `numero_testes` times, `stdin` contains an unspecified number of lines of input that will be processed by `func_1()`.

#Overall this is what the function does:Reads an integer from standard input representing the number of test cases, then executes the function `func_1()` that number of times, processing an unspecified number of lines of input from standard input.

