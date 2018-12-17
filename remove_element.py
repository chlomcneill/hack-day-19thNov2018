def remove_element(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            del nums[i]
        else:
            i += 1
    return len(nums)

print(remove_element([0,1,2,2,3,0,4,2],2)) #5

