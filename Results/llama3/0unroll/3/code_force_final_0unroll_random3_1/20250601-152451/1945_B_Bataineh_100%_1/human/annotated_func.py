#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t sets of three space-separated integers a, b, m (1 <= a, b, m <= 10^18).
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a and m < b:
            print(2)
        elif m < a and m > b:
            print(2 + m // b)
        elif m < b and m > a:
            print(2 + m // a)
        else:
            print(m // a + m // b + 2)
        
    #State: The output state will be a series of integers, each representing the minimum number of operations required to make 'a' and 'b' equal to 'm' for each set of inputs. The number of integers in the output state will be equal to 't', the number of sets of inputs.

#Overall this is what the function does:This function reads a series of input sets from standard input, where each set contains three integers: a, b, and m. It then calculates and prints the minimum number of operations required to make 'a' and 'b' equal to 'm' for each set of inputs. The number of operations is determined based on the relative values of a, b, and m, and the function handles all possible cases. The function outputs a series of integers, each representing the minimum number of operations required for each input set.

