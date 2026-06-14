from pypdf import PdfReader # type: ignore
import io

def extract_resume_text(pdf_bytes):
    reader = PdfReader(io.BytesIO(pdf_bytes))
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"
    return text

def extract_section(text, start_keyword, end_keyword):
    start_index = text.find(start_keyword)

    if start_index == -1:
        return ""

    start_index += len(start_keyword)

    end_index = text.find(end_keyword, start_index)

    if end_index == -1:
        return text[start_index:].strip()

    return text[start_index:end_index].strip()