# Enter your code here. Read input from STDIN. Print output to STDOUT
def Read():
    stack_main = []
    output = []
    opNumber = int(raw_input())
    for i in range(opNumber):
        op = raw_input().split()
        if len(op) == 1 and op[0] == "pop":
            pop(stack_main, output)
        elif len(op) == 2 and op[0] == "push":
            push(stack_main,output, int(op[1]))
        elif len(op) == 3 and op[0] == "inc":
            Inc(stack_main,output, int(op[1]), int(op[2]))
    for i in output:
        print i
def pop(stack, output):
    if stack:
        stack.pop()
        if stack:
            output.append(str(stack[-1]))
            return
    output.append("EMPTY")
    return
   
def push(stack, output, ele):
    stack.append(ele)
    output.append(str(ele))
    return
    
def Inc(stack, output, x, d):
    for i in range(x):
        stack[i]+=d
    output.append(str(stack[-1]))
    return
Read()
