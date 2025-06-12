#State of the program right berfore the function call: stdin contains a sequence of inputs: first an integer t (1 <= t <= 10^4), then t pairs of inputs. Each pair consists of an integer n (1 <= n <= 10) and a string s of length n containing only 'W' and 'B' characters, with at least one 'B' character.
    n = int(input())
    for i in range(n):
        t = int(input())
        
        x = list(input())
        
        if 'B' in x:
            start = x.index('B')
            end = len(x) - x[::-1].index('B') - 1
            print(end - start)
        else:
            print(0)
        
    #State: n is an integer between 1 and 10^4 (inclusive), i is n-1, t is an integer, x is a string of length n containing only 'W' and 'B' characters with at least one 'B' character, stdin is empty.

#Overall this is what the function does:This function reads a sequence of inputs from stdin, where the first input is an integer t, followed by t pairs of inputs. Each pair consists of an integer n and a string s of length n containing only 'W' and 'B' characters. The function then calculates and prints the length of the substring containing only 'B' characters for each pair, or 0 if no 'B' characters are found. The function processes all input pairs and leaves stdin empty.

