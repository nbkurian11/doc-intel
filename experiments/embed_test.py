#initial task 
# Prediction (highest to lowest): A-B, A-C, B-C
# Why: THE FIRST TWO PAIRS, A-B share same meaning, A-C share the word password, B-C have neither

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


sentences = ["How do I reset my password?","I forgot my login credentials and need to get back into my account.", "The password for the meeting room is posted on the whiteboard."]

result = model.encode(sentences)

print(result.shape)

print(model.similarity(result, result))