import re
import random
import sys

# --------- Rules: patterns -> responses ----------
RULES = [
    # greetings
    (r'\b(hi|hello|hey|hiya|good (morning|afternoon|evening))\b',
     ["Hello! 👋 How can I help you today?", "Hi there! What would you like to do?"]),
    
    # farewells
    (r'\b(bye|goodbye|see you|see ya|talk later|farewell)\b',
     ["Goodbye! Have a great day.", "Bye — take care!"]),
    
    # how are you
    (r"\b(how are you|how's it going|how are things)\b",
     ["I'm a chatbot, but I'm doing great — thanks! How about you?",
      "All good here! What can I do for you?"]),
    
    # ask name
    (r"\b(what('s)? your name|who are you|your name)\b",
     ["I'm a simple rule-based chatbot.", "You can call me RuleBot."]),
    
    # thanks
    (r'\b(thanks|thank you|thx)\b',
     ["You're welcome!", "No problem — happy to help!"]),
    
    # help / capabilities
    (r'\b(help|what can you do|capabilities|features)\b',
     ["I can greet you, answer simple questions, and say goodbye. "
      "Try: 'hi', 'what's your name?', 'how are you?', 'bye'."]),
    
    # ask time/date
    (r'\b(time|date)\b',
     ["I can't access the real time in this simple demo, "
      "but you can check your system clock!"]),
]

FALLBACK_RESPONSES = [
    "Sorry, I didn't understand that. Can you rephrase?",
    "I'm not sure about that. Try asking something simpler (e.g., 'hi', 'help', 'bye')."
]

# --------- Preprocessing ----------
def normalize(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'[^\w\s]', ' ', text)  # remove punctuation
    text = re.sub(r'\s+', ' ', text)      # collapse spaces
    return text

# --------- Matching ----------
def match_rule(text: str):
    for pattern, responses in RULES:
        if re.search(pattern, text):
            return random.choice(responses)
    return None

# --------- Conversation loop ----------
def main():
    print("RuleBot: Hello! (type 'quit' or 'bye' to exit)")
    while True:
        try:
            user = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nRuleBot: Bye!")
            break

        if not user.strip():
            print("RuleBot: I didn't catch that — say something or type 'help'.")
            continue

        norm = normalize(user)

        # exit keywords
        if re.search(r'\b(quit|exit|bye|goodbye)\b', norm):
            print("RuleBot: Goodbye! 👋")
            break

        response = match_rule(norm)
        if response:
            print(f"RuleBot: {response}")
        else:
            print(f"RuleBot: {random.choice(FALLBACK_RESPONSES)}")

if __name__ == '__main__':
    main()
