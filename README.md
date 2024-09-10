# Yandex Disk Public File Downloader

This Django web application allows users to enter a public Yandex Disk link, filter files by type (images or documents), and download selected files or multiple files at once as a ZIP archive.

## Features
- Display files and folders from a public Yandex Disk link.
- Filter files by type (images or documents).
- Download individual files.
- Download multiple selected files as a ZIP archive.

## Prerequisites
- Python 3.8 or higher is installed.
- `pip` is installed to manage Python packages.
- A Yandex Disk public key is available for testing.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/lixdxn/Yandex_disk.git
   cd yandex_disk
   
2. Set up a virtual environment and activate it:
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
4. Install the dependencies:
   pip install -r requirements.txt

5. Migrate the database:
   python manage.py migrate

6. Start the development server:
   python manage.py runserver

7. Open your browser and navigate to:
   http://127.0.0.1:8000/disk/

  
