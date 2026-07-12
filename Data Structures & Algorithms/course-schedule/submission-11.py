class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        prereq_for = defaultdict(list)
        for crs, prereq in prerequisites:
            indegree[crs] +=1
            prereq_for[prereq].append(crs)

        q = deque([i for i in range(numCourses) if indegree[i]==0])
        taken_courses = set()
        while q:
            crs = q.popleft()
            taken_courses.add(crs)
            for other_course in prereq_for[crs]:
                indegree[other_course]-=1
                if indegree[other_course] == 0:
                    q.append(other_course)

        return len(taken_courses) == numCourses

        


# prereq [a,b] = take "b" first
# step 1: insert all indegree = 0 courses to queue then while loop on q
#   step 2: pop from stack, reduce indegree of nodes pointed to by current node