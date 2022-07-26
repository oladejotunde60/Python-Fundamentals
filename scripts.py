def first_and_last(message):
    if not message:
        return True
    elif message[0] == message[-1]:
        return True
    elif message[0] != message[-1]:
        return False
 
print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))


#Function that replaces domain of an email

def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email
replace_domain('t@ab.com', 'ab.com', 'abc.com')
