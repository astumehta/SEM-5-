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
    msg=input("Enter data to be sent")
    c=0
    final=''
    for i in msg:
        if(i=='1'):
            c+=1
        else:
            c=0
        final+=i
        if(c==5):
            final+='0'
            c=0
    print(final)                    



print("character c:")
transmitted_message_character_count=character_count()
print("transmitted message character c:"+transmitted_message_character_count)


print("byte stuffing:")
transmitted_message_byte_stuffing=byte_stuffing()
print("transmitted message byte stuffing:"+transmitted_message_byte_stuffing)


print("bit stuffing:")
transmitted_message_bit_stuffing=bit_stuffing()
print("transmitted message bit stuffing:"+transmitted_message_bit_stuffing)