#State of the program right berfore the function call: stdin contains one or more test cases. Each test case consists of three lines. The first line contains an integer n (1 <= n <= 16). The second line contains a single character, the trump suit, which is one of "CDHS". The third line contains a space-separated list of 2n cards. Each card is described by a two-character string, the first character is the rank of the card, which is one of "23456789", and the second one is the suit of the card, which is one of "CDHS". All cards are different.
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
        
    #State: Output State: trump is a single character, one of "CDHS". trumps is a list of one or more characters. answers is a list of one or more strings. suits is a dictionary with keys 'C', 'D', 'H', 'S' and all values are None.
    for (suit, rank) in suits.items():
        if rank is None:
            continue
        
        if trumps != []:
            answers.append(f'{rank}{suit} {trumps.pop()}{trump}')
        else:
            print('IMPOSSIBLE')
            return
        
    #State: Output State: trump is a single character, one of "CDHS". trumps is an empty list. answers is a list of one or more strings. suits is a dictionary with keys 'C', 'D', 'H', 'S' and all values are not None.
    trumps = sorted(trumps, reverse=True)
    while trumps != []:
        print(f'{trumps.pop()}{trump} {trumps.pop()}{trump}')
        
    #State: trump is a single character, one of "CDHS", trumps is an empty list, answers is a list of one or more strings, suits is a dictionary with keys 'C', 'D', 'H', 'S' and all values are not None.
    for answer in answers:
        print(answer)
        
    #State: Output State: trump is a single character, one of "CDHS", trumps is an empty list, answers is an empty list, suits is a dictionary with keys 'C', 'D', 'H', 'S' and all values are not None.

#Overall this is what the function does:The function processes a series of test cases from standard input, where each test case consists of three lines: an integer n, a trump suit, and a list of 2n cards. It then generates a list of answers based on the cards and the trump suit, and prints out the answers in a specific format. If it's impossible to generate answers, it prints 'IMPOSSIBLE' and returns. The function does not return any value, but instead prints out the results directly.

