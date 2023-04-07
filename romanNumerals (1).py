
def romanToInt(s: str) -> int:
    total = 0
    num = 0
    index = -1
    if len(s) <= 15 and len(s) >= 1:
        for letter in s:
            if letter == 'I':
                total = total + 1
            if letter == 'V':
                total = total + 1
            if letter == 'X':
                total = total + 1
            if letter == 'L':
                total = total + 1
            if letter == 'C':
                total = total + 1
            if letter == 'D':
                total = total + 1
            if letter == 'M':
                total = total + 1
            if total == len(s):
                for letter in s:
                    index = index + 1
                    if letter == 'I':
                        if s.find('V', index + 1, index + 2) != -1:
                            num = num - 1
                        elif s.find('X', index + 1, index + 2) != -1:
                            num = num - 1
                        else:
                            num = num + 1
                    if letter == 'V':
                        num = num + 5
                    if letter == 'X':
                        if s.find('L', index + 1, index + 2) != -1:
                            num = num - 10
                        elif s.find('C', index + 1, index + 2) != -1:
                            num = num - 10
                        else:
                            num = num + 10
                    if letter == 'L':
                        num = num + 50
                    if letter == 'C':
                        if s.find('D', index + 1, index + 2) != -1:
                            num = num - 100
                        elif s.find('M', index + 1, index + 2) != -1:
                            num = num - 100
                        else:
                            num = num + 100
                    if letter == 'D':
                        num = num + 500
                    if letter == "M":
                        num = num + 1000
                
    return num
print(romanToInt('III'))
print(romanToInt('LVIII'))
print(romanToInt('MCMXCIV'))