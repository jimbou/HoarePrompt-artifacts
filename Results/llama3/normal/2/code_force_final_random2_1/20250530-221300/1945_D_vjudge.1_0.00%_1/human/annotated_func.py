#State of the program right berfore the function call: stdin contains three inputs: first two integers n and k separated by a space, then a space-separated list of n integers and then another space-separated list of n integers. The integer n is a positive integer and k is a positive integer such that 1 <= k <= n.
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
        
    #State: n is a positive integer, k is a positive integer such that 1 <= k <= n, lista_A is a list of n integers in reverse order, lista_B is a list of n integers in reverse order, stdin is empty, i is equal to n - k, pref is the sum of all elements in lista_A that are less than the corresponding elements in lista_B plus the sum of all elements in lista_B that are greater than or equal to the corresponding elements in lista_A up to the (n-k)th iteration, soma_b is 0.
    resultado = float('inf')
    for i in range(n - k, n):
        resultado = min(resultado, pref + soma_b + lista_A[i])
        
        soma_b += lista_B[i]
        
    #State: n is a positive integer, k is a positive integer greater than 0, lista_A is a list of n integers in reverse order, lista_B is a list of n integers in reverse order, stdin is empty, i is equal to n, pref is the sum of all elements in lista_A that are less than the corresponding elements in lista_B plus the sum of all elements in lista_B that are greater than or equal to the corresponding elements in lista_A up to the (n-k)th iteration, soma_b is the sum of all elements in lista_B from the (n-k)th to the nth iteration, resultado is the minimum of its original value and pref + soma_b + the sum of all elements in lista_A from the (n-k)th to the nth iteration.
    print(resultado)
    #This is printed: minimum of the original value of resultado and pref + soma_b + the sum of all elements in lista_A from the (n-k)th to the nth iteration

#Overall this is what the function does:This function reads input from stdin, processes two lists of integers, and prints the minimum sum of certain elements. It takes no arguments and returns no value, but instead prints the result to the console. The function's purpose is to find the minimum sum of elements in the lists based on certain conditions, and it achieves this by iterating through the lists, comparing elements, and updating the sum accordingly. The final state of the program is that the minimum sum is printed to the console, and the input lists are processed and discarded.

#State of the program right berfore the function call: stdin contains an integer followed by multiple sets of input data. Each set of input data contains two lines: the first line contains two integers n and m (1 <= m <= n <= 200,000), and the second line contains n integers a_1, a_2, ..., a_n separated by spaces (1 <= a_i <= 10^9). The third line contains n integers b_1, b_2, ..., b_n separated by spaces (1 <= b_i <= 10^9).
    numero_testes = int(input())
    for _ in range(numero_testes):
        func_1()
        
    #State: `numero_testes` is greater than or equal to 0 and the function `func_1()` has been executed `numero_testes` times.

#Overall this is what the function does:Reads a specified number of test cases from standard input, where each test case consists of two lines of integers, and executes a function (`func_1`) for each test case, without returning any value or modifying the input data.

