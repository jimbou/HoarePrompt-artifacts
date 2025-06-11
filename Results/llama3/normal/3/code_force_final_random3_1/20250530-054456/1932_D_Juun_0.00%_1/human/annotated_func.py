#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 100) followed by t test cases. Each test case consists of three lines: the first line contains an integer n (1 ≤ n ≤ 16), the second line contains a single character (one of "CDHS"), and the third line contains 2n two-character strings (each string consists of a character from "23456789" followed by a character from "CDHS"). All 2n strings are different.
    input()
    trump = input()
    trumps = []
    answers = []
    suits = {'C': None, 'D': None, 'H': None, 'S': None}
    for card in input().split():
        rank, suit = card
        
        if suit == trump:
            trumps.append(rank)
        elif suits[suit] is not None:
            answers.append(' '.join([(x + suit) for x in sorted([suits[suit], rank])]))
            suits[suit] = None
        else:
            suits[suit] = rank
        
    #State: stdin contains 0 test cases, trump is a single character (one of "CDHS"), trumps is a list containing the ranks of all cards in the input().split() if the suit of any card is equal to trump, answers is a list with elements that are strings containing the rank and suit of each card, separated by a space, and sorted alphabetically if the suit of the card is not equal to trump, suits is a dictionary with keys 'C', 'D', 'H', 'S' and all values are None.
    for (suit, rank) in suits.items():
        if rank is None:
            continue
        
        if trumps != []:
            answers.append(f'{rank}{suit} {trumps.pop()}{trump}')
        else:
            print('IMPOSSIBLE')
            return
        
    #State: stdin contains 0 test cases, trump is a single character (one of "CDHS"), trumps is an empty list, answers is a list with elements that are strings containing the rank and suit of each card, separated by a space, and sorted alphabetically if the suit of the card is not equal to trump, with additional elements that are strings containing the rank and suit of each card, followed by the popped rank from trumps and the trump suit, suits is a dictionary with keys 'C', 'D', 'H', 'S' and all values are None, suit is 'S'.
    trumps = sorted(trumps)
    while trumps != []:
        print(f'{trumps.pop()}{trump} {trumps.pop()}{trump}')
        
    #State: trumps is an empty list, answers is a list with elements that are strings containing the rank and suit of each card, separated by a space, and sorted alphabetically if the suit of the card is not equal to trump, with additional elements that are strings containing the rank and suit of each card, followed by the popped rank from trumps and the trump suit, and all possible combinations of two ranks from trumps followed by trump are printed.
    for answer in answers:
        print(answer)
        
    #State: `trumps` is an empty list, `answers` is a list with elements that are strings containing the rank and suit of each card, separated by a space, and sorted alphabetically if the suit of the card is not equal to trump, with additional elements that are strings containing the rank and suit of each card, followed by the popped rank from trumps and the trump suit, and all possible combinations of two ranks from trumps followed by trump are printed, and must have at least as many elements as the number of iterations of the loop, `answer` is the last element in the list, and the last element of the list `answers` which is `answer` is being printed.

#Overall this is what the function does:This function processes a set of test cases from standard input, where each test case consists of a number of cards with ranks and suits. It then prints out all possible combinations of two cards, where the suits are either the same or one is a trump suit. If there are not enough trumps to pair with all non-trump cards, it prints 'IMPOSSIBLE'. The function does not return any value, but instead prints the results directly to the console.

