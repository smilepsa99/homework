import smtplib

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
print(smtp.login("smilepsa99@gmail.com","699799sang!"))