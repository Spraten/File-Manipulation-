import os
import shutil
import subprocess
import sys

# Function to install required packages
def install_packages(packages):
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

# Required packages
packages = ['PyPDF2']

# Call function to install required packages
install_packages(packages)

from PyPDF2 import PdfReader, PdfWriter

def decrypt_pdf(input_pdf_path, output_pdf_path, password):
    print(f"Attempting to decrypt: {input_pdf_path}")
    
    reader = PdfReader(input_pdf_path)

    if reader.is_encrypted:
        try:
            reader.decrypt(password)

            writer = PdfWriter()

            for page in reader.pages:
                writer.add_page(page)

            writer.write(output_pdf_path)

            print(f"The file {input_pdf_path} has been successfully decrypted as {output_pdf_path}")

        except NotImplementedError:
            print(f"Sorry, the encryption used in this PDF: {input_pdf_path} is not supported.")
    else:
        print(f"The file {input_pdf_path} is not encrypted.")
    
    print("Finished processing: ", input_pdf_path)

# Prompt for directory
dir_path = input("Please enter the absolute path of the PDFs (leave blank for current directory): ")
if not dir_path:
    dir_path = '.'

# Get all PDF files in the given directory
pdf_files = [f for f in os.listdir(dir_path) if f.endswith('.pdf')]

print(f"Found {len(pdf_files)} PDF files in the directory: {dir_path}.")

# Prompt for password
password = input("Please enter the password (leave blank if password is stored in password.txt): ")
if not password:
    with open('password.txt', 'r') as f:
        password = f.read().strip()

# Decrypt each PDF
for pdf_file in pdf_files:
    input_pdf_path = os.path.join(dir_path, pdf_file)
    output_pdf_path = os.path.join(dir_path, 'decrypted', pdf_file[:-4] + '_decrypted.pdf')

    # Create 'decrypted' folder if it doesn't exist
    if not os.path.exists(os.path.join(dir_path, 'decrypted')):
        os.makedirs(os.path.join(dir_path, 'decrypted'))

    decrypt_pdf(input_pdf_path, output_pdf_path, password)

# Move decrypted PDFs to new folder
for pdf_file in pdf_files:
    old_file_path = os.path.join(dir_path, pdf_file[:-4] + '_decrypted.pdf')
    new_file_path = os.path.join(dir_path, 'decrypted', pdf_file[:-4] + '_decrypted.pdf')
    shutil.move(old_file_path, new_file_path)
