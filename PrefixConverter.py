from pickletools import stackslice
from turtle import st


class PrefixConverter:
    def __init__(self):
        self.stackList = []
    
    def push(self,data):
        self.stackList.append(data)

    def peek(self):
        if self.stackList:
            return self.stackList[-1]
        else:
            return "Isi Stack Kosong"
    
    def pop(self):
        if self.stackList:
            data = self.stackList.pop(-1)
            return data
        else:
            return "Isi Stack Kosong"
    
    def cekValidExpression(self,expression):
        if '(' in expression:
            return True
    def infixToPrefix(self,expression):
        expression = expression[::-1]
        exp = []
        for i in expression:
            if i == '-':
                self.push(i)
            elif i == '/':
                self.push(i)
            elif i == '*' and self.peek() == '/':
                exp.append(self.peek())
                self.pop()
                self.push(i)
            elif i == '+' and self.peek() == '*' or i == '+' and self.peek() =='-':
                exp.append(self.peek())
                self.pop()
                self.push(i)
            #elif i == '+' and self.peek() == '+':
            #    exp.append(self.peek())
            #    self.pop()
            #    self.push(i)
            else:
                exp.append(i)
            print(self.stackList)
        if len(self.stackList) !=0:
            for i in range(len(self.stackList)-1,-1,-1):
                print(i)
        print(self.stackList)

        return ''.join(exp[::-1])

x = PrefixConverter()
print(x.infixToPrefix("1+2+3*4/2-1"))

        
        
