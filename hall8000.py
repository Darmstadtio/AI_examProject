# Importazione librerie:
from chatterbot import ChatBot

# Creazione oggetto chatbot tramite la libreria chatterbot
chabot = ChatBot("HALL8000")

exit_conditions = ("!exit", "!quit")

while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"-.-{chatbot.get_response(query)}")
