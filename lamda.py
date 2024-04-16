import base64
import io
import qrcode

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
    return img

def lamda_handler(event, context):
    # image_bytes = base64.b64decode(event['image'])
    url = context.request.url
    image = " "
    if('brainModel' in url):
        image = io.BytesIO(generate_qr('https://humananatomy-ar.s3.amazonaws.com/BrainModel.html', '3D_Brain.png'))
    
    elif('heartModel' in url):
        image = io.BytesIO(generate_qr('https://humananatomy-ar.s3.amazonaws.com/heartModel.html', '3D_Heart.png'))
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'image/jpeg'
        },
        'body': image.getvalue()
    }

# Generate QR code for the Brain model
# generate_qr('https://humananatomy-ar.s3.amazonaws.com/BrainModel.html', '3D_Brain.png')

# Generate QR code for the Heart model
# generate_qr('https://humananatomy-ar.s3.amazonaws.com/heartModel.html', '3D_Heart.png')








