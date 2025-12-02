#given data:
devices = [ ("192.168.1.10", [22, 80, 443]),
("192.168.1.11", [21, 22, 80]), ("192.168.1.12", [23,
80, 3389])]

# Given risky ports:
risky_ports = [21, 23, 3389]

#variable to count open oprts form the given data:
open_ports = 0


print("Scanning Network Devices:")
#loop to scan the given data to check for open ports:
for ip,ports in devices:

    for port in ports:
        if port == 21:
            print(f"{ip} has risky Port {port} openWarning:")
            open_ports += 1


        if port == 23:
            print(f"{ip} has risky Port {port} openWarning:")
            open_ports += 1

        if port == 3389:
            print(f"{ip} has risky Port {port} openScan:")
            open_ports += 1

#printing the number of open ports:
if open_ports == 1:
    print("Warning!")
    print(f"{open_ports} port is open!  ")

elif open_ports > 1:
    print("Warning!")
    print(f"{open_ports} ports is open!  ")
else: 
    print("NO ports are open::")
    

    
