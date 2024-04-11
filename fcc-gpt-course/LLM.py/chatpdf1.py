import argparse
from pdfminer.high_level import extract_text
from sentence_transformers import SentenceTransformer, CrossEncoder

def embed(window_size, step_size):
    pdf_filename = "supernova_poster_back.pdf"  # Specify the PDF filename here
    text = extract_text(pdf_filename)
    text = "".join(text.split())
    text_tokens = text.split()
    
    sentences = []
    for i in range(0, len(text_tokens), step_size):
        window = text_tokens[i: i + window_size]
        if len(window) < window_size:
            break
        sentences.append(window)
        
    paragraphs = ["".join(s) for s in sentences]
    print(paragraphs)

    model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
    model.max_seq_length = 512
    cross_encoder = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
    
    embeddings = model.encode(paragraphs, show_progress_bar=True)
    return model, cross_encoder, embeddings, paragraphs

if __name__ == "__main__":
    window_size = 128
    step_size = 100

    model, cross_encoder, embeddings, paragraphs = embed(window_size, step_size)
    print(embeddings[0].shape)

