data = input("Enter 9-bit data that was transmitted: ")
array = [None] * 9
for i in range(0, 9):
    array[i] = int(data[i]) 

def iseven(sum):
    if sum % 2 == 0:
        return 0
    else:
        return 1

sum1 = array[8] + array[6] + array[4] + array[2] + array[0]  
sum2 = array[7] + array[6] + array[3] + array[2]
sum3 = array[5] + array[4] + array[3] + array[2]
sum4 = array[1] + array[0]

e1 = iseven(sum1)
e2 = iseven(sum2)
e3 = iseven(sum3)
e4 = iseven(sum4)

errorbinary = f"{e4}{e3}{e2}{e1}"
errordecimal = int(errorbinary, 2)

print("Array:", array)
print("Error Position (Binary):", errorbinary)
print("Error Position (Decimal):", errordecimal)

if array[9-errordecimal-1]==1:
    array[9-errordecimal-1]=0
else:
    array[9-errordecimal-1]=1
print("Corrected data:", array)   
