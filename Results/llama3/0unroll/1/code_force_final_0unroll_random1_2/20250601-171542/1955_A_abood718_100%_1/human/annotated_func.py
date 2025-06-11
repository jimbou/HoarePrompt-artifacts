#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t (1 <= t <= 10^4), then t sets of three integers n, a, and b (1 <= n <= 100, 1 <= a, b <= 30).
    for i in range(int(input())):
        A, B, C = map(int, input().split())
        
        if B * 2 < C:
            print(A * B)
        elif A % 2 == 0:
            print(int(A * C / 2))
        else:
            X = A // 2
            print(X * C + B)
        
    #State: The output state will be a list of t integers, each representing the result of the calculation for the corresponding set of inputs. The calculation is based on the conditions specified in the loop body. If B is less than half of C, the result is A times B. If A is even, the result is A times C divided by 2. Otherwise, the result is X times C plus B, where X is A divided by 2.

#Overall this is what the function does:Calculates and prints the result of a mathematical operation for each set of three input integers, based on specific conditions. The operation is either multiplication of the first two integers, multiplication of the first and third integers divided by 2, or a combination of multiplication and addition involving the first and third integers, depending on the values of the input integers. The function processes multiple sets of inputs and prints the corresponding results.

