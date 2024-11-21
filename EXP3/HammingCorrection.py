data = input("Enter 7-bit data that was transmitted: ")
array = [None] * 7
for i in range(0, 7):
    array[i] = int(data[i]) 

def iseven(sum):
    if sum % 2 == 0:
        return 0
    else:
        return 1

sum1 = array[6] + array[4] + array[2] + array[0]
sum2 = array[5] + array[4] + array[2] + array[1]
sum3 = array[3] + array[2] + array[1] + array[0]

e1 = iseven(sum1)
e2 = iseven(sum2)
e3 = iseven(sum3)

errorbinary = f"{e3}{e2}{e1}"
errordecimal = int(errorbinary, 2)

print("Array:", array)
print("Error Position (Binary):", errorbinary)
print("Error Position (Decimal):", errordecimal)

if array[7-errordecimal]==1:
    array[7-errordecimal]=0
else:
    array[7-errordecimal]=1
print("Corrected data:", array)   
