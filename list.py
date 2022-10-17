nums = input("Введите данные для отбора: ")
if type(nums)==str:
    nums = list(map(lambda s: int(s), nums.split(",")))
for i in nums:
    if i != 0 and i % 3 == 0:
        print(i)

