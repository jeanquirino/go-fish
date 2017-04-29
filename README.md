# go-fish
[![Build Status](https://travis-ci.com/jeanquirino/go-fish.svg?token=QSCpRppUcxvwf7UfuSsy&branch=master)](https://travis-ci.com/jeanquirino/go-fish)

The classic Go Fish card game via the console.

## Rules
### Players
This game is played with one human and one computer.

### Deck
The standard 52-card pack is used. Some cards are dealt at the beginning of the game and the rest form a stock pile. 

### Objective
The goal is to create the most pairs of cards, with regards to rank. Suits are not important. For example, a queen of hearts and a queen of clubs is a pair and so is a two of spades and a two of hearts.  

#### Rank of Card
A rank is the value that the card has. For example, eight is the rank of the eight of spades, hearts, clubs, and diamonds.  

### To Begin
Seven cards are randomly dealt to each player. Before "fishing" begins, each player shall create all the pairs from their hand. The player with the most initial pairs will begin first. If either players do not have pairs or have the same amount, the human player will be the first to start.

### The Play
On your turn, a prompt will appear asking the player what rank they would like to go "fishing" for. If the other player has the rank that you are "fishing" for, that card will automatically be removed from their hand and given to the other player. The pair will be removed from the hand, and the player's turn ends. If the rank that is asked for is not available, a card will automatically be taken from the stock pile and added to the player's hand. If a pair is made, the pair is removed from the hand. The player's turn ends, regardless of whether they have made a pair or not. This continues until a player has no more cards in their hand. The player with the most pairs at this point wins the game. 