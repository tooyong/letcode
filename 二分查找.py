class Solution:
    def search(self, nums: list, target: int) -> int:
        head = 0
        tail = len(nums) - 1
        return get_index(head, tail, nums, target)
def get_index(head, tail, nums, target): 
    point = int((tail - head) / 2) + head
    if nums[point] == target:
        #匹配成功
        return point
    else:
        if head >= tail:
            #匹配已经结束
            return -1
        else:
            if nums[point] < target:
                head = point + 1
            else:
                tail = point - 1
            return get_index(head, tail, nums, target)
        
print(Solution().search([ 2 , 5], 2))
