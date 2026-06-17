class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs, prereq in prerequisites:
            preMap[crs].append(prereq)
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True
            
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True








# Below approach doesn't work since it only checks for 1 length distances
# hashset = defaultdict(list)
#         for course, prereq in prerequisites:
#             if course in hashset[prereq]:
#                 return False
#             hashset[course].append(prereq)
#         return True 