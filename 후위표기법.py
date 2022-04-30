expression = input()
splited = expression.split(' ')

def add(a, b):
    return b+a
def subtract(a,b):
    return b-a
def multiple(a,b):
    return b*a
def divided(a,b):
    return b/a

def calculation(nStack, t):
    a=int(nStack.pop())
    b=int(nStack.pop())
    if t=='+':
        return add(a,b)
    elif t=='-':
        return subtract(a,b)
    elif t=='*':
        return multiple(a,b)
    elif t=='/':
        return divided(a,b)
    
token=['+', '-', '*', '/'] #연산자 문자열
nStack=[]
#만약 연산자면 연산자 stack에 넣기
for s in splited:
    #스택에 집어넣기
    if s.isdigit():
        nStack.append(s)
        #print(nStack)
    else:
        #print(tStack)
        #숫자칸에 2개 이상 있으면 연산 시작
        n=calculation(nStack, s)
        nStack.append(n)
        #print(nStack)

print(nStack[0])