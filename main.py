############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
another_card = True

# # def user_cards():
# #   user = random.sample(cards, 2)
# #   print(user)
# #   user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
# #   if sum(user) > 21:
# #     print('Bust')
# #   if user_choice == 'y':
# #     user.append(random.choice(cards))
# #     print(user)
# #   else:

user = random.sample(cards, 2)
dealer = random.sample(cards, 1)

def add_card(player):
  player.append(random.choice(cards))
  return player

def show_cards(show):
  print(f"  Your cards: {user}, current score: {sum(user)}")
  if show == False:
    print(f"  Dealer's first card: {dealer[0]}")
  if show == True:
    print(f"Dealer's final hand: {dealer}, final score: {sum(dealer)}")

#def compare(player1,player2):
  


# # def usr():
# #   if sum(user) < 21:
# #     add_card(user)

# # def dealr():
# #   if sum(dealer) < 17:
# #     add_card(dealer)
    
# def final():
#   print(f"Dealer's final hand: {dealer}, final score: {sum(dealer)}")

# def deal():
#   if sum(add_card(dealer)) < 17:
#     add_card(dealer)

def compare(player1,player2):
  #player1 = sum(player1)
  #player2 = sum(player2)
  if 1 in player1 or 1 in player2:
    if sum(player1) < 21:
      player1.remove(11)
      player1.append(1)
    if sum(player2) < 21:
      player2.remove(1)
      player2.append(11)
    
  if sum(player1) <= 21 and sum(player2) <= 21:
    if sum(player1) < sum(player2):
      print('You lose')
    elif sum(player1) == sum(player2):
      print('Tie')
    elif sum(player1) > sum(player2):
      print('You win')

  if sum(player1) > 21 or sum(player2) > 21:
    if sum(player1) < sum(player2):
      print('You win')
    elif sum(player1) == sum(player2):
      print('Tie')
    elif sum(player1) > sum(player2):
      print('You lose')


def game():
  another_card = True
  while another_card:
    show = False
    show_cards(show)
    user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
    if user_choice == 'y':
      add_card(user)
      if sum(user) > 21:
        while sum(dealer) < 17:
          add_card(dealer)
        show = True
        show_cards(show)
        compare(user, dealer)
        another_card = False
    elif user_choice == 'n':
      while sum(dealer) < 17:
        add_card(dealer)
        show = True
      show_cards(show)
      compare(user, dealer)
      another_card = False

game()


# restart = True
# while restart:
#   starting = input("Would you like to play a game of blackjack?: Type 'y' if yes, 'n' for no: ")
#   if starting == 'y':
#     game()
#   else:
#     restart = False
  


  


  
  

       
   

  

  
   

