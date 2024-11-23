def character_count():

    frame=int(input("Enter no. of frames:"))
    final=''

    for i in range(0,frame):
        data=input(f"Enter string {i+1}:")
        char_count=str(len(data)+1)+data
        final+=char_count

    return final


def byte_stuffing():
    
    message=input("Enter the message:")
    start=input("Enter start flag:")
    end=input("Enter end flag:")
    escape=input("Enter the escape character:")
    final=""

    for i in range(0,len(message)):
        if(message[i]==start or message[i]==end):
            final+=escape+message[i]
        else:
            final+=message[i]

    return start+final+end



def bit_stuffing():
    data = list(input("Enter data: "))
    c = 0
    i = 0
    while i < len(data):
        if data[i] == '1':  
            c += 1
        else:
            c = 0 

        if c == 6:
            data.insert(i, '0')             
            c = 0                           
            i += 1                          
        i += 1                              

    return ''.join(data)                    



print("character count:")
transmitted_message_character_count=character_count()
print("transmitted message character count:"+transmitted_message_character_count)


print("byte stuffing:")
transmitted_message_byte_stuffing=byte_stuffing()
print("transmitted message byte stuffing:"+transmitted_message_byte_stuffing)


print("bit stuffing:")
transmitted_message_bit_stuffing=bit_stuffing()
print("transmitted message bit stuffing:"+transmitted_message_bit_stuffing)