
def check_parentheses(string):
    stack = []
    for char in string:
        # wrong character, stop
        if char not in '()':
            return False
        # when opening, add to stack
        elif char == '(':
            # push operation
            stack.append(char)
        # when closing, check if there is anything in the stack
        # i.e. is there a corresponding opening ?
        elif char == ')':
            if not stack:
                return False
            # remove opening from stack using pop
            stack.pop()
    return not stack

my_par = '(()()(()))()'
print(check_parentheses(my_par))