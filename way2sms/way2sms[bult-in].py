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
import urllib
import urllib2
import cookielib
import sys
from getpass import getpass

# Function For Tokken Extraction
def cook(cj):
        j=str(cj)
        t2=j.find(' for ')
        t1=int(j.find('~'))+1
        tokken=str(j[t1:t2])
        return tokken   

# Main
def main():
        print '''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+   This is Only For Practise And Educational Purpose Only  +
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''
        # Take User Inputs
        number=int(raw_input(' [+] Please Enter Your Username : '))
        password=int(getpass(' [+] Please Enter Your Password : '))

        #================   Verifying Inputs =====================================
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
        url='http://site24.way2sms.com/Login1.action'     		# Site Url
        data={'username':str(number),'password':str(password)}  # Data
        data=urllib.urlencode(data)								# Encode Data

        # ********************************************************
        cj=cookielib.CookieJar()								# Cookie Jar
        header={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.8.0'}
        req=urllib2.Request(url, data, headers=header)			# Creating request
        opennr=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), 
                                    urllib2.HTTPRedirectHandler())	# Creating Opener
        print '[+] Please Wait. Trying To Login In '
        req=opennr.open(req)									# Open Url
        sucess=str(req.info())									# Capture Response
        sucess=sucess.find('Set-Cookie')						# Capture cookie
        # Verifying Cookies
        if (sucess==-1):
                print '\n','[+] Login Successful [+]'
                pass
        else:
                print '\n','[+] Login Failed [+]'
                raw_input('')
                sys.exit(0)
        # ****** Tokken Receiving Mechanizem ******************
        tokken=cook(cj)
        print '\n [+] Tokken Received : ', tokken
        # *******************************************************************
        # ********* Sms Sending System Configuration ************************
        url='http://site24.way2sms.com/smstoss.action'
        head={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.8.0','Refere':str('http://site24.way2sms.com/sendSMS?Token='+tokken)}
        mobiles=raw_input(' [*] Please Enter Mobile Number For Sending SMS : ').split(',')
	print " [+] Total Mobile Number Added : ", len(mobiles)
        #================  Input Message Checking Mechanizam =====================================

        while True:
                message_raw=str(raw_input(' [*] Please Enter Message For Sending. Note ! Not More Then 140 Words: '))
                message=message_raw.replace(' ', '+')
                msglen=140-len(message)
                if len(message)<140:
                        break
                else:
                        pass
	failed_number=[]
	# Sending Data
	for mobile in mobiles:
		if len(str(mobile))==10:
	        	data='ssaction=ss&Token='+tokken+'&mobile='+str(mobile)+'&message='+str(message)+'&msgLen='+str(msglen)
	        	req=urllib2.Request(url, data=data, headers=head)
	        	print '\n [+] Sending SMS to ... {} Please Wait [+]'.format(mobile)
	        	req=opennr.open(req)
	        	print ' 	[+] Done! Sms Sent To {} [+]'.format(mobile)
		else:
			failed_number.append(mobile)

        for i in failed_number:
		print " [+] Wrong Number ... {} [+]".format(i)
# Main Trigger
if __name__=='__main__':
        main()