#!/usr/bin/python
#rot13encoder.py	MrG	2013.0428
email = raw_input("enter email: ")
print "original email: ", email

encoded=""
for i in range(len(email)):
    if (ord(email[i])>=97 and ord(email[i])<=122):
        encoded =  encoded + chr(((ord(email[i])+13)-97)%26+97)
    elif (ord(email[i])>=65 and ord(email[i])<=90):
        encoded =  encoded + chr(((ord(email[i])+13)-65)%26+65)
    else:
        encoded =  encoded + email[i]
print
print "encoded email:  ", encoded