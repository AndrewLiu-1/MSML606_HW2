# MSML606_HW2

No external sources were used; all ideas are my own or from course lecture slides.

## Problem 4

1. Empty postfix expression edge cases can be seen in ``evaluatePostfix()`` method
In these cases the handled by:
- Checks if exp is None or an empty string
- Checks if the tokens list is empty
- and raises a Value Error if necessary