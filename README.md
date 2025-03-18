# OCR Drag & Drop App

A simple, modern drag-and-drop OCR (Optical Character Recognition) application built with Python using `tkinter`, `ttkbootstrap`, and `pytesseract`. This app allows users to extract text from images by simply dragging and dropping them into the interface.

## Features
- **Drag & Drop Support**: Easily drop images into the app for text extraction.
- **Minimalist UI**: Uses `ttkbootstrap` for a clean black, white, and gray-themed design.
- **Processing Indicator**: Displays a message when an image is being processed.
- **Works Locally**: No internet required; runs entirely on your machine.
- **Cross-Platform**: Works on Windows, macOS, and Linux, including Raspberry Pi.

## Installation

### Prerequisites
- Python 3.7+
- `Tesseract OCR` installed on your system:
  - **Windows**: [Download Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
  - **Linux**: Install via package manager:
    ```bash
    sudo apt install tesseract-ocr
    ```
  - **macOS**: Install using Homebrew:
    ```bash
    brew install tesseract
    ```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage
Run the application with:
```bash
python ocr_app.py
```
Then, **drag and drop an image** into the app, and it will display the extracted text.

## Dependencies
All dependencies are listed in `requirements.txt`:
```txt
pytesseract
pillow
ttkbootstrap
tkinterdnd2
```

## Contributing
Feel free to submit pull requests or issues on GitHub to improve the project!

## License
This project is open-source and available under the MIT License.


