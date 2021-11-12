import re
phonenum="91-9876543564"
reg="\w{2}-\w{10}"
if re.search(reg,phonenum):
    print("valid phone number")
else:
    print("invalid phone number")