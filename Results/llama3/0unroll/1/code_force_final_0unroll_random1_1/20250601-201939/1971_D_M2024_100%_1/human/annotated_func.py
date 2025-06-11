#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t strings, each consisting of characters '0' and '1' with a length between 1 and 500 (inclusive).
    t = int(input())
    for _ in range(t):
        a = input()
        
        cut0 = 0
        
        cut1 = 0
        
        for i in range(len(a) - 1):
            if a[i] == '1' and a[i + 1] == '0':
                cut1 += 1
            if a[i] == '0' and a[i + 1] == '1':
                cut0 += 1
        
        if cut0 == 0:
            print(cut1 + 1)
        else:
            print(cut0 + cut1)
        
    #State: The output state will contain t lines, each containing a single integer. The integer on each line will be the total number of cuts required to make all the characters in the corresponding input string the same, either all '0's or all '1's. The cuts are made by changing a '1' to a '0' or a '0' to a '1'. The number of cuts is calculated by counting the number of transitions from '1' to '0' and from '0' to '1' in the string, and adding 1 if the string starts with a '1' and there are no transitions from '0' to '1'.

#Overall this is what the function does:This function reads an integer t from standard input, followed by t strings consisting of '0' and '1' characters. For each string, it calculates the minimum number of cuts (character changes) required to make all characters the same, either all '0's or all '1's. The function then prints the total number of cuts required for each string, considering transitions from '1' to '0' and '0' to '1', and adding 1 if the string starts with '1' and has no '0' to '1' transitions. The output consists of t lines, each containing a single integer representing the total number of cuts required for the corresponding input string.

