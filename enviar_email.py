import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import pyttsx3

maquina = pyttsx3.init()

maquina.say("Digite seu email!")
maquina.runAndWait()
remetente = str(input("Qual o seu email?\nResponda aqui: "))
maquina.say("Digite quem vai receber esse email!")
maquina.runAndWait()
destinatario = str(input("Quem vai receber o email:\nResponda aqui: "))
maquina.say("Digite o assunto do seu email!")
maquina.runAndWait()
assunto = str(input("Qual o assunto?\nResponda aqui:"))
maquina.say("Digite a sua mensagem!")
maquina.runAndWait()
mensagem = str(input("Qual a mensagem?\nResponda aqui: "))
maquina.say("Digite a sua senha!")
maquina.runAndWait()
senha = str(input("Qual a sua senha?\nResponda aqui: "))



msg = MIMEMultipart()
msg["From"] = remetente
msg["To"] = destinatario
msg["Subject"] = assunto

msg.attach(MIMEText(mensagem, "plain"))
server = smtplib.SMTP("smtp.gmail.com", port=587)
server.starttls()
server.login(msg["From"], senha)
server.sendmail(msg["From"], msg["To"], msg.as_string())
server.quit()

maquina.say("email enviado!")
maquina.runAndWait()
print("email enviado!")