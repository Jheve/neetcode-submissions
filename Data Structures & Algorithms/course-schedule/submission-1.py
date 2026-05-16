class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map courses to their prerequisites
        prerequsite_map = {i: [] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            prerequsite_map[course].append(prerequisite)
        
        # keep track of already visited courses 
        visited = set()

        def dfs(course):
            if course in visited:   # cycle detected, return false
                return False
            
            # base case -> no course nor prerequisite
            if prerequsite_map[course] == []:
                return True
            
            visited.add(course)

            for prerequisite in prerequsite_map[course]:
                if not dfs(prerequisite):
                    return False
                
            visited.remove(course)          # backtrack
            prerequsite_map[course] = []    # memoize -> mark as safe

            return True
            
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
        