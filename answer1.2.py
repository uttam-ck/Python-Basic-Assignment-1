# Validate a given email address to check if it’s a valid Gmail address, considering:
# It should contain "@gmail.com".
# The username before "@gmail.com" should contain only lowercase letters , numbers and permitted symbols.
# Provide informative error messages for invalid IP or email.

def validate_email(mail_id: str) -> bool:
    
    mail_id = mail_id.strip()

    if mail_id.count('@') != 1:
        return False
    username, domain = mail_id.split('@')
    
    if domain != "gmail.com":
        return False
    
    if username.isdigit():
        return False
    
    if not username.lower():
        return False
    
    if ' ' in username:
        return False
    
    
    
    invalid_symbols = ["!", "#", "$", "%", "&", "*", "+", "/", "=", "?", "^", "{", "}", "|", "~", " "]
    
    for x in invalid_symbols:
        if x in username:
            return False
    
    return True
    
mail = input("Enter an mail address: ")
if validate_email(mail):
    print("Valid mail address")
else:
    print("Invalid mail address")
    