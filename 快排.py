def f_sort(nums):
    #升序排序
    do_search(nums=nums, head=0, tail=len(nums) - 1)
    #print(nums)

def do_search(nums, head, tail):
    #返回当前字符被调整后坐标
    if head >= tail:
        return
    point = l_search(nums, head, tail)
    #print('do_search next', head, tail, point, nums[head:point], nums[point + 1:tail+1])
    do_search(nums=nums, head=head, tail=point - 1)
    do_search(nums=nums, head=point + 1, tail=tail)

def l_search(nums, head, tail):
    #target_point:标识上一次调换的位置
    #target_value：标识需要排序的值
    #--->>>
    
    target_point = head
    target_value = nums[head]
    left = True
    
    #print('search start----------------------------', target_point, target_value, head, tail, nums[head:tail+1])
    while(head <= tail):
        if left:
            if target_value > nums[tail]:
                nums[target_point] = nums[tail]
                target_point = tail
                left = False
                #<<<---
            tail -= 1
        else:
            # >>>----
            if target_value < nums[head]:
                nums[target_point] = nums[head]
                target_point = head
                left = True
            head += 1
    nums[target_point] = target_value
    #print('search done', target_point, target_value, nums)
    return target_point
