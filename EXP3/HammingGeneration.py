#5 bit data aaya toh 4 parity le lena baaki same karo aage
array = [None] * 7
data = input("Enter 4-bit data to send: ")

if len(data) != 4:
    print("Error")
else:
    array[0] = int(data[0])#position D7
    array[1] = int(data[1])#position D6  
    array[2] = int(data[2])#position D5
    array[4] = int(data[3])#position D3

    def iseven(sum):
        if sum % 2 == 0:
            return 0
        else:
            return 1

    sum1 = array[0] + array[2] + array[4]
    sum2 = array[1] + array[2] + array[4]
    sum3 = array[0] + array[1] + array[2]

    p1 = iseven(sum1)
    p2 = iseven(sum2)
    p3 = iseven(sum3)

    array[6] = p1
    array[5] = p2
    array[3] = p3

    result = ''.join(map(str, array))
    print(result)
