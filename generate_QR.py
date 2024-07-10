import qrcode  # Import the qrcode library for generating QR codes

def generate_qr_code(data, filename):
    """
    Generate a QR code for the given data and save it as an image.

    Args:
        data (str): The data to be encoded in the QR code.
        filename (str): The name of the file to save the QR code image as.
    """
    # Create a QR code object with the specified data
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
# version=1: This parameter controls the size of the QR code. The version parameter ranges from 1 to 40, where version 1 is a 21x21 matrix, and each increment adds 4 modules/units per side (e.g., version 2 is 25x25). In this case, version 1 is used, which is the smallest QR code.
# error_correction=qrcode.constants.ERROR_CORRECT_L: This sets the error correction level. The error correction level determines how much of the QR code can be corrupted or obscured and still be readable. There are four levels:
# ERROR_CORRECT_L: About 7% or less errors can be corrected.
# ERROR_CORRECT_M: About 15% or less errors can be corrected.
# ERROR_CORRECT_Q: About 25% or less errors can be corrected.
# ERROR_CORRECT_H: About 30% or less errors can be corrected.
# box_size=10: This sets the size of each box (or pixel) in the QR code. The larger the box size, the larger the resulting QR code image will be.
# border=4: This sets the thickness of the border (in boxes) around the QR code. The default is 4, which is the minimum required for QR code readers to function properly.
    qr.add_data(data)
    # data: This is the content you want to encode in the QR code. It can be a URL, text, or any other string.
    qr.make(fit=True)
    # fit=True: This parameter ensures that the QR code is sized appropriately to fit the data. If set to False, the QR code will be generated according to the specified version parameter regardless of the data size, which might result in a larger QR code than necessary.

    img = qr.make_image(fill_color="black", back_color="white")
# This converts the QR code matrix into an image.
# fill_color="black": This sets the color of the QR code's data modules (the "black" parts).
# back_color="white": This sets the background color of the QR code (the "white" parts).

    img.save(filename) # filename: This is the name of the file to save the image as. For example, you might use "qr_code.png".
    print(f"QR code saved as {filename}") # This uses an f-string to format the message, including the filename where the QR code image was saved.

if __name__ == "__main__":
    data = input("Enter the data or URL to encode in the QR code: ")
    filename = input("Enter the filename to save the QR code image (e.g., qr_code.png): ")
    generate_qr_code(data, filename)
