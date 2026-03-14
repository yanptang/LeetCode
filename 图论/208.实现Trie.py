#对比前缀，按照树的逻辑一层一层向下搜索
#你想查 "apple" 和 "apply"。在普通列表里，你要完整比对两个单词；但在 Trie 里，它们共享 "appl" 这条路径，只是在最后一个字符处分叉
#所以插入就是一个字符一个字符插入，插入的时候要注意每一个字典都是一层
#查找的逻辑跟插入一样，找到了就继续下一层，没有找到就返回return，注意子串的验真
class Trie:
    def __init__(self):
        # 使用一个根字典来代表树的顶端
        self.root = {}
    
    #一个字符一个字符插入
    #并且用end来标记结束
    def insert(self, word: str) -> None:
        node = self.root #创建一个根节点
        for char in word:
            #如果当前没有这个字母公共前缀
            #就创建一个新的，并且向下探一层，此刻node为自己新建的字典对象
            if char not in node:
                node[char]={} #
            node=node[char]
        
        # 单词走完后，在当前层打一个特殊的标记，代表这是一个完整的词
        node['end']=True 

    #查找
    #从最初始的一个字符一个字符顺序查找，如果找到end标记，返回True
    def search(self, word: str) -> bool:
        node=self.root 
        for char in word:
            #如果找到了公共前缀就继续
            if char in node:
                node=node[char] 
            else:
                return False
        #如果顺利到达最后一个
        #查看是否有end（因为有可能存apple，查找app，走到了最后但实际不存在
        return 'end' in node

    def startsWith(self, prefix: str) -> bool:
        #共用前缀查询
        #想知道是否有当前的字符串的公共前缀，可以省去重新查询
        node=self.root
        for char in prefix:
            #如果找到了公共前缀就继续
            if char in node:
                node=node[char] 
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)