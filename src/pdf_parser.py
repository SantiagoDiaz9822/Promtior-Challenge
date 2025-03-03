from PyPDF2 import PdfReader

def parse_pdf(file_path):
    text = ""
    try:
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        print(f"PDF parsing failed: {e}")
        return ""

# Save parsed PDF text to a file
pdf_text = parse_pdf("data/Challenge_AI_Engineer-Promtior.pdf")
with open("data/pdf_text.txt", "w", encoding="utf-8") as f:
    f.write(pdf_text)