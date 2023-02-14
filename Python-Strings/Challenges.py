# Challenge 1
# Consider the following string declaration which is part of the output of a  Linux command.
my_str = 'wlo1      Link encap:Ethernet  HWaddr b4:6d:83:77:85:f3'

# Write a Python script that extracts the MAC address (b4:6d:83:77:85:f3) from the string.

mac = my_str[len(my_str)-17:]
print(mac)

# Challenge 2
Display the following strings literally:
#It displayed: "You've got an error!"
#\n means a new line.
#\ is known as the escape character.
message = 'It displayed: "You\'ve got an error!"'
print(message)