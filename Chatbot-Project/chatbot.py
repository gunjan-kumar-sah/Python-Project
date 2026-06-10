# Smart Q&A Chatbot

print("=" * 40)
print("      SMART Q&A CHATBOT")
print("=" * 40)
print("Type 'exit' to quit the chatbot.\n")

# Questions and Answers
responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi! Nice to meet you.",
    "how are you?": "I am fine. Thank you for asking.",
    "what is your name?": "My name is Smart Q&A Chatbot.",
    "who created you?": "I was created using Python.",
    "what is python?": "Python is a popular programming language.",
    "what is cyber security?": "Cyber Security protects systems and data from cyber attacks.",
    "what is ethical hacking?": "Ethical Hacking is finding vulnerabilities legally to improve security.",
    "what is ai?": "AI stands for Artificial Intelligence.",
    "thank you": "You're welcome!",
    "thanks": "Glad to help!",
    "bye": "Goodbye! Have a great day."
}

# Chat Loop
while True:
    
    user = input("You: ").lower().strip()

    if user in ["exit", "quit", "bye"]:
        print("Bot: Goodbye! 👋")
        break

    if user in responses:
        print("Bot:", responses[user])
    else:
        print("Bot: Sorry, I don't understand that question.")