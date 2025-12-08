#数字栈记重复次数，字符串栈记之前的内容；遇 "[" 入栈状态，遇 "]" 弹栈构造字符串。
class Solution:
    def decodeString(self, s: str) -> str:
    #从左到右扫描，遇到左括号，说明即将遇到的内容将会首先重复，先把之前的内容存起来之后碰到}再用--压栈
    #遇到右括号，说明当前登记的状态首先应该出来了
    #数字里的栈顶元素，总是对当前状态的string有效，因为存在k[STRING]结构
    #同时要把登记的string移到当前状态string，因为下一个数字栈顶将会对之前登记的string有效

        numberStack=[]
        strStack=[]
        curNumer=0
        curString=""

        for c in s:
            if c.isdigit():
                curNumer=curNumer * 10 + int(c)
            elif c=="[": #左边括号出现，需要存储括号之前的状态
                numberStack.append(curNumer)
                strStack.append(curString)
                curNumer=0
                curString=""
            #右括号出现，需要构造字符串，从上一次压栈到这一次碰到的都要构造，使用压栈前的k
            elif c=="]":
                repeat=numberStack.pop()
                curString=strStack.pop()+curString*repeat
            else:
                curString+=c 
        return curString