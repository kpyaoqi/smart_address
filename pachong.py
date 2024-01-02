import socket

def get_ip_address(domain_name):
    domain_name = "dune.com"
    try:
        ip_address = socket.gethostbyname(domain_name)
        if ip_address:
            print(f"The IP address of {domain_name} is {ip_address}")
        else:
            print(f"Failed to retrieve the IP address for {domain_name}")
        return ip_address
    except socket.error as e:
        print(f"Error: {e}")
        return None




