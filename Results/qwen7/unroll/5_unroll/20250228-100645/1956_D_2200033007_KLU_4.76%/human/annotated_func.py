#State of the program right berfore the function call: c is a list of integers where the length of the list n satisfies 1 ≤ n ≤ 18, and each element a_i of the list satisfies 0 ≤ a_i ≤ 10^7.
def func_1(c):
    m = 0
    if (c == 2) :
        print(f'4 1')
        #This is printed: 4 1
        print(f'1 2')
        #This is printed: 1 2
    else :
        print(f'13 0')
        #This is printed: 13 0
    #State: Postcondition: `m` is 0, `c` is a list of integers where the length of the list n satisfies 1 ≤ n ≤ 18, and each element a_i of the list satisfies 0 ≤ a_i ≤ 10^7. The value of `c` is either 2 or not 2.
    return
    #The program does not return any value since there is no return statement in the provided code.
#Overall this is what the function does:The function accepts a list of integers `c` where the length of the list is between 1 and 18 (inclusive), and each element in the list is between 0 and 10^7 (inclusive). It prints one of two messages based on the length of the list: "4 1" if the length is exactly 2, or "13 0" otherwise. After executing the print statements, the function ends without returning any value.

