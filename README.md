# MSML606_HW2

No external sources were used; all ideas are my own or from course lecture slides.

## Problem 4

### 1. Empty postfix expression 
These edge cases can be seen in ``evaluatePostfix()`` method
In these cases the handled by:
- Checks if exp is None or an empty string
- Checks if the tokens list is empty
- and raises a ``ValueError`` if necessary

### 2. Malformed Expressions
Checked by ensuring exactly two operands are available for every operator and exactly one result remains in the stack.

Insuffecient Operands
- Seen in ``evaluatePostfix()``
- Handling Process: Checks if ``stack.size()`` < 2 before popping out 2 operands and raises a ``ValueError`` if insuffecient opperands

Too many Operands
- Handling Process: Checks if stack.size() != 1.

### 3. Division by zero
These edge cases are handled by an explicit zero-check before the division operation in the evaluator.
- Can be seen in ``evaluatePostfix()`` - when operator is '/'
- explicitly checks if operand2 == 0 before division
- raises ZeroDivisionError if necessary

### 4. Invalid Tokens
Filters out non-numeric operands that arent supported operators
- Seen in ``evaluatePostfix()`` when parsing operands
- handled by using try/except around int(token) conversion and if the token is not a valid operator (cannot be converted), then a ValueError is raised

### 5. Very Large Numbers
Handled by Python - ``int`` type has no fixed size limit - operations on large number function correctly

### 6. Negative Numbers in the Expression
- Seen again in ``evaluatePostfix()`` during operand parsing
- handled fine through python as it correclt yparses negative numbers -> strings are still able to be converted and aritmetic operations still work correctly