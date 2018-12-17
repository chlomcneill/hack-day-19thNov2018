def remove_duplicates(nums):
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i+1]:
            del nums[i]
        else:
            i += 1
    return len(nums)

print(remove_duplicates([0,0,1,2,3,3,3,4,5,6,6,7])) #8