#State of the program right berfore the function call: stdin contains three inputs: first two integers n and k separated by space and then two lists of integers separated by space. n and k are positive integers such that k <= n, and the two lists have n integers each.
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
        
    #State: n is a positive integer, k is a positive integer such that k <= n, lista_A is a list of n integers in reverse order, lista_B is a list of n integers in reverse order, stdin is empty, i is n - k, pref is the sum of its original value and the sum of all elements in lista_A that are less than the corresponding elements in lista_B, soma_b is the sum of all elements in lista_B that are greater than or equal to the corresponding elements in lista_A.
    resultado = float('inf')
    for i in range(n - k, n):
        resultado = min(resultado, pref + soma_b + lista_A[i])
        
        soma_b += lista_B[i]
        
    #State: n is a positive integer, k is a positive integer such that k <= n, lista_A is a list of n integers in reverse order, lista_B is a list of n integers in reverse order, i is n, pref is the sum of its original value and the sum of all elements in lista_A that are less than the corresponding elements in lista_B, soma_b is the sum of all elements in lista_B that are greater than or equal to the corresponding elements in lista_A plus the sum of all elements in lista_B from index n - k to n, resultado is the minimum of its original value and the sum of pref, soma_b, and the minimum element in lista_A from index n - k to n, stdin is empty.
    print(resultado)
    #This is printed: The minimum of the original value of resultado and the sum of pref, soma_b, and the minimum element in lista_A from index n - k to n

#Overall this is what the function does:This function reads input from stdin, processes two lists of integers, and prints the minimum sum of certain elements. It takes no parameters and returns no value, but instead prints the result. The function's purpose is to find the minimum sum of elements in the second list and the minimum element in the first list, considering certain conditions. The final state of the program is that the input has been processed, and the minimum sum has been printed to the console.

#State of the program right berfore the function call: stdin contains an integer representing the number of test cases, followed by a series of test cases. Each test case consists of two lines: the first line contains two integers n and m separated by spaces, and the second line contains n integers separated by spaces.
    numero_testes = int(input())
    for _ in range(numero_testes):
        func_1()
        
    #State: `numero_testes` is at least 3, and the function `func_1()` has been executed `numero_testes` times.

#Overall this is what the function does:The function reads the number of test cases from standard input, then iterates through each test case, executing the `func_1()` function for each one, without returning any value or modifying the input variables.

