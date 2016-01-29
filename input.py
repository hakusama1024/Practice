# Enter your code here. Read input from STDIN. Print output to STDOUT

def ValidBST():
    caseSize = int(raw_input())
    testCases = []
    for i in range(caseSize):
        nodeNumber = int(raw_input())
        test = raw_input().split()
        test = map(int, test)
        test = test[:nodeNumber]
        testCases.append(test)
    for i in range(caseSize):
        IsBSTPreorder(testCases[i])

def IsBSTPreorder(test):
    lower = None
    stack = []
    for i in test:
        if lower and i < lower : 
            print "NO"
            return
        while stack and stack[-1] < i:
            lower = stack.pop()
        stack.append(i)
    print "YES"
        
ValidBST()
