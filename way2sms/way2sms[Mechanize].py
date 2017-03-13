#!/usr/bin/python
# ---------------- READ ME ---------------------------------------------
# This Script is Created Only For Practise And Educational Purpose Only
# This Script Is Created For https://bitforestinfo.blogspot.in
# This Script is Written By
#
#
##################################################
######## Please Don't Remove Author Name #########
############### Thanks ###########################
##################################################
#
#
__author__='''

######################################################
                By S.S.B Group                          
######################################################

    Suraj Singh
    Admin
    S.S.B Group
    surajsinghbisht054@gmail.com
    https://bitforestinfo.blogspot.in/

    Note: We Feel Proud To Be Indian
######################################################
'''
# Import Module
import mechanize
import cookielib
import sys

# Function For Extracting Tokken 
def cook(cj):
	j=str(cj)
	t2=j.find(' for ')
	t1=int(j.find('~'))+1
	tokken=str(j[t1:t2])
	return tokken	

# Main Function
def main():
	number=int(raw_input(' [+] Please Enter Your Username : '))
        password=int(raw_input(' [+] Please Enter Your Password : '))
	#================   Checking Mechanizam =====================================
	if len(str(number))==10:
		pass
	else:
		print " [*] Invalid Username"
		sys.exit(0)
	if len(str(password))==10:
		pass
	else:
		print " [*] Invalid Password  "
		sys.exit(0)


	#============================================================================
	# ***************** Login *******************************
	# ***************** Configuration  **********************	
	url='http://site24.way2sms.com/Login1.action'
	data='username='+str(number)+'&password='+str(password)
	# ********************************************************
	cj=cookielib.LWPCookieJar()
	br=mechanize.Browser()
	br.addheaders=[('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.8.0')]
	# Setting Management
	br.set_cookiejar(cj)
	br.set_debug_http(True)
	br.set_debug_redirects(True)
	br.set_debug_responses(True)
	br.set_handle_equiv(True)
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	print '[+] Please Wait. Trying To Login In '
	req=br.open(url, data=data)
	print '\n'*14,'[+] Login Successful [+]'
	# ****** Tokken	Receiving Mechanizem ******************
	tokken=cook(cj)
	print '\n [+] Tokken Received : ', tokken
	# *******************************************************************
	# ********* Sms Sending System Configuration ************************
	url='http://site24.way2sms.com/smstoss.action'
	head=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.8.0'),('Refere','http://site24.way2sms.com/sendSMS?Token='+tokken)]
	mobile=int(raw_input(' [*] Please Enter Mobile Number For Sending SMS : '))
	#================   Checking Mechanizam =====================================
	if len(str(mobile))==10:
		pass
	else:
		print " [*] Invalid Username"
		sys.exit(0)


	while True:
		message_raw=str(raw_input(' [*] Please Enter Message For Sending. Note ! Not More Then 140 Words: '))
		message=message_raw.replace(' ', '+')
		msglen=140-len(message)
		if len(message)<140:
			break
		else:
			pass
	data='ssaction=ss&Token='+tokken+'&mobile='+str(mobile)+'&message='+str(message)+'&msgLen='+str(msglen)
	br.addheaders=head
	print '[+] Sending SMS . Please Wait [+]'
	req=br.open(url, data=data)
	print '\n'*40,' [+] Task Complete Thanks For Using [+]'

# Main Function Trigger
if __name__=='__main__':
	main()
