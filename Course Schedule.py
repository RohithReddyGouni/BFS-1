class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        Indegree=[0]*numCourses
        Map=defaultdict(list)
        Que=deque()
        
        for course,requisite in prerequisites:
            Map[requisite].append(course)
            Indegree[course]+=1
        count=0
        for i in range(len(Indegree)):
            if Indegree[i]==0:
                Que.append(i)
        if len(Que)==0:
            return False
        while Que:
            
            value=Que.popleft()
            count+=1
            for i in Map[value]:
                Indegree[i]-=1
                if Indegree[i]==0:
                    Que.append(i)
        return count==numCourses