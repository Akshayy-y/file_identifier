Magic Number File Type Identifier (CLI Tool)

A lightweight, cybersecurity-oriented CLI tool that identifies file types using magic numbers instead of file extensions — useful for detecting spoofed/malicious files, analyzing malware samples, and performing digital forensics.

🚀 Features

Identify real file types using magic bytes

Detect mismatches between extension & magic number

Support for common formats:

JPEG, PNG, GIF

PDF

ZIP, GZIP

EXE (Windows PE)

MP3, WAV

Prevents spoofing (e.g., virus.jpg.exe or renamed .exe files)

Zero external dependencies — pure Python

Clean CLI interface

Works on Windows, Linux, and macOS

🛡️ Why This Project? (Cybersecurity Use Case)

Attackers often rename malicious files to bypass filters:

malware.pdf.exe → "looks like PDF"
trojan.jpg → actually an EXE


This tool detects such spoofing by reading the magic number at the start of the file, not the file extension.

Useful for:

Malware analysis labs

Forensics exercises

Red-team / blue-team training

File validation in secure applications

Portfolio projects for cybersecurity students



Run directly with Python (no dependencies):

python file_identifier.py

▶️ Usage
1. Interactive Mode
python file_identifier.py


Then enter:

C:\Users\YourName\Downloads\sample.jpg

2. Direct CLI Argument
python file_identifier.py "C:\path\to\file.pdf"

🧪 Example Output
===== File Type Identification =====
[✓] File Path: /home/user/Downloads/test.png
[✓] Signature Bytes: 89 50 4E 47 0D 0A 1A 0A
[✓] Detected Type: PNG Image
====================================


Unknown/malicious:

[!] Unknown file type (signature not found)


Extension spoofing example:

WARNING: extension does not match detected file type!

📁 Supported Magic Numbers
Format	Magic Number	Example
JPEG	FF D8 FF	image.jpg
PNG	89 50 4E 47	pic.png
GIF	47 49 46 38	gif87a / gif89a
PDF	25 50 44 46	doc.pdf
ZIP	50 4B 03 04	archive.zip
EXE	4D 5A (MZ)	program.exe
GZIP	1F 8B	backup.gz
MP3	49 44 33	song.mp3