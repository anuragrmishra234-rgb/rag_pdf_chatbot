from pypdf import PdfReader

print("Program Started")

reader = PdfReader("data/COMMUNICATION ENGINEERING.pdf")

print("PDF Loaded Successfully")

print("Number of pages:", len(reader.pages))

all_text = ""

for i, page in enumerate(reader.pages):
    print(f"Reading page {i+1}")

    text = page.extract_text()

    if text:
        print("Text found!")
        all_text += text + "\n"
    else:
        print("No text on this page.")

print("\n====================")
print(all_text[:1000])   # Print first 1000 characters