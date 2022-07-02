import socket
import sys
import subprocess 
from datetime import datetime 

#removes anything from the screen 
subprocess.call("clear", shell=True)


port_scan = input("Please enter an ip to scan: ")
remote_server_ip = socket.gethostbyname(port_scan)

#visual aid for user to show program is running
print("------------------------------")
print("Scanning ip..... please wait")
print("------------------------------")

#Taking note of the initial time before the portscan
t_initial = datetime.now()

#scanning ports with saftey net
try:
  for port in range (1, 3000): 
    sock = socket.socket(socket.AF_INET. socket.SOCK_STREAM)
    result = socket.connect_ex((remote_server_ip, port))
    if result == 0: 
      print("Port {}:   Open".format(port))
    sock.close()

except socket.error:
  print("Unable to connect. Exiting ")
  sys.exit()

except KeyboardInterrupt:
  print("You Pressed CTRL + C ")
  sys.exit 

except socket.gaierror:
  print("The HostName you are trying to connect to cannot be resolved to an ip adress. Exiting ")

#noting the time after the port scan 
t_final = datetime.now()

scan_time = t_final - t_initial
print("Port scan completed in: " + scan_time)

