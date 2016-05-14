import mechanize
def Notify():
	browser = mechanize.Browser() 
	browser.open('https://pushbots.com/auth/login')
	browser.select_form(nr=0)
	#Enter email id in Email field
	browser['email'] = 'Email'
	#Enter password in password field
	browser['password'] = 'password'
	browser.submit()
	#Enter pushbots App ID
	browser.open('https://pushbots.com/application/push/Pushbots_App_ID')
	browser.select_form(nr=0)
	browser['push_message'] = 'Hello World'
	browser.submit()
Notify()


