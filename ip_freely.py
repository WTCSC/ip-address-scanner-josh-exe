import os
import time
import ipaddress

def scan_network(cidr):

    network = ipaddress.ip_network(cidr, strict=False)#----------------------------------------------------------->  Convert the CIDR input into an IP network
    
    scan_results = []
    
   
    for ip in network.hosts(): #---------------------------------------------------------------------------------->  Loop through all the host IP addresses in the network
        start_time = time.time() #-------------------------------------------------------------------------------->  Record the start time for the ping
        
        response = os.system(f"ping -c 1 -w 1 {ip} > /dev/null 2>&1")#-------------------------------------------->  Ping the host (1 packet, 1 second timeout)
        end_time = time.time() #---------------------------------------------------------------------------------->  Record the end time
        
        
        response_time = round((end_time - start_time) * 1000, 2) if response == 0 else None # -------------------->  Calculate the round-trip time (in milliseconds) if the ping was successful
        
        status = "Up" if response == 0 else "Down" #-------------------------------------------------------------->  Determine the status based on the response (Up or Down)
    
        error_message = "" if response == 0 else "No response" #-------------------------------------------------->  Assign error message if the host is down
        
        
        scan_results.append({ #---------------------------------------\
            "IP": str(ip),                        #                    \
            "Status": status,                     #                     |----------------------------------------->  Append the result of the scan to the results list
            "Response Time (ms)": response_time,  #                     |
            "Error Message": error_message        #                    /
        }) #----------------------------------------------------------/
    
    return scan_results

if __name__ == "__main__":
    
    network_cidr = input("Enter a network in CIDR notation (e.g., 192.168.1.0/24): ") #--------------------------->  Prompt the user to enter a network in CIDR notation
    
    
    devices = scan_network(network_cidr) #------------------------------------------------------------------------>  Scan the network and get the results
    
    
    for device in devices:#--------------------------------------------------------------------------------------->  Print out the results for each device in the network
        print(f"IP: {device['IP']}, Status: {device['Status']}, Response Time: {device['Response Time (ms)']} ms, Error: {device['Error Message']}") #------------/
