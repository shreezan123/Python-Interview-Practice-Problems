def balancedparenthesis(s):
    if len(s) %2 != 0:
        return False
    openingset = {'(','[','{'}
    pairedset = {('(',')'),('[',']'),('{','}')}
    stack = [] #using list as a stack
    for paren in s:
        if paren in openingset: #if opening parenthesis, then append, if no opening then we can conclude that no closing parenthesis
            stack.append(paren)
        else:
            if len(stack) == 0: #we conclude that there is no matching opening parenthesis for the closing one
                return False
            poppedparen = stack.pop() #now our stack only has the closing parenthesis
            if (poppedparen, paren) not in pairedset:
                return False
    return len(stack) ==0
