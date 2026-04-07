from transformers import pipeline

# Load AI model
chatbot = pipeline("text-generation", model="gpt2")

print("AI Chatbot started! (type 'exit' to quit)")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("AI: Goodbye! 👋")
        break
    
    response = chatbot(user_input, max_length=50, num_return_sequences=1)
    
    print("AI:", response[0]['generated_text']) 
