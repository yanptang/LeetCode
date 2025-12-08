class MinStack:

    def __init__(self):
        self.stack=[] #表示构造的时候，为对象创造一个stack属性，每一个对象都有一个独立的变量
        self.min=[]

    def push(self, val: int) -> None:
        #表示对象调用push方法的时候，对对象的stack属性操作，因为stack是对象固有的属性，所以要用到self
        #不是本函数里定义的属性，而是属于当前对象的，对于对象的方法和属性的调用都要使用self
        #否则每个对象都要调用push方法，那么究竟对谁做改变呢？答案是当前调用的对象本身，也即self
        self.stack.append(val) 

        #维护一个最小元素栈，否则不可能只有o1复杂度
        if not self.min:
            self.min.append(val)
        else:
            self.min.append(min(val, self.min[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()