#State of the program right berfore the function call: stdin contains multiple sets of inputs: the first line contains an integer, the second line contains two integers n and k such that 1 <= k <= n <= 200000, the third line contains n integers, and the fourth line contains n integers.
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
        
    #State: Output State: The output state after the loop executes all the iterations is as follows: n remains unchanged, k remains unchanged, lista_A remains unchanged, lista_B remains unchanged, stdin remains unchanged, pref is the sum of all elements in lista_A from index 0 to n-k-1 plus the sum of all elements in lista_B from index 0 to n-k-1, and soma_b is the sum of all elements in lista_B from index n-k to n-1.
    resultado = float('inf')
    for i in range(n - k, n):
        resultado = min(resultado, pref + soma_b + lista_A[i])
        
        soma_b += lista_B[i]
        
    #State: Output State: The variable resultado is assigned the minimum value between the current value of resultado and the sum of pref, soma_b, and the current element of lista_A. The variable soma_b is updated by adding the current element of lista_B.
    print(resultado)
    #This is printed: minimum value between the current value of resultado and the sum of pref, soma_b, and the current element of lista_A

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the minimum sum of elements from two lists. It takes no parameters and returns no value, but instead prints the result. The function reads four lines of input: an integer, two integers n and k, and two lists of n integers each. It then calculates the sum of elements from the first list and the sum of elements from the second list, considering the constraint k. Finally, it prints the minimum sum of elements from the two lists, considering all possible combinations.

#State of the program right berfore the function call: stdin contains an integer (greater than 0) representing the number of test cases.
    numero_testes = int(input())
    for _ in range(numero_testes):
        func_1()
        
    #State: Output State: `numero_testes` is an integer equal to 0, stdin contains no input.

#Overall this is what the function does:The function reads an integer from standard input representing the number of test cases, then calls another function (`func_1`) for each test case. After all test cases have been processed, the function leaves the standard input empty and the number of test cases is set to 0.

