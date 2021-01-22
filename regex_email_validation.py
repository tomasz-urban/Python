#  Email validation (check if somebody enters real email

#  Google for: python email validation regex

#  on a website: https://emailregex.com/ found:
# r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
# check it on a https://regex101.com/ and try to understand

import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = 'b@b.com'

a = pattern.search(string)
print(a)

# if there is no match we can use an "if" statement to give the uotput to the user: "Please try again"

