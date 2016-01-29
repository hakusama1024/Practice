def Read():
    stack_main = []
    opNumber = int(raw_input())
    for i in range(opNumber):
        op = raw_input().split()
        if len(op) == 1:
            pop(stack_main)
        elif len(op) == 2:
            push(stack_main, int(op[1]))
        elif len(op) == 3:
            Inc(stack_main, int(op[1]), int(op[2]))
def pop(stack):
    if stack:
        stack.pop()
        if stack:
            print stack[-1]
            return
    print "EMPTY"
   
def push(stack, ele):
    stack.append(ele)
    print ele
    
def Inc(stack, x, d):
    if not stack :
        print "EMPTY"
        return
    tmp = []
    while stack:
        tmp.append(stack.pop())
    while x and tmp:
        stack.append(tmp.pop() + d)
        x -= 1
    while tmp:
        stack.append(tmp.pop())
    print stack[-1]
    
Read()
