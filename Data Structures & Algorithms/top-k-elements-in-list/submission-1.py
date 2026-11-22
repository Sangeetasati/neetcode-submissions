class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = [ [] for s in range(len(nums)+1)]

        
        for key, value in count.items():
            arr[value].append(key)

        res = []
        for i in range(len(arr)-1, 0, -1):
            for j in range(len(arr[i])):
                res.append(arr[i][j])
                if len(res)==k:
                    return res
        








        