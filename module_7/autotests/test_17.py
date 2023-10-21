lst = []
def encode(data):
    num = 0
    if not data:
        return []
    else:
        for i in data:
            if i == data[0]:
                print(num)
                num += 1
            else:
                lst.append(data[0])
                lst.append(num)
                return [data[0], num] + encode(data[num:])

print(encode(["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z" ]))
    

    