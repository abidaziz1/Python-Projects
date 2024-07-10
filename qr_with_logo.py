import qrcode  # Import the qrcode library for generating QR codes
from PIL import Image  # Import the Image module from the PIL library

def generate_qr_code_with_logo(data, filename, logo_path):
    """
    Generate a QR code with a logo in the center and save it as an image.

    Args:
        data (str): The data to be encoded in the QR code.
        filename (str): The name of the file to save the QR code image as.
        logo_path (str): The path to the logo image file.
    """
    # Create a QR code object with the specified data
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code object
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    
    # Open the logo image file
    logo = Image.open(logo_path)

    # Calculate the size and position for the logo
    logo_size = 50
    logo = logo.resize((logo_size, logo_size))
    pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)

    # Paste the logo onto the QR code image
    img.paste(logo, pos)

    # Save the image to the specified filename
    img.save(filename)
    print(f"QR code with logo saved as {filename}")

if __name__ == "__main__":
    data = input("Enter the data or URL to encode in the QR code: ")
    filename = input("Enter the filename to save the QR code image (e.g., qr_code_with_logo.png): ")
    logo_path = input("Enter the path to the logo image: ")
    generate_qr_code_with_logo(data, filename, logo_path)
