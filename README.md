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
Step 1: Clone the Repository

```shell
git clone https://github.com/lixdxn/Yandex_disk.git
cd yandex_disk
```


Step 2: Set Up a Virtual Environment
Using venv

```shell
python -m venv venv
source venv/bin/activate   
# On Windows use 
cd venv/Scripts 
./activate
```


Step 3: Install Dependencies
Install the required packages using pip:

```
pip install -r requirements.txt
```
**requirements.txt**: Make sure your `requirements.txt` file is up-to-date with all the necessary dependencies for your Django project. You can generate it using:
```
pip freeze > requirements.txt
```


Step 4: Set Up the Database
Apply migrations to set up the database schema:

```
python manage.py migrate
```


Step 5: Running the Project
To start the development server, run:

```
python manage.py runserver
```


Step 6: Open your browser and navigate to

http://127.0.0.1:8000/disk/