nums = [int(line.strip()) for line in open('input.txt', 'r')]
nums.sort()

dic = {1: 1, 2: 0, 3: 1}

for i in range(len(nums)-1):
    last, this = nums[i], nums[i+1]

    dic[this-last] += 1

print(dic[1] * dic[3])
