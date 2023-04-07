def defangIPaddr(address: str) -> str:
    newAddress = ''
    for letter in address:
        if letter == '.':
            newAddress = newAddress + '[.]'
        else:
            newAddress = newAddress + letter
    return newAddress
print(defangIPaddr("1.1.1.1"))
print(defangIPaddr("255.100.50.0"))