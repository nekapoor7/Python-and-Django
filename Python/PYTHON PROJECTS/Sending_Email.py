import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


from_addr = 'neha.kapoor070789@gmail.com'
to_addr = ['nehakpr789@gmail.com','harshm67@gmail.com']
msg=MIMEMultipart()
msg['From'] = from_addr
msg['To'] =",".join(from_addr)
msg['subject'] = 'Sending Love'

body ='I Love you baby !!!!!!!!!!!!!!!! MMMMMMMuuuuuuuuaaaaaaahhhhhhhhh'

msg.attach(MIMEText(body,'plain'))

email = "neha.kapoor070789@gmail.com"
password = "meenu@RCK7079"

mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(email,password)
text = msg.as_string()
mail.sendmail(from_addr,to_addr,text)
mail.quit()

