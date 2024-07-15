from pdf2docx import Converter

def convert_pdf_to_docx(input_path, output_path):
    """
    Convert a PDF file to DOCX format.
    
    Args:
    input_path (str): Path to the input PDF file.
    output_path (str): Path to the output DOCX file.
    """
    # Create a PDF to DOCX converter object
    cv = Converter(input_path)
    
    # Perform the conversion
    cv.convert(output_path, start=0, end=None)
    
    # Close the converter object
    cv.close()

def main():
    input_path = 'path/to/input/document.pdf'  # Specify the path to the input PDF
    output_path = 'path/to/output/document.docx'  # Specify the path to the output DOCX
    
    # Convert the PDF to DOCX
    convert_pdf_to_docx(input_path, output_path)
    
    print(f'Converted {input_path} to {output_path}')

if __name__ == "__main__":
    main()
