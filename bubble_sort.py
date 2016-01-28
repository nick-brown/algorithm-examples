def bubble_sort(nums):
    for pos in range(len(nums)-1, 0, -1):
        for j in range(pos):
            if nums[j] > nums[j+1]:
               nums[j+1], nums[j] = nums[j], nums[j+1]

    return nums

print bubble_sort([9,37,123,6666,-1,-10000, -362])
print bubble_sort(["david", "roger", "francis", "lucas", "johnathan"])
