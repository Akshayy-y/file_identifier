import os
import sys

# -------------------------------------------
# Magic Number Signatures Dictionary
# -------------------------------------------
SIGNATURES = {
    b"\xFF\xD8\xFF": "JPEG Image",
    b"\x89PNG": "PNG Image",
    b"%PDF": "PDF Document",
    b"PK\x03\x04": "ZIP Archive",
    b"PK\x05\x06": "ZIP Archive (Empty)",
    b"PK\x07\x08": "ZIP Archive (Spanned)",
    b"MZ": "Windows Executable (EXE)",
    b"GIF87a": "GIF Image (GIF87a)",
    b"GIF89a": "GIF Image (GIF89a)",
    b"ID3": "MP3 Audio (ID3 Tag)",
    b"\xFF\xFB": "MP3 Audio (MPEG1 Layer III)",
    b"RIFF": "WAV Audio",
    b"\x1F\x8B": "GZIP Archive",
}


# -------------------------------------------
# Read File’s Magic Bytes
# -------------------------------------------
def read_magic_bytes(file_path, num_bytes=16):
    """
    Reads the first N bytes from a file.
    """
    try:
        with open(file_path, "rb") as f:
            return f.read(num_bytes)
    except FileNotFoundError:
        print(f"[!] File not found: {file_path}")
        sys.exit(1)
    except PermissionError:
        print(f"[!] Permission denied: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"[!] Error: {e}")
        sys.exit(1)


# -------------------------------------------
# Identify File Type Using Magic Numbers
# -------------------------------------------
def identify_file_type(magic_bytes):
    """
    Matches file signatures from the SIGNATURES dictionary.
    """
    for signature, file_type in SIGNATURES.items():
        if magic_bytes.startswith(signature):
            return file_type
    return None


# -------------------------------------------
# Main Program (CLI)
# -------------------------------------------
def main():
    # Case 1: File path passed as CLI argument
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        # Case 2: Ask user for file path
        file_path = input("Enter file path: ").strip().strip('"')

    # Validate path
    if not os.path.isfile(file_path):
        print(f"[!] Invalid file path: {file_path}")
        sys.exit(1)

    # Read the magic bytes
    magic_bytes = read_magic_bytes(file_path)

    # Identify file type
    detected_type = identify_file_type(magic_bytes)

    # Print Results
    print("\n===== File Type Identification =====")
    print(f"[✓] File Path: {file_path}")
    print("[✓] Signature Bytes:", " ".join(f"{b:02X}" for b in magic_bytes[:8]))

    if detected_type:
        print(f"[✓] Detected Type: {detected_type}")
    else:
        print("[!] Unknown file type (signature not found).")

    print("====================================\n")


# -------------------------------------------
# Run Code
# -------------------------------------------
if __name__ == "__main__":
    main()
