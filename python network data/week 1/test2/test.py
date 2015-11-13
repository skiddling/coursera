import re

# file = open("regex_sum_42.txt")
file = open("regex_sum_197949.txt")

vlist = []
for line in file:
    vlist += re.findall('[0-9]+', line)

sum = 0
for e in vlist:
    sum += int(e)
print sum

# line = 'from fwjiefja@wfaefa wfa waefaaw wfa'
# y = re.findall('@([^ ]*)', line)
# print y
