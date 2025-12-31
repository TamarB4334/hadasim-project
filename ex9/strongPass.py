import re

def check_strong_pass(password):
    if not re.search(r'[a-z]',password):
        return False
    
    if not re.search(r'[A-Z]',password):
        return False
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]',password):
        return False
    
    if not re.search(r'[0-9]',password):
        return False
    
    if  len(password)<8:
        return False
    for char in set(password):
        if password.count(char) > 2:
            return False
    for i in range(len(password) - 2):
        seq = password[i:i+3]
        if seq.isalpha() and ord(seq[1]) == ord(seq[0]) + 1 and ord(seq[2]) == ord(seq[1]) + 1:
            return False
        if seq.isdigit() and int(seq[1]) == int(seq[0]) + 1 and int(seq[2]) == int(seq[1]) + 1:
            return False
    return True
print(check_strong_pass("1Ta@vbgd7"))