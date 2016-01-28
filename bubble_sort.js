function bubbleSort(nums) {
    for(var x = nums.length - 1; x > 0; x--) {
        for(var j = 0; j < x; j++) {
            if(nums[j] > nums[j+1]) {
                temp = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = temp
            }
        }
    }

    return nums;
}

console.log(bubbleSort([9,37,123,6666,-1,-10000, -362]));
console.log(bubbleSort(["david", "roger", "francis", "lucas", "johnathan"]));
