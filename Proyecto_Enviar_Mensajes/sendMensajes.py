# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 22:30:40 2022

@author: Yuli
"""

from flask import Flask, render_template, request
from twilio.rest import Client
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Instancia de Flask. Aplicación
app = Flask(__name__)


#Creamos nuestro primer route. '/login'
@app.route('/')
def principal():
    #Renderizamos la plantilla del formulario
    return render_template("Formulario5.html")

@app.route('/sms')
def sms():
    return render_template('sms.html')

@app.route('/whatsapp')
def whatsapp():
    return render_template('whatsapp.html')

@app.route('/email')
def email():
    return render_template('email.html')



# Definimos el route con el método POST
@app.route('/sms', methods=["POST"])
def sendSMS():
    mensajeSMS = request.form['mensajeSMS']
    
    # Your Account SID from twilio.com/console
    account_sid = "AC076ac813fe27870b945a0fb8ee08620c"
    # Your Auth Token from twilio.com/console
    auth_token  = "5e473f03c101ee9429c99d251c73fca7"
    
    try:

        client = Client(account_sid, auth_token)
    
        message = client.messages.create(
            to="+573108662432", 
            from_="+16084801820",
            body=mensajeSMS)
    
        print(message.sid)
        enviadoSMS = True
        
    except Exception as e:
        enviadoSMS = False
        print(e)
    
    return render_template("sms.html", enviadoSMS=enviadoSMS)

@app.route('/whatsapp', methods=["POST"])
def sendWhatsapp():
    mensajeWhats = request.form['mensajeWhats']
    
    account_sid = 'AC076ac813fe27870b945a0fb8ee08620c'
    auth_token = '5e473f03c101ee9429c99d251c73fca7'
    
    try:
    
        client = Client(account_sid, auth_token)
    
        message = client.messages.create(
        body=mensajeWhats,
        from_='whatsapp:+14155238886',
        to='whatsapp:+573108662432')
    
        print(message.sid)
        enviadoWhats = True
        
    except Exception as e:
        enviadoWhats = False
        print(e)
    
    return render_template("whatsapp.html", enviadoWhats=enviadoWhats)

@app.route('/email', methods=["POST"])
def sendEmail():
    correoU = request.form['emailU']
    encabezado = request.form['emailHeader']
    mensajeEmail = request.form['mensajeEmail']
    
    message = Mail(
        from_email='nikybae18@gmail.com',
        to_emails=correoU,
        subject=encabezado,
        html_content=mensajeEmail)
    
    try:
        sg = SendGridAPIClient('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')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        
        enviadoEmail = True
    except Exception as e:
        enviadoEmail = False
        print(e)
        
    return render_template("email.html", enviadoEmail=enviadoEmail)
   
    

if __name__ == '__main__':
    #Iniciamos la aplicación en modo debug
    app.run(debug=True)