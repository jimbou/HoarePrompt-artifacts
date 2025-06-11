#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t test cases. Each test case consists of an integer n (1 <= n <= 16), a character representing the trump suit ('C', 'D', 'H', or 'S'), and 2n distinct two-character strings representing the cards, where the first character is the rank ('2', '3', '4', '5', '6', '7', '8', or '9') and the second character is the suit ('C', 'D', 'H', or 'S').
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
        
    #State: Output State: trump is the trump suit of the second test case, trumps contains the ranks of the trump cards in the current test case, answers contains the resolved cards for the current test case, and suits is a dictionary with keys 'C', 'D', 'H', 'S' and values None.
    for (suit, rank) in suits.items():
        if rank is None:
            continue
        
        if trumps != []:
            answers.append(f'{rank}{suit} {trumps.pop()}{trump}')
        else:
            print('IMPOSSIBLE')
            return
        
    #State: Output State: trump is the trump suit of the second test case, trumps is an empty list, answers contains the resolved cards for the current test case, and suits is a dictionary with keys 'C', 'D', 'H', 'S' and values None.
    trumps = sorted(trumps)
    while trumps != []:
        print(f'{trumps.pop()}{trump} {trumps.pop()}{trump}')
        
    #State: trumps is an empty list.
    for answer in answers:
        print(answer)
        
    #State: trumps is still an empty list.

#Overall this is what the function does:This function resolves a card game by processing a series of test cases from standard input. It takes no parameters and returns no value. For each test case, it reads the trump suit and a set of cards, then resolves the cards according to the game rules, printing the resolved cards to standard output. If a test case cannot be resolved, it prints 'IMPOSSIBLE' and exits. The function processes all test cases in the input, printing the resolved cards for each case.

