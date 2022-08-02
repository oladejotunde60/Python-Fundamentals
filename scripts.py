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

#Compare strings
word = "This is the beginning of my wonderful Python exploit"
"This" in word

#lower() and upper() change case
ans = "YES"
if ans.lower() == "yes":
    print("User said yes")
    
#strip() removes spaces
g = "  yes  "
h = g.strip()
p = g.lstrip()
y = g.rstrip()
print(h, p, y)

#"This returns how many times an alphabet retrn".count("e")
t = "This returns how many times an alphabet retrn".count("e")
print(t)

#endswith,prints string that ends with a substring
l = 'forest'.endswith("st")
print(l)

#isnumeric checks if the strings are just number
u = "Hello world!".isnumeric()
print(u)
r = "234".isnumeric()
print(r)


Fill in the gaps in the initials function so that it returns the initials of the words contained in the phrase received, in upper case. For example: "Universal Serial Bus" should return "USB"; "local area network" should return "LAN”.
def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS

#Palindrome function
def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for string in input_string.lower():
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		if string.replace(" ",""):
			new_string = string + new_string
			reverse_string = string + reverse_string
	# Compare the strings
	if new_string[::-1] == reverse_string:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
