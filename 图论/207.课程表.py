from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #prerequisites 提供了所有的课程连接关系
        #通过此列表构建有向图
        
        #解法
        #1.先找不需要前置课程的课->可上课的队列
        #2.上一门没有要求的课，看是否解锁了其他课程
        #3.解锁的课程的入度减一，如果变成了一个入度为0的课程，那么就放到可上的队列
        #统计最后自己一共队列里存在过多少课程


        #000 构建表
        indegree=[0]*numCourses
        adjacency=[[] for _ in range(numCourses)] 

        for cur,pre in prerequisites:
            indegree[cur]+=1           #下标表示该课程，值表示需要完成的前置课程
            adjacency[pre].append(cur) #下标为index-表示前置课程，对应行的数字表示其能解锁的课程
        
        #先寻找所有可以上课的
        queue = deque()               # 1. 先创建一个空的双端队列
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i) 

        count=0

        #解锁过程
        while queue:
            pre = queue.popleft() #上一门课
            count+=1
            for cur in adjacency[pre]: #上了这门课所有可以解锁的课程->cur
                indegree[cur]-=1 #对应的解锁课程-1

                if indegree[cur]==0: #如果这门课程已经完全解锁
                    queue.append(cur) 



        return count==numCourses
