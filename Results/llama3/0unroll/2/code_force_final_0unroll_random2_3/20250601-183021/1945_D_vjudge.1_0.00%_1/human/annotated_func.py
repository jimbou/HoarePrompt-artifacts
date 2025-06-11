#State of the program right berfore the function call: stdin contains three inputs: first two integers separated by a space, then a space-separated list of integers, and then another space-separated list of integers. The first integer is a positive integer, the second integer is a positive integer and less or equal than the first integer. The two lists of integers have the same length as the first integer and contain positive integers.
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
        
    #State: Output State: n is a positive integer, k is a positive integer and less or equal than n, lista_A is a list of positive integers in reverse order, lista_B is a list of positive integers in reverse order, soma_b is the sum of the elements of lista_B from index n-k to n-1, pref is the sum of the elements of lista_A from index 0 to n-k-1 plus the sum of the elements of lista_B from index 0 to n-k-1 that are greater than the corresponding elements in lista_A, stdin is empty
    resultado = float('inf')
    for i in range(n - k, n):
        resultado = min(resultado, pref + soma_b + lista_A[i])
        
        soma_b += lista_B[i]
        
    #State: Output State: `resultado` is the minimum value between the initial value of `resultado` and the sum of `pref`, `soma_b` and the smallest element in `lista_A` from index `n-k` to `n-1`, `soma_b` is the sum of all elements in `lista_B`, `n`, `k`, `lista_A`, `lista_B`, `pref` and stdin remain unchanged.
    print(resultado)
    #This is printed: the minimum value between the initial value of resultado and the sum of pref, soma_b, and the smallest element in lista_A from index n-k to n-1

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the minimum value between the initial value of `resultado` and the sum of `pref`, `soma_b`, and the smallest element in `lista_A` from index `n-k` to `n-1`. It takes no arguments and returns no value, but instead prints the result to the console. The function assumes that the input is well-formed and does not perform any error checking.

#State of the program right berfore the function call: stdin contains an integer representing the number of test cases.
    numero_testes = int(input())
    for _ in range(numero_testes):
        func_1()
        
    #State: Output State: `numero_testes` is 0, stdin is empty.

#Overall this is what the function does:Reads an integer from standard input representing the number of test cases, then calls another function (`func_1`) for each test case, leaving the input stream empty and the test case counter at 0 after execution.

