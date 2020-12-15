for part in [2020,30000000]:
    nums, one = { e:i+1 for i,e in enumerate([19,0,5,1,10,13]) }, 19
    for turn in range(7, part):
        nums[one], one = turn, 0 if one not in nums else turn-nums[one]
    print(one)
