# 1_figures

## Task

[The code](https://raw.githubusercontent.com/polytech-lectures-python/lecture-6-oop/refs/heads/master/1_basics/inheritance_and_polymorphism.py) from lecture 6 does not conform to the [Liskov substitution principle](https://en.wikipedia.org/wiki/Liskov_substitution_principle).
Change the code to support the principle.

## Changes

There is only a single problem with the code provided.
When you change the width of an instance of Square class, the height doesn't change.
The width of a square is always equal to it's height.

I used `property` decorator to make width conform to height when object is a square.

