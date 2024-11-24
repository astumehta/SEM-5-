def xor(a,b):
    c=[]
    for i,j in zip(a,b):
        if (i=='1' and j=='0' or i=='0' and j=='1'):
            c.append('1')
        else:
            c.append('0')
    return c

def division(divisor,dividend):
    n=len(divisor)
    quotient=[]
    current=dividend[:n]
    for i in range(len(dividend)-n+1):
        if(current[0]=='1'):
            quotient.append('1')
            current=xor(divisor,current)
        else:
            quotient.append('0')
            current=xor(['0']*n,current)
        if i+n<len(dividend):
            current.append(dividend[i+n])
        current=current[1:]
    remainder=current
    return quotient,remainder

def encode(data,divisor):
    n=len(divisor)-1
    padded_data=data+['0']*n
    quotient,remainder=division(divisor,padded_data)
    transmitted_data=data+remainder
    return transmitted_data

def decode(received_data,divisor):
    quotient,remainder=division(divisor,received_data)
    if all(bit=='0' for bit in remainder):
        print("right message received")
    else:
        print("wrong message is received")
        print(f"remainder{''.join(remainder)}")

def crc():
    data=list(input("enter the data in binary: "))
    divisor=list(input("enter the divisor: ").lstrip('0'))

    transmitted_data=encode(data,divisor)
    print(f"the transmitted data is: {''.join(transmitted_data)}")

    received_data=list(input("enter the received data: "))
    decode(received_data,divisor)

crc() 
