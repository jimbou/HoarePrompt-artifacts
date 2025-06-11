#State of the program right berfore the function call: stdin contains one or more lines of input. Each line contains two positive integers n and k, separated by a space, such that 1 <= n <= 26 and 1 <= k <= 26.
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        s = ''
        
        for j in range(97, k + 97):
            s += chr(j)
        
        if k == 1:
            print(n * s)
        else:
            print((2 - (n == 1)) * s)
        
    #State: The output state will be a series of strings, each consisting of a sequence of lowercase letters, repeated a certain number of times. The sequence of letters will start from 'a' and go up to the k-th letter of the alphabet (where k is the second number in each input line). If k is 1, the sequence will be repeated n times. If k is greater than 1, the sequence will be repeated twice if n is greater than 1, and once if n is 1. The number of strings in the output will be equal to the value of t.

#Overall this is what the function does:This function reads input from stdin, where each line contains two positive integers n and k, and generates a series of strings based on these inputs. For each input line, it creates a sequence of lowercase letters from 'a' to the k-th letter of the alphabet, and repeats this sequence a certain number of times: n times if k is 1, and twice if n is greater than 1 and k is greater than 1, or once if n is 1 and k is greater than 1. The function then prints these strings to the output, with the number of strings equal to the value of t, which is read from the input before the loop.

