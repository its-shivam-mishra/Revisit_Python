'''

A generator is a special type of function that produces values one at a time instead of 
creating and storing all values in memory at once.

A generator is a Python function that uses yield to lazily produce values one at a time.
It maintains its execution state between iterations, making it memory-efficient 
for processing large or streaming data."

The key difference is:

Normal function → uses return
Generator function → uses yield

'''
def count_numbers():
    for i in range(1, 4):
        yield i

for number in count_numbers():
    print(number)
    
    
    ###########################################
    ###########################################
    
from pypdf import PdfReader


def read_pdf_chunks(file_path, chunk_size=1000):
    reader = PdfReader(file_path)

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""

        # Split page text into smaller chunks
        for i in range(0, len(text), chunk_size):
            chunk = text[i:i + chunk_size]

            yield {
                "page": page_number,
                "text": chunk
            }


# Consume generator
for chunk in read_pdf_chunks("policy.pdf"):
    print("Page:", chunk["page"])
    print(chunk["text"])
    print("-" * 50)