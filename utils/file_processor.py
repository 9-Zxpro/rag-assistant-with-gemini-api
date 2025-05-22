import fitz

def process_file(file):
    text=""
    if file.filename.endswith('.pdf'):
        with fitz.open(stream=file.read()) as doc:
            for page in doc:
                text += page.get_text()
    elif file.filename.endswith('.txt'):
        text = file.stream.read().decode('utf-8')
    else:
        raise ValueError("Unsupported file type. Please upload a PDF or TXT file.")
    
    return split_into_chunks(text)

def split_into_chunks(text, chunk_size=200):
    words = text.split()
    chunks=[]
    for i in range(0, len(words), chunk_size):
        chunks.append(' '.join(words[i:i + chunk_size]))

    return chunks
