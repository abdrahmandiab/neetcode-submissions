class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {i: [] for i in range(numCourses)}
        for crs, prereq in prerequisites:
            premap[crs].append(prereq)
        
        processed, visiting =set(), set()
        res = []

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in processed:
                return True

            visiting.add(crs)
            for prereq in premap[crs]:
                if not dfs(prereq):
                    return False
            visiting.remove(crs)
            processed.add(crs)
            res.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res