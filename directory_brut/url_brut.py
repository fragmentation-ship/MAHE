# -*- coding: utf-8 -*- 
import urllib.request
import threading
from datetime import datetime
import sys

event = threading.Event()
event2 = threading.Event()

def func(ev, urll):
	File = open("directory_brut/dictionare/dict1.txt", 'r')
	for line in File:
		address = urll + line
		try:
			url = urllib.request.urlopen(address)
			if url.code == 200:
				print (address, url.code, "--Ditrctoty available")
				print ("-------*--------")
		except urllib.error.HTTPError as error:
			if(error.code == 404):
				print (address, error.code ,"--error")
				print ("-------*--------")
			pass


def func2(ev, urll):
	File = open("directory_brut/dictionare/dict2.txt", 'r')
	
	for line in File:
		address = urll + line
		try:
			url = urllib.request.urlopen(address)
			print (address, url.code, "--Ditrctoty available")
			print ("-------*--------")
		except urllib.error.HTTPError as error:
			if(error.code == 404):
				print (address, error.code ,"--error")
				print ("-------*--------")
			pass
 
def call():
	start_time = datetime.now()

	a = input("-> Enter Url: ")

	thr = threading.Thread(target=func, args=(event, a)) # initiate threading n1
	thr2 = threading.Thread(target=func2, args=(event2, a)) #initiate threading n2

	thr.daemon = True
	thr2.daemon = True
	 
	thr.start()
	thr2.start()

	while True: #
	    thr.join(600)
	    thr.join(600)
	    if not thr.isAlive() and not thr2.isAlive():
	        break

	end_time = datetime.now()
	print('Duration time: {}'.format(end_time - start_time) + "\n")



# -----------------------------------
# import urllib.request
# import threading
# from datetime import datetime
# import sys

# event = threading.Event()
# event2 = threading.Event()

# def func(ev):
# 	File = open("dictionare/dict1.txt", 'r')
# 	for line in File:
# 		address = 'http://maulnet.ru/' + line
# 		try:
# 			url=urllib.request.urlopen(address)
# 		# if url.code == 200:
# 			print (address, url.code, "--Ditrctoty available")
# 			print ("-------*--------")
# 		except urllib.error.HTTPError as e:
# 			if(e.code == 404):
# 				print (address, e.code ,"--error")
# 				print ("-------*--------")


# def func2(ev):
# 	File = open("dictionare/dict2.txt", 'r')
	
# 	for line in File:
# 		address = 'http://maulnet.ru/' + line
# 		try:
# 			url=urllib.request.urlopen(address)
# 			print (address, url.code, "--Ditrctoty available")
# 			print ("-------*--------")
# 		except urllib.error.HTTPError as e:
# 			if(e.code == 404):
# 				print (address, e.code ,"--error")
# 				print ("-------*--------")
 

# start_time = datetime.now()

# thr = threading.Thread(target=func, args=(event, )) # initiate threading n1
# thr2 = threading.Thread(target=func2, args=(event2, )) #initiate threading n2

# thr.daemon = True
# thr2.daemon = True
 
# thr.start()
# thr2.start()

# while True: #
#     thr.join(600)
#     thr.join(600)
#     if not thr.isAlive() and not thr2.isAlive():
#         break

# end_time = datetime.now()
# print('Duration: {}'.format(end_time - start_time))
# ------------------------
