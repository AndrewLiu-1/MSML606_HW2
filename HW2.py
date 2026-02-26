# Andrew Liu - MSML606 HW2
import csv
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class HomeWork2:

    # Problem 1: Construct an expression tree (Binary Tree) from a postfix expression
    # input -> list of strings (e.g., [3,4,+,2,*])
    # this is parsed from p1_construct_tree.csv (check it out for clarification)

    # there are no duplicate numeric values in the input
    # support basic operators: +, -, *, /

    # output -> the root node of the expression tree. Here: [*,+,2,3,4,None,None]
    # Tree Node with * as root node, the tree should be as follows
    #         *
    #        / \
    #       +   2
    #      / \
    #     3   4

    def constructBinaryTree(self, input) -> TreeNode:
        # Edge case -> empty input
        if not input or len(input) == 0:
            return None
        
        # Define the set of basic support operators
        operators = {'+', '-', '*', '/'}
        
        # Stack that holds the TreeNode references
        stack = []
        
        for token in input:
            if token in operators:
                # Token is an operator: pop two operands and create subtree
                # Edge case: less than 2 nodes on stack
                if len(stack) < 2:
                    raise ValueError(f"Malformed expression: insufficient operands for operator '{token}'")
                
                # Pop right child first (stack is LIFO), then left child
                right_node = stack.pop()
                left_node = stack.pop()
                
                # Create new operator node with children
                operator_node = TreeNode(val=token, left=left_node, right=right_node)
                
                # Push the subtree root back onto stack
                stack.append(operator_node)
            else:
                # Token is an operand: create leaf node
                # We keep the value as string to match output format
                operand_node = TreeNode(val=token)
                stack.append(operand_node)
        
        # Edge case: too many operands
        if len(stack) != 1:
            raise ValueError(f"Malformed expression: {len(stack)} items left on stack (expected 1)")
        
        # Returns the root of the constructed tree
        return stack.pop()



    # Problem 2.1: Use pre-order traversal (root, left, right) to generate prefix notation
    # return an array of elements of a prefix expression
    # expected output for the tree from problem 1 is [*,+,3,4,2]
    # you can see the examples in p2_traversals.csv

    def prefixNotationPrint(self, head: TreeNode) -> list:
        result = []
        
        def preorder(node):
            # Checks for best case: if node is None, return
            if node is None:
                return
            
            # Pre-order: Root -> Left -> Right
            # visit root
            result.append(node.val)
            # Traverse left subtree
            preorder(node.left)
            # Traverse right subtree
            preorder(node.right)
        
        preorder(head)
        return result

    # Problem 2.2: Use in-order traversal (left, root, right) for infix notation with appropriate parentheses.
    # return an array of elements of an infix expression
    # expected output for the tree from problem 1 is [(,(,3,+,4,),*,2,)]
    # you can see the examples in p2_traversals.csv

    # don't forget to add parentheses to maintain correct sequence
    # even the outermost expression should be wrapped
    # treat parentheses as individual elements in the returned list (see output)

    def infixNotationPrint(self, head: TreeNode) -> list:
        result = []
        operators = {'+', '-', '*', '/'}
        
        def inorder(node):
            # Checks again for best case: if node is None, return
            if node is None:
                return
            
            # Check if current node is an operator (internal node)
            is_operator = node.val in operators
            
            # Addsa opening parenthesis for operator nodes
            if is_operator:
                result.append('(')
            
            # In-order: Left -> Root -> Right
            inorder(node.left)        # Traverse left subtree
            result.append(node.val)   # Visit root
            inorder(node.right)       # Traverse right subtree
            
            # Add closing parenthesis for operator nodes
            if is_operator:
                result.append(')')
        
        inorder(head)
        return result


    # Problem 2.3: Use post-order traversal (left, right, root) to generate postfix notation.
    # return an array of elements of a postfix expression
    # expected output for the tree from problem 1 is [3,4,+,2,*]
    # you can see the examples in p2_traversals.csv

    def postfixNotationPrint(self, head: TreeNode) -> list:
        result = []
        
        def postorder(node):
            # Base case: if node is None, return 
            if node is None:
                return
            
            # Post-order: Left -> Right -> Root
            postorder(node.left)      # Traverse left subtree
            postorder(node.right)     # Traverse right subtree
            result.append(node.val)   # Visit root
        
        postorder(head)
        return result


class Stack:
    # Implement your stack using either an array or a list
    # (i.e., implement the functions based on the Stack ADT we covered in class)
    # You may use Python's list structure as the underlying storage.
    # While you can use .append() to add elements, please ensure the implementation strictly follows the logic we discussed in class
    # (e.g., manually managing the "top" of the stack
    
    # Use your own stack implementation to solve problem 3

    def __init__(self):
        # Initialize the underlying list for storage
        self._data = []
        self._top = -1

    def push(self, item):
        """
        Pushes an item onto the top of the stack.
        Time Complexity: O(1) amortized
        """
        self._top += 1
        # Use append to add element
        if self._top < len(self._data):
            self._data[self._top] = item
        else:
            self._data.append(item)

    def pop(self):
        """
        Remove and return the item at the top of the stack.
        Raises IndexError if stack is empty.
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Stack is empty - cannot pop")
        item = self._data[self._top]
        self._top -= 1
        return item

    def peek(self):
        """
        Return the item at the top of the stack without removing it.
        Raises IndexError if stack is empty.
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Stack is empty - cannot peek")
        return self._data[self._top]

    def is_empty(self):
        """
        Check if the stack is empty.
        Time Complexity: O(1)
        """
        return self._top == -1

    def size(self):
        """
        Return the number of elements in the stack.
        Time Complexity: O(1)
        """
        return self._top + 1

    # Problem 3: Write code to evaluate a postfix expression using stack and return the integer value
    # Use stack which you implemented above for this problem

    # input -> a postfix expression string. E.g.: "5 1 2 + 4 * + 3 -"
    # see the examples of test entries in p3_eval_postfix.csv
    # output -> integer value after evaluating the string. Here: 14

    # integers are positive and negative
    # support basic operators: +, -, *, /
    # handle division by zero appropriately

    # DO NOT USE EVAL function for evaluating the expression

    def evaluatePostfix(self, exp: str) -> int:
        # Edge case: empty expression
        if not exp or exp.strip() == "":
            raise ValueError("Empty expression")
        
        # Define valid operators
        operators = {'+', '-', '*', '/'}
        
        # Split expression to get tokens
        tokens = exp.split()
        
        # Edge case: no tokens
        if len(tokens) == 0:
            raise ValueError("Empty expression after parsing")
        
        for token in tokens:
            if token in operators:
                # Edge case: need at least 2 operands on stack
                if self.size() < 2:
                    raise ValueError(f"Malformed expression: insufficient operands for operator '{token}'")
                
                # Pop operands
                operand2 = self.pop()  # top of stack
                operand1 = self.pop()
                
                # Perform the operation
                if token == '+':
                    result = operand1 + operand2
                elif token == '-':
                    result = operand1 - operand2
                elif token == '*':
                    result = operand1 * operand2
                elif token == '/':
                    # Edge case: Division by zero
                    if operand2 == 0:
                        raise ZeroDivisionError("Division by zero")
                    result = int(operand1 / operand2)
                
                # Push result back to stack
                self.push(result)
            else:
                # Token should be an number
                try:
                    # Edge case: negative numbers
                    # Edge case: very large numbers
                    operand = int(token)
                    self.push(operand)
                except ValueError:
                    # Edge case: invalid token (no  number or operator)
                    raise ValueError(f"Invalid token: '{token}' is not a valid number or operator")
        
        # Edge case: malformed expression -> too many operands
        if self.size() != 1:
            raise ValueError(f"Malformed expression: {self.size()} values left on stack (expected 1)")
        
        return self.pop()


# Main Function. Do not edit the code below
if __name__ == "__main__":
    homework2 = HomeWork2()

    print("\nRUNNING TEST CASES FOR PROBLEM 1")
    testcases = []
    try:
        with open('p1_construct_tree.csv', 'r') as f:
            testcases = list(csv.reader(f))
    except FileNotFoundError:
        print("p1_construct_tree.csv not found")

    for i, (postfix_input,) in enumerate(testcases, 1):
        postfix = postfix_input.split(",")

        root = homework2.constructBinaryTree(postfix)
        output = homework2.postfixNotationPrint(root)

        assert output == postfix, f"P1 Test {i} failed: tree structure incorrect"
        print(f"P1 Test {i} passed")

    print("\nRUNNING TEST CASES FOR PROBLEM 2")
    testcases = []
    with open('p2_traversals.csv', 'r') as f:
        testcases = list(csv.reader(f))

    for i, row in enumerate(testcases, 1):
        postfix_input, exp_pre, exp_in, exp_post = row
        postfix = postfix_input.split(",")

        root = homework2.constructBinaryTree(postfix)

        assert homework2.prefixNotationPrint(root) == exp_pre.split(","), f"P2-{i} prefix failed"
        assert homework2.infixNotationPrint(root) == exp_in.split(","), f"P2-{i} infix failed"
        assert homework2.postfixNotationPrint(root) == exp_post.split(","), f"P2-{i} postfix failed"

        print(f"P2 Test {i} passed")

    print("\nRUNNING TEST CASES FOR PROBLEM 3")
    testcases = []
    try:
        with open('p3_eval_postfix.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                testcases.append(row)
    except FileNotFoundError:
        print("p3_eval_postfix.csv not found")

    for idx, row in enumerate(testcases, start=1):
        expr, expected = row

        try:
            s = Stack()
            result = s.evaluatePostfix(expr)
            if expected == "DIVZERO":
                print(f"Test {idx} failed (expected division by zero)")
            else:
                expected = int(expected)
                assert result == expected, f"Test {idx} failed: {result} != {expected}"
                print(f"Test case {idx} passed")

        except ZeroDivisionError:
            assert expected == "DIVZERO", f"Test {idx} unexpected division by zero"
            print(f"Test case {idx} passed (division by zero handled)")