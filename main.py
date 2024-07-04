# Import the pyfiglet library, which is used to generate ASCII art banners
import pyfiglet

# Import the sys library, which provides access to system-specific parameters and functions
import sys

# Import the socket library, which provides low-level network communication functions
import socket

# Import the datetime library, which provides functions for working with dates and times
from datetime import datetime

# Use pyfiglet to generate an ASCII art banner with the text "PORT SCANNER"
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
# Print the banner to the console
print(ascii_banner)

# Check if the user provided a target hostname or IP address as a command-line argument
if len(sys.argv) == 2:
    # Translate the hostname to an IPv4 address using the socket library
    target = socket.gethostbyname(sys.argv[1]) 
else:
    # If no target was provided, print an error message
    print("Invalid amount of Argument")

# Print a separator line to the console
print("-" * 50)
# Print the target hostname or IP address to the console
print("Scanning Target: " + target)
# Print the current date and time to the console
print("Scanning started at:" + str(datetime.now()))
# Print another separator line to the console
print("-" * 50)

try:
    # Loop through all possible port numbers (1-65,535)
    for port in range(1,65535):
        # Create a new socket object using the AF_INET (IPv4) and SOCK_STREAM (TCP) protocols
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set the socket timeout to 1 second
        socket.setdefaulttimeout(1)
        
        # Attempt to connect to the target host on the current port
        # The connect_ex method returns an error indicator (0 if successful, otherwise an error code)
        result = s.connect_ex((target,port))
        # If the connection was successful, print a message indicating that the port is open
        if result ==0:
            print("Port {} is open".format(port))
        # Close the socket
        s.close()
        
# Catch any KeyboardInterrupt exceptions (e.g. if the user presses Ctrl+C)
except KeyboardInterrupt:
    print("\n Exiting Program!!!!")
    # Exit the program using the sys library
    sys.exit()
# Catch any socket.gaierror exceptions (e.g. if the hostname cannot be resolved)
except socket.gaierror:
    print("\n Hostname Could Not Be Resolved!!!!")
    # Exit the program using the sys library
    sys.exit()
# Catch any socket.error exceptions (e.g. if the server is not responding)
except socket.error:
    print("\ Server not responding!!!!")
    # Exit the program using the sys library
    sys.exit()