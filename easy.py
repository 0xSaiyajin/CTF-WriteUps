#Bugs Bunny CTF 2017 - Programming Challenge WriteUp
import socket

city ={"Alabama":"Montgomery","Montana":"Helena","Alaska":"Juneau","Nebraska":"Lincoln","Arizona":"Phoenix","Nevada":"Carson City","Arkansas":"Little Rock","New Hampshire":"Concord","California":"Sacramento","New Jersey":"Trenton","Colorado":"Denver","New Mexico":"Santa Fe","Connecticut":"Hartford","New York":"Albany","Delaware":"Dover","North Carolina":"Raleigh","Florida":"Tallahassee","North Dakota":"Bismarck","Georgia":"Atlanta","Ohio":"Columbus","Hawaii":"Honolulu","Oklahoma":"Oklahoma City","Idaho":"Boise","Oregon":"Salem","Illinois":"Springfield","Pennsylvania":"Harrisburg","Indiana":"Indianapolis","Rhode Island":"Providence","Iowa":"Des Moines","South Carolina":"Columbia","Kansas":"Topeka","South Dakota":"Pierre","Kentucky":"Frankfort","Tennessee":"Nashville","Louisiana":"Baton Rouge","Texas":"Austin","Maine":"Augusta","Utah":"Salt Lake City","Maryland":"Annapolis","Vermont":"Montpelier","Massachusetts":"Boston","Virginia":"Richmond","Michigan":"Lansing","Washington":"Olympia","Minnesota":"Saint Paul","West Virginia":"Charleston","Mississippi":"Jackson","Wisconsin":"Madison","Missouri":"Jefferson City","Wyoming":"Cheyenne"}

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '34.253.165.46'
port = 11223

sock.connect((host,port))
while(True):
	data1 = sock.recv(1024)
	data = sock.recv(1024)
	data2 = data.replace("\n","")
	data2 = data2.replace("\r","")
	data2 = data2.replace(" ",",")
	
	problem = data2.split(",")

	if '=' in problem:
		
		if '+' == problem[3]:
			x = int(problem[6]) - int(problem[4])
		elif '-' == problem[3]:
			x = int(problem[6]) + int(problem[4])
		elif '*' == problem[3]:
			x = int(problem[6]) / int(problem[4])
		elif '/' == problem[3]:
			x = int(problem[6]) * int(problem[4])

		print data1
		print data + "\nx value is: " + str(x)
		sock.send(str(x))
		
	elif 'Level 500.: ' in data:
		print "Flag?"
		print data1
		print data
		arg = raw_input("Manual Input at 500: ")
		print sock.send(arg)
		print sock.recv(1024)
		sock.close()
	else:
		data3 = " ".join(problem[2:])
		answer = (city[data3])
		
		print data1
		print data + "\nanswer is: " + answer
		sock.send(answer)



