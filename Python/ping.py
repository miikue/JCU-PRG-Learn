import socket

ip = "192.168.243.130"
portStart = 20
portEnd = 27

def testPort(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((ip, port))
        return True
    except:
        return False
    finally:
        s.close()

for i in range(portStart, portEnd + 1):
    if testPort(ip, i):
        print("Port", i, "is open")
