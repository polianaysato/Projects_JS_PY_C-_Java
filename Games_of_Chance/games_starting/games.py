import random

money = 100


def flip_coins(bet, heads_or_tails):
    """
    Parameters: integer (bet) and string (head or tail)
    Description: method will generate a random head or tail result and it'll compare with the argument passed by the user. 
                 It implements ways for preventing the user to pass invalid bets or guesses.
    Return: a positive or negative integer bet, based on if the user has scored or not.

    """
    flip = random.randint(1,2)
    result_aux = ['head', 'tail']
    if flip == 1:
        result = result_aux[0]
    else:
        result = result_aux[1]
    print("The result was " + result)
    guess = heads_or_tails.lower()
    
    if not guess in result_aux or bet <= 0:
        print("You've entered an invalid guess or bet. Please make sure you've passed 'head' or 'tail' and a bet greater than 0!")
        return 0  
    elif result == guess and bet > 0:
        bet = str(bet)
        print("Your guess was " + guess + ". You won $" + bet)
        return int(bet)
    
    elif result != guess  and bet > 0:
        print("Your guess was " + guess + ". You lost $" + str(bet))
        bet = int(bet)
        return bet * (-1)

def cho_han(bet, odd_or_even):
    """
    Parameters: integer (bet) and string (odd or even)
    Description: method will generate dices' results randomly and it'll compare with the argument passed by the user. 
                 It implements ways for preventing the user to pass invalid bets or guesses.
    Return: a positive or negative integer bet, based on if the user has scored or not.

    """
    dice_1 = random.randint(1,6)
    print("Dice one result was: " + str(dice_1))
    dice_2 = random.randint(1,6)
    print("Dice two result was: " + str(dice_2))
    modulo_aux = ['even', 'odd']
    modulo = ''
    if (dice_1 + dice_2) % 2 == 0:
        modulo = modulo_aux[0]
    else:
        modulo = modulo_aux[1]
    
    guess = odd_or_even.lower()
    
    if not guess in modulo_aux or bet <= 0:
        print("You've entered an invalid guess or bet. Please, make sure you pass 'even' or 'odd' and a value greater than 0!")
        return 0
    elif guess == modulo:
        print("The result was " + modulo + ". You've earned $" + str(bet))
        return bet
    else:
        print("The result was " + modulo + ". You've lost $" + str(bet))
        return bet * (-1)


def pick_cards(bet):
    """
    Parameters: integer (bet) 
    Description: method will randomly choose a card from a list and it'll compare with the card assigned randomly to the user.
                 It compares one another card based on the higher index on the list.
                 It implements ways for preventing the user to pass invalid bets.
    Return: a positive or negative integer bet, based on if the user has scored or not.
    """
    cards = ['ace', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king' ]
    cards_aux = []
    
    card = cards[random.randint(0, (len(cards)-1))]
    random_card = cards[random.randint(0, (len(cards)-1))]
    
    if bet <= 0:
        print("You've entered an invalid bet. Please make sure you've passed a bet greater than 0!")
        return 0
    
    if not card in cards_aux:
        cards_aux.append(card)
    
    if not random_card in cards_aux:
        random_card = random_card
    else:
        random_card = cards[random.randint(0, len(cards))]
    
    if cards.index(random_card) < cards.index(card):
        print("You've got " + str(card) + ". The system's got " + str(random_card) + ". You've earned $" + str(bet))
        return bet
    elif cards.index(random_card) == cards.index(card):
        print("You've got " + str(card) + ". The system's got " + str(random_card) + ". You've earned $ 0")
        return 0
    else:
        print("You've got " + str(card) + ". The system's got " + str(random_card) + ". You've lost $ " + str(bet * (-1)))
        return bet * (-1)


def roulette(bet, guess):
    """
    Parameters: integer (bet) and string or integer (guess)
    Description: method will generate a random result in a range 0 to 37. The user can pass 'odd', 'even' or a number in a range 1 to 36.
                 It implements ways for preventing the user to pass invalid bets or guesses.
    Return: a positive or negative integer bet, based on if the user has scored or not.
    """
    random_number = random.randint(0,37)
    print("The result was: " + str(random_number))
    wheel_result = ['even', 'odd']
    for x in range(1,37):
        wheel_result.append(x)
        
    if guess.__class__ == 'string':
        guess = guess.lower()
        
    if not guess in wheel_result or bet <= 0:
        print("You've entered an invalid guess or bet. Please make sure you've passed 'even', 'odd' or a number between 1 and 36. Also, pass a bet greater than 0!")
        return 0
    else:
        if random_number == 0 or random_number == 37:
            print("Wheel landed on 0 or 00!")
            return 0
        else:
            if guess == 'even' and random_number % 2 == 0:
                print("You've guessed even.")
                print("You've earned $" + str(bet))
                return bet
            elif guess == 'odd' and random_number % 2 != 0:
                print("You've guessed odd.")
                print("You've earned $" + str(bet))
                return bet
            elif guess == random_number:
                print("Your guess was " + str(guess) + " and the results was " + str(random_number) + ". You've earned $" + str(bet * 35))
                return bet * 35
            else:
                print("You've guessed " + str(guess))
                print("You've lost $" + str(bet*(-1)))
                return bet * (-1)




# calling the flip_coins() function with an invalid argument
money += flip_coins(50, 'TAIL!')
print(money)

money += flip_coins(50, 'HEAD')
print(money)

# calling the cho_han() function with an invalid argument
money += cho_han(50, 'ODD!')
print(money)

money += cho_han(50, 'even')
print(money)

money += pick_cards(50)
print(money)

# calling the pick_card() function with an invalid argument
money += pick_cards(-50)
print(money)

money += roulette(50, 'even')
print(money)

money += roulette(50, 'odd')
print(money)

# calling the pick_card() function with an invalid argument
money += roulette(50, 'odd*&')
print(money)

# calling the pick_card() function with an integer guess instead of a string
money += roulette(50, 23)
print(money)
