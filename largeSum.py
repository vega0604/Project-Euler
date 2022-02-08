with open('nums.txt', 'r') as f:
    nums = [int(x) for x in f.readlines()]


print(str(sum(nums))[:10])