def singleNumber(nums) -> int:
    x = 0
    used = [-1]
    correct = False
    for num in nums:
        if x + 1 <= len(nums): 
            try :
                nums.index(num,x + 1)
                used.append(num)
            except:
                for e in used:
                    if num == e:
                        correct = False
                        break
                    else:
                        correct = True
            if correct == True:
                return num
        x = x + 1
    return num
print(singleNumber([2,2,1]))
print(singleNumber([4,1,2,1,2]))
print(singleNumber([1]))