class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        t = [-1,-1,-1]
        new_trips = []
        for trip in triplets:
            if trip == target:
                return True
            if (trip[0] <= target[0] and trip[1] <= target[1] and trip[2] <= target[2]):
                new_trips.append(trip)
        
        for trip in new_trips:
            t = self.maxer(t,trip)
            if t == target:
                return True
        return False


    def maxer(self,trip1,trip2):
        return [max(trip1[0],trip2[0]),max(trip1[1],trip2[1]),max(trip1[2],trip2[2])]