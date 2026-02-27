#思路：hash表可以降低时间复杂度
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={} #值做key，index作value
        for i in range(len(nums)):
            cur_value=target-nums[i]
            if cur_value in hashmap:
                return [i,hashmap[cur_value]]
            hashmap[nums[i]]=i  #把当前的值存到key-value作为键值对
