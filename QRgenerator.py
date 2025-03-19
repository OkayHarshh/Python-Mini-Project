import qrcode
#Taking UPI ID as a Input
upi_id = input("Enter UPI ID: ")

#upi://pay?pa

#Defining the payment URL based on UPI ID and Payment app
#You can modify these URLS based on the payment apps you want to support

phonepeURL = f'upi://pay?pahonepe{upi_id}&pn=Recipient%20Name&mc=1234&tid=123456&tn=Payment%20Description&am=100&cu=INR'
gpayURL = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234&tid=123456&tn=Payment%20Description&am=100&cu=INR'
paytmURL = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234&tid=123456&tn=Payment%20Description&am=100&cu=INR'

#Generating QR codes
phonepeQR = qrcode.make(phonepeURL)
gpayQR = qrcode.make(gpayURL)
paytmQR = qrcode.make(paytmURL)

#Displaying QR codes
phonepeQR.show()

gpayQR.show()

paytmQR.show()

#Saving QR codes
phonepeQR.save('phonepeQR.png')
gpayQR.save('gpayQR.png')
paytmQR.save('paytmQR.png')

print("QR codes saved successfully!")

