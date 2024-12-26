### Task:  

Create a program that checks whether specific ports are open on a given IP address. The program should:  

1. Use Python and the `socket` module to test port availability.  
2. Define an IP address and a range of ports to scan.  
   - **IP Address**: `192.168.243.130`  
   - **Port Range**: from `20` to `27` (inclusive).  
3. Implement a function `testPort(ip, port)` that:  
   - Creates a TCP socket.  
   - Sets a timeout of 2 seconds.  
   - Attempts to connect to the specified port.  
   - Returns `True` if the port is open, or `False` otherwise.  
   - Closes the socket after the test.  
4. Iterate through the specified range of ports, call the `testPort` function for each port, and print whether the port is open or closed.  

**Example Output:**  
For each port in the range 20–27, the program should display whether the port is open:  
```
Port 20 is open
Port 21 is open
Port 22 is closed
Port 23 is closed
Port 24 is open
...
```  