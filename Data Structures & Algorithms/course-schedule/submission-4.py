class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i: [] for i in range(numCourses)}
        for crs, prereq in prerequisites:
            premap[crs].append(prereq)
        
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if premap[crs] == []:
                return True
            visiting.add(crs)
            for prereq in premap[crs]:
                if not dfs(prereq):
                    return False
            visiting.remove(crs)
            premap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True