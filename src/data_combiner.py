def combine_data():
    try:
        with open("data/website_text.txt", "r", encoding="utf-8") as f:
            website_text = f.read()
        with open("data/pdf_text.txt", "r", encoding="utf-8") as f:
            pdf_text = f.read()
        combined_text = f"WEBSITE CONTENT:\n{website_text}\n\nPDF CONTENT:\n{pdf_text}"
        with open("data/combined_data.txt", "w", encoding="utf-8") as f:
            f.write(combined_text)
        print("Data combined successfully!")
    except FileNotFoundError:
        print("Error: Missing input files.")

combine_data()