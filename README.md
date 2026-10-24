# doc-intel

Upload a document and ask questions about it in plain English. Answers are grounded in the document's actual content and cite their sources.

> **Status: in development.** This README describes the project plan. Items are checked off as they are built.

## What it does

doc-intel is a retrieval-augmented generation (RAG) app. Instead of pasting a whole document into an LLM, it finds the passages most relevant to your question and gives only those to Claude. This keeps answers grounded, reduces hallucination, and scales to documents too large for a single prompt.

## How it works

**Index time (once per document)**
1. Extract text from the uploaded file
2. Split the text into overlapping chunks
3. Embed each chunk into a vector
4. Store the vectors with their source info (file name, page)

**Query time (every question)**
1. Embed the question with the same embedding model
2. Find the top-k most similar chunks (cosine similarity)
3. Send those chunks plus the question to Claude, instructing it to answer only from them
4. Return the answer with source citations

## Planned tech stack

| Layer | Choice |
|---|---|
| Backend | Python, Flask |
| Embeddings | `sentence-transformers` (`all-MiniLM-L6-v2`), run locally |
| Vector store | Supabase (Postgres + pgvector) |
| LLM | Claude API |
| Frontend | React, Tailwind CSS |
| Deployment | Vercel (frontend), Render (backend) |


## Getting started

Setup instructions will be added as the project takes shape. Planned requirements:

- Python 3.11+
- A Claude API key, stored in a `.env` file (never committed)
- A Supabase project (free tier)


