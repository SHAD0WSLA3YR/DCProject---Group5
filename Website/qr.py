import qrcode

# Function to generate QR code
def generate_qr(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Generate QR code for the Brain model
generate_qr('https://adobeaero.app.link/E8c8fzy7xIb', '3D_Brain.png')

# Generate QR code for the Heart model
generate_qr('https://adobeaero.app.link/rILR04qdyIb', '3D_Heart.png')
