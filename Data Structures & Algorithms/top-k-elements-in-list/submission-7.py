class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        output = []
        for num in nums:
            freq[num] +=1

        for key, value in freq.items():
            if len(output) < k:
                output.append(key)
            else:
                min_key = min(output, key=lambda x: freq[x])
                if value > freq[min_key]:
                    output[output.index(min_key)] = key
        return output