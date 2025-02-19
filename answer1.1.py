# Validate a given public IP address to check if it follows the correct format (IPv4).

def validate_ip(ip: str) -> bool:
    
    sections = ip.split('.')
    
    if len(sections) != 4:
            return False
    
    for section in sections:
        
        if not section.isdigit():
            return False
        
        if section.startswith('-'):
            return False
        
        if len(section) > 1 and section.startswith('0'):
            return False
        
        num = int(section)
        if num > 255:
            return False
    
    return True

ip = input("Enter an IPv4 address: ")
if validate_ip(ip):
    print("Valid IPv4 address")
else:
    print("Invalid IPv4 address")
    
    
        







