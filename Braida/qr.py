import qrcode

file = open('lista_invitati.txt', 'r')

for nome in file:
    #nome = input('Inserisci il nome: ')    
    qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4,)
    qr.add_data(nome)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    im1 = img.save("lista_qr/{}.jpg".format(nome))
