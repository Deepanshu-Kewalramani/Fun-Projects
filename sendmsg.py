from datetime import datetime
import pywhatkit

try:
	#now = datetime.now()
	#hours = now.strftime("%H")
	#minutes = now.strftime("%M")
	pywhatkit.sendwhatmsg("Number with contry code" , "Hello World!" , 'give send time in hours as an integer' , 'give send time in minutes as an integer')
	
      #If you want to send message at 11:30 PM refer the line below. It uses 24-hour format and if the digit is singular don't use 0 in the beginning for eg 01:30 will be written as 1,30
      #pywhatkit.sendwhatmsg('+91xyz' , 'Hello! This message is sent using python' , 23 , 30)
	
	print('sent Successfuly')
except Exception as e:
	print(e)	
