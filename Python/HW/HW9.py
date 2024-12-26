def ipToBinary(ip):
    ip = ip.split('.')
    for i in range(len(ip)):
        ip[i] = bin(int(ip[i]))[2:]
        while len(ip[i]) < 8:
            ip[i] = '0' + ip[i]
    return "".join(ip)    

def binaryToIp(binary):
    ip = []
    for i in range(0,32,8):
        ip.append(str(int(binary[i:i+8],2)))
    return ".".join(ip)

####################################

# Return network from list of ips
def calculateNetwork(list):
    binary = []
    for i in list:
        binary.append(ipToBinary(i))
    binary.sort()
    network = binary[0]
    for i in range(32):
        for j in range(1,len(binary)):
            if binary[j][i] != network[i]:
                return binaryToIp(network) + '/' + str(i)
    return binaryToIp(network) + '/32'

# Test
calculateNetwork(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"

calculateNetwork(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"

calculateNetwork(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"



# nějaký experiment s lambda funkcí
#adresy = ["172.16.12.0", "172.16.13.0", "172.155.43.9"]

#sorted(adresy, key=lambda x: ipToBinary(x))

#print(adresy)