def check_balance(text):
    stack = Stack()
    amount = 0
    error = False
    index = 0
    left = {'(': 1, 
            '{': 2, 
            '[': 3}
            
    right = {')': 1,
             '}': 2,
             ']': 3}
    for c in text:
        if c in left:
            stack.push(c)
        if c in right:
            n = stack.pop()
            if n == None:
                error = True
                break
            if left[n] == right[c]:
                amount += 1
            else:
                error = True
                break
        index += 1
    if stack._size > 0:
        index -= 1
        return f"Match error at position {index}"
    if not error:
        return f"Ok - {amount}"
    if error:
        return f"Match error at position {index}"
                