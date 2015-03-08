import smtplib

fromaddr = 'duanelewis88@gmail.com'
toaddr = 'duanelewis88@gmail.com'
message = """From: {} <{}>

To: {} <{}>

Subject: {}

{}

"""
fromname ='Duane'
fromaddr = 'duanelewis88@gmail.com'
toname = 'Duane'
toaddr='duanelewis88@gmail.com'
subject = 'Hello'
msg = 'This is a test email.'
messagetosend = message.format(

 fromname,
 fromaddr,
 toname,
 toaddr,
 subject,
 msg)

# Credentials (if needed)

username = 'duanelewis88@gmail.com'

password = 'nfkdxlhdicvehlez'

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(username,password)

server.sendmail(fromaddr, toaddr, messagetosend)

server.quit()