Image Steganography with Python (Tkinter GUI)

This project implements image steganography using Python, allowing users to hide and extract text inside images through a simple graphical interface built with Tkinter.

The application uses Least Significant Bit (LSB) steganography, where binary data derived from text is embedded into the RGB pixel values of an image with minimal visual distortion. A termination flag is included to ensure accurate decoding of the hidden message.

Features

Encode text into PNG/JPEG images

Decode hidden text from encoded images

Tkinter-based GUI for ease of use

Uses Pillow (PIL) for image processing

Lossless encoding for PNG images

Technologies Used

Python

Tkinter

Pillow (PIL)

Notes

This project is intended for educational purposes to demonstrate basic steganography concepts. It does not include encryption and is not designed for secure data hiding in adversarial environments.
