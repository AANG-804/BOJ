nums = input().split()
result = {}
max_ = -1
for num in nums:
    if result.get(int(num)) == None:
        result[int(num)] = 1
    else:
        result[int(num)] += 1

    if max_ < int(num):
        max_ = int(num)

rep = max(list(result.values()))

if rep == 3:
    i = list(result.keys())[list(result.values()).index(3)]
    print(10000+1000*i)
elif rep == 2:
    i = list(result.keys())[list(result.values()).index(2)]
    print(1000+100*i)
else:
    print(max_*100)
