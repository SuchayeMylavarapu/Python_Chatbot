from chatbot import chatbot
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(ChatBot)

trainer.train([
    "How are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you",
    "You are welcome.",
])