import socket

host = input("Enter a host for scan: ")
scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def primary_scan(port):
  try:
    scanner.connect((host, port))
  except:
    return False
  
for array_scan in range(1, 65535):
  if primary_scan(array_scan):
    print("Port:", array_scan, "is open!")
  else:
    print("Port:", array_scan, "is close!")

for x in range(1, 1024):
  t = threading.Thread(target=primary_scan)
  t.start()
  
