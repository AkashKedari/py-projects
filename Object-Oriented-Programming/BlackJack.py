 # Akash Kedari, Object Oriented Programming Section 1 , November 16th, 2020
# Assignment 6 - Problem 3 - extra credit blackjack game


import random 


cards = ['10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts', '6 of Hearts', '5 of Hearts', '4 of Hearts',
 '3 of Hearts', '2 of Hearts', 'Ace of Hearts', 'King of Hearts', 'Queen of Hearts', 'Jack of Hearts', 
 '10 of Diamonds', '9 of Diamonds', '8 of Diamonds', '7 of Diamonds', '6 of Diamonds', '5 of Diamonds', 
 '4 of Diamonds', '3 of Diamonds', '2 of Diamonds', 'Ace of Diamonds', 'King of Diamonds', 'Queen of Diamonds', 
 'Jack of Diamonds', '10 of Clubs', '9 of Clubs', '8 of Clubs', '7 of Clubs', '6 of Clubs', '5 of Clubs', 
 '4 of Clubs', '3 of Clubs', '2 of Clubs', 'Ace of Clubs', 'King of Clubs', 'Queen of Clubs', 'Jack of Clubs',
  '10 of Spades', '9 of Spades', '8 of Spades', '7 of Spades', '6 of Spades', '5 of Spades', '4 of Spades', 
  '3 of Spades', '2 of Spades', 'Ace of Spades', 'King of Spades', 'Queen of Spades', 'Jack of Spades']

values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10,
          10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10]

# Take the initial length of the original list
cards_len = len(cards)-1
# Set two enpty lists to hold player_hand and the value of the players 
player_hand = []
player_hand_value = []
# Make two copies of the card, value lists for the player. 
# These lists will be modified for the remove functions 
# Jk, im not using the remove function, I just figured out another way to do the "removing" by using "in"
player_cards_list = cards[:]
player_values_cards_list = values[:]


# Deal two random cards
for i in range(0, 2):
    rand_card = random.randint(0, cards_len)
    # Choose rand number and access that index value and append it into the player hand list.
    # Check to see if the card is already in your list
    # if the rand_card is in your player hand, the choose another card
    # if it is not in your list, then break and print out your list
    while True:
        if player_cards_list[rand_card] in player_hand:
            rand_card = random.randint(0, cards_len)
            continue
        else:
            player_hand.append(player_cards_list[rand_card])
            player_hand_value.append(player_values_cards_list[rand_card])
            break


value_player_hand = 0
for index in player_hand_value:
    value_player_hand += index

print("Players hand is: ", player_hand, player_hand_value,
      "The value of players current hand is:", value_player_hand)



# hitting or standing mechanic
while True:

    hit = input("Do you want to (h)it or (s)tand?  (h or s) : ")

    if hit == 'h':
        rand_card = random.randint(0, cards_len)

        # Same contingecy as above. 
        # check to see if the card is already in the players hand, and if it is, then choose another card
        # If it is not, add the cards/value, keep track of the card your drew and break this while loop
        while True:
            if player_cards_list[rand_card] in player_hand:
                rand_card = random.randint(0, cards_len)
                continue
            else:
                player_hand.append(player_cards_list[rand_card])
                player_hand_value.append(player_values_cards_list[rand_card])
                # Keep track of the card you drew
                player_card_drew = player_cards_list[rand_card]
                break

        print("You drew the card", player_card_drew)
        # Recalculate value 
        value_player_hand = 0
        for index in player_hand_value:
            value_player_hand += index

        if value_player_hand > 21:
            print("Players hand is: ", player_hand, player_hand_value,
                  "The value of players current hand is:", value_player_hand)
            print("Oh No! You busted! ")
            break

        if player_hand_value == 21:
            print("You got a blackjack!")
            print("Players hand is: ", player_hand, player_hand_value,
                  "The value of players current hand is:", value_player_hand)
            break

        print("Players hand is: ", player_hand, player_hand_value,
              "The value of players current hand is:", value_player_hand)
        continue
    else:
        print("You chose to stand...")
        print("Players hand is: ", player_hand, player_hand_value,
      "The value of players current hand is:", value_player_hand) 
        break
print()
print("----------------------------------------------------------------------------")
print()
########################################################################################
# Computer is playing below 

# Empty lists to hold computer cards and thier respective values 
computer_hand = []
computer_hand_value = []

# Deal the computer two random cards for the first turn. 
for i in range(0, 2):
    # Choose rand number and access that index value and append it into the computer hand list
    rand_card = random.randint(0, cards_len)
    # Check to see if the card is already in your list
    # if the rand_card is in your computers hand, the choose another card
    # if it is not in your list, add the cards/values in,  then break and print out your list
    while True:
        if cards[rand_card] in computer_hand:
            rand_card = random.randint(0, cards_len)
            continue
        else:
            computer_hand.append(cards[rand_card])
            computer_hand_value.append(values[rand_card])
            break


value_computer_hand = 0 
for index in computer_hand_value:
    value_computer_hand += index 

print("Computers hand is: ", computer_hand, computer_hand_value,
      "The value of computers current hand is:", value_computer_hand)

while (value_computer_hand < value_player_hand) and (value_computer_hand < 21):

    rand_card = random.randint(0, cards_len)

    while True:
        if cards[rand_card] in computer_hand:
            rand_card = random.randint(0, cards_len)
            continue
        else:
            computer_hand.append(cards[rand_card])
            computer_hand_value.append(values[rand_card])
            computer_card_drew = cards[rand_card]
            break

    print("Computer drew the card:",computer_card_drew)

    value_computer_hand = 0
    for index in computer_hand_value:
        value_computer_hand += index

    if value_computer_hand == 21:
        print("Computers hand is: ", computer_hand, computer_hand_value,
              "The value of computers current hand is:", value_computer_hand)
        break

    if value_computer_hand > 21:
        print("Computer busted!")

    print("Computers hand is: ", computer_hand, computer_hand_value,
          "The value of computers current hand is:", value_computer_hand)


if (value_computer_hand < value_player_hand) and (value_computer_hand <=21):
    print("computer wins!")
elif (value_computer_hand < value_player_hand):
    print("computer wins!")

if (value_player_hand < value_computer_hand) and (value_player_hand <=21):
    print("Player wins!")
elif (value_player_hand < value_computer_hand):
    print("Player wins!")

if value_computer_hand == value_player_hand:
    print("Tie game!")
