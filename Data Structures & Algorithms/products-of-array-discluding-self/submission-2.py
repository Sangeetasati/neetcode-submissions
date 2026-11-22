class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix =[1]*len(nums)
        suffix =[1]*len(nums)
        res = []
        for i in range(len(nums)):
            if i == 0:
                prefix[0]= nums[i]
            else:
                prefix[i] = prefix[i-1] * nums[i]


        for j in range(len(nums)-1, -1, -1):
            if j == len(nums)-1:
                suffix[j]= nums[j]
            else:
                suffix[j] = suffix[j+1] * nums[j]


        res = []
        for x in range(len(nums)):
            if x == 0:
                res.append(1*suffix[x+1])
            elif x == len(nums)-1:
                res.append(prefix[x-1]*1)
            else:
                res.append(prefix[x-1] * suffix[x+1])

        return res



