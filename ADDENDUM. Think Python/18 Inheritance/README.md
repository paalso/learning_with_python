
Think Python
How to Think Like a Computer Scientist
2nd Edition, Version 2.4.0
[Link](http://cs.williams.edu/~cs134/thinkpython2.pdf)

#####Exercises 18.2 - 18.3

**Exercise 18.2.** Write a Deck method called deal_hands that takes two parameters, the number of hands and the number of cards per hand. It should create the appropriate number of Hand objects, deal the appropriate number of cards per hand, and return a list of Hands.

**Exercise 18.3.** The following are the possible hands in poker, in increasing order of value and decreasing order of probability:

_**pair**_: two cards with the same rank

_**two pair**_: two pairs of cards with the same rank

_**three of a kind**_: three cards with the same rank

_**straight**_: five cards with ranks in sequence (aces can be high or low, so Ace-2-3-4-5 is a straight and so is 10-Jack-Queen-King-Ace, but Queen-King-Ace-2-3 is not.)

_**flush**_: five cards with the same suit

_**full house**_: three cards with one rank, two cards with another

_**four of a kind**_: four cards with the same rank

_**straight flush**_: five cards in sequence (as defined above) and with the same suit

The goal of these exercises is to estimate the probability of drawing these various hands.

1. Download the following files from [http://thinkpython2.com/code](http://thinkpython2.com/code ):

	_Card.py_ : A complete version of the Card, Deck and Hand classes in this chapter.

	_PokerHand.py_ : An incomplete implementation of a class that represents a poker hand, and some code that tests it.

2. If you run PokerHand.py, it deals seven 7-card poker hands and checks to see if any of them contains a flush. Read this code carefully before you go on.

3. Add methods to PokerHand.py named has_pair, has_twopair, etc. that return True or
False according to whether or not the hand meets the relevant criteria. Your code should
work correctly for “hands” that contain any number of cards (although 5 and 7 are the most common sizes).

4. Write a method named classify that figures out the highest-value classification for a hand and sets the label attribute accordingly. For example, a 7-card hand might contain a flush and a pair; it should be labeled “flush”.

5. When you are convinced that your classification methods are working, the next step is to estimate the probabilities of the various hands. Write a function in PokerHand.py that shuffles a deck of cards, divides it into hands, classifies the hands, and counts the number of times various classifications appear.

6. Print a table of the classifications and their probabilities. Run your program with larger and larger numbers of hands until the output values converge to a reasonable degree of accuracy. Compare your results to the values at [http://en.wikipedia.org/wiki/Hand_rankings](http://en.wikipedia.org/wiki/Hand_rankings)

6. Print a table of the classifications and their probabilities. Run your program with larger and larger numbers of hands until the output values converge to a reasonable degree of accuracy. Compare your results to the values at 
[Авторское решение задачи](https://github.com/AllenDowney/ThinkPython2/blob/master/code/PokerHandSoln.py)

#####Version 1.0
Задача решена, но не совсем так, как у автора. В предлагаемом решении классификация комбинаций сделана в соответсвии с авторской спецификацией:

> Write a method named classify that figures out the highest-value classification for a hand and sets the label attribute accordingly. For example, a 7-card hand might contain a flush and a pair; it should be labeled “flush”

т.е. старшая комбинация поглощает младшие, напр. к "Парам" относятся только те комбинации,в к-х есть только одна пара, и ничего более. В решении же, к-е предлагает автор, учитваются все комбинации, к-е можно выбрать в колоде.

