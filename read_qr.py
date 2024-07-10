from PIL import Image
from pyzbar.pyzbar import decode

def read_qr_code(image_path):
    """
    Read and decode a QR code from an image.

    Args:
        image_path (str): The path to the image containing the QR code.

    Returns:
        str: The decoded data from the QR code.
    """
    try:
        # Open the image file
        with open(image_path, 'rb') as image_file:
            # Load image data
            image = Image.open(image_file)
            # Decode QR code
            qr_codes = decode(image)
            # Extract and return data
            if qr_codes:
                return qr_codes[0].data.decode('utf-8')
            else:
                return "No QR code found or could not be decoded."
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    image_path = input("Enter the path to the image containing the QR code: ")
    result = read_qr_code(image_path)
    print(f"Decoded QR code data: {result}")




# Imports: Import necessary modules including PIL.Image for image manipulation and pyzbar.pyzbar.decode for QR code decoding.

# read_qr_code Function: This function reads and decodes a QR code from an image file.

# Opening the Image: Image.open(image_file) opens the image file using PIL's Image module.

# Decoding the QR Code: decode(image) attempts to decode the QR code from the opened image.

# Error Handling: Exception handling (try and except) is used to catch and display any errors that occur during image loading or QR code decoding.