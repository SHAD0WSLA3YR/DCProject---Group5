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
    byte_arr = io.BytesIO()
    img.save(byte_arr)
    byte_arr = byte_arr.getvalue()
    
    return byte_arr

def lambda_handler(event, context):
    url = event['rawPath']
    image_bytes = b""
    
    if 'brainModel' in url:
        image_bytes = generate_qr('https://humananatomy-ar.s3.amazonaws.com/BrainModel.html', '3D_Brain.png')
    
    elif 'heartModel' in url:
        image_bytes = generate_qr('https://humananatomy-ar.s3.amazonaws.com/heartModel.html', '3D_Heart.png')
    
    qr_image_base64 = base64.b64encode(image_bytes).decode('utf-8')

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': qr_image_base64
    }










