lose_condition = False
column = ""
for x in range(9):
    nums = input("input your 9 numbers: ")
    if len(nums) != 9:
        print("invalid input!")
        break
    elif nums.isdigit() == False:
        print("invalid input!")
        break
    for ch in nums:
        if nums.count(ch) > 1:
            lose_condition = True
    column += nums[0]
for ch in column:
    if column.count(ch) > 1:
        lose_condition = True
if lose_condition == False:
    print("Yes!!!")
else:
    print("no")
        