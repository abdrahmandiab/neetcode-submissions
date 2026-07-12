class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        prereq_for = defaultdict(list)
        for crs, prereq in prerequisites:
            indegree[crs]+=1
            prereq_for[prereq].append(crs)
        
        q = deque([i for i in range(numCourses) if indegree[i]==0])
        order = []
        consumed = set()
        while q:
            node = q.popleft()
            order.append(node)
            consumed.add(node)
            for crs in prereq_for[node]:
                indegree[crs]-=1
                if indegree[crs] == 0:
                    q.append(crs)
        return order if len(consumed )==numCourses else []
