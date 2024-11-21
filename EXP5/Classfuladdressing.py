ip = input("Enter IP address: ")
iplist = ip.split(".")

if len(iplist) != 4:
    print("ERROR IN IP")
else:
    firstoctet=int(iplist[0])
    if (firstoctet>=0 and firstoctet<=127):
        print("Class: A")
        print("Subnet mask: 255.0.0.0")
        iplist[1]=iplist[2]=iplist[3]="0"
        modified_ip = ".".join(iplist)
        print("Subnet address: ", modified_ip)
    elif (firstoctet>=128 and firstoctet<=191):
        print("Class: B")
        print("Subnet mask: 255.255.0.0")
        iplist[2]=iplist[3]="0"
        modified_ip = ".".join(iplist)
        print("Subnet address: ", modified_ip)
    elif (firstoctet>=192 and firstoctet<=223):
        print("Class: C")
        print("Subnet mask: 255.255.255.0")
        iplist[3]="0"
        modified_ip = ".".join(iplist)
        print("Subnet address: ", modified_ip)
    elif (firstoctet>=224 and firstoctet<=239):
        print("Class: D")
        print("Subnet mask: Multicast")
    elif (firstoctet>=240 and firstoctet<=255):
        print("Class: E")
        print("Subnet mask: Reserved")
