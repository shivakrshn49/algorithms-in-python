def twoSum(nums, target: int, starting_index=None):
    if not starting_index:
        starting_index = 0
    ending_index = starting_index + 1
    first_element = nums[starting_index]
    try:
        second_element = nums[ending_index]
    except:
        return []
    if first_element + second_element == target:
        return [nums.index(first_element), nums.index(second_element)]
    else:
        return twoSum(nums, target, ending_index)

if __name__ == "__main__":
    print(twoSum([1,3,5,6,8], 11))
