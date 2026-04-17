class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers sorted in non-decreasing i.e. ascending with duplicates
        # index1 != index2
        # numbers[index1] + numbers[index2] = target
        # O(1) space
        n = len(numbers)
        for i in range(n):
            for j in range(i+1,n,1):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
                elif numbers[i] + numbers[j] > target:
                    break
        return [-1,-1]
        
        