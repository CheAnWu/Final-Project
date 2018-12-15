# Title: 
Monte Carlo Stimulation for Blackjack

## Team Member(s):
Che-An Wu
Xue Lu

# Monte Carlo Simulation Scenario & Purpose:
Find the strategy based on player and dealer's cards.

## Simulation's variables of uncertainty
Each time a card is drawn from the cardpool randomly to the dealer or a player. The player's hand, dealer's hand are the variables of interest that are uncertain. The probability distribution of player and dealer's hand is to be calculated.

Since we simulate a 6-deck situation which the number of cards is large, it is not significant that the previous card has an influence to the next card. Each hand has a range from 2-22(or the game ends), and the probability distribution of each card is close to a uniform distribution. We think it represents the reality well.

## Hypothesis or hypotheses before running the simulation:
Player's options: Hit/Stand/Split
Input: Stand point, dec

## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)
One can play 21 jack using our strategy based on his hand and the one card of dealer that is showing. We also include a pdf strategy report based on our findings in this repository.

## Instructions on how to use the program:
We similate a single game with the function 'Game' and then run it for every standpoint we set for 1,000,000 times. Results are put in csv files and are analyzed using pandas and jupyter which are also uploaded to this repository.

## All Sources Used:
We compare our strategy to this:
https://wizardofodds.com/games/blackjack/strategy/4-decks/
