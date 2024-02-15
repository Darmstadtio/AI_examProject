# Attenzione: versione di chatbot richiesta: 1.0.4
# Attenzione: versione di python richiesta: 3.7.0

# Importazione librerie:
import re
import time
from chatterbot import ChatBot as CB
from chatterbot.trainers import ListTrainer

#==============================================================

# Definizioe funzione di pulizia del testo
def pulizia_testo(testo):

    # Impostazione testo in minuscolo
    testo = testo.lower()
    
    testo = re.sub(r"i'm", "i am", testo)
    testo = re.sub(r"he's", "he is", testo)
    testo = re.sub(r"she's", "she is", testo)
    testo = re.sub(r"it's", "it is", testo)
    testo = re.sub(r"that's", "that is", testo)
    testo = re.sub(r"what's", "that is", testo)
    testo = re.sub(r"where's", "where is", testo)
    testo = re.sub(r"how's", "how is", testo)
    testo = re.sub(r"\'ll", " will", testo)
    testo = re.sub(r"\'ve", " have", testo)
    testo = re.sub(r"\'re", " are", testo)
    testo = re.sub(r"\'d", " would", testo)
    testo = re.sub(r"\'re", " are", testo)
    testo = re.sub(r"won't", "will not", testo)
    testo = re.sub(r"can't", "cannot", testo)
    testo = re.sub(r"n't", " not", testo)
    testo = re.sub(r"n'", "ng", testo)
    testo = re.sub(r"'bout", "about", testo)
    testo = re.sub(r"'til", "until", testo)
    testo = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", testo)
    
    return testo

# ============================================================

# Definizione funzione di importazione testo
def preparazione_database():
    # Caricamento file di testo
    linee = open('movie_lines.txt', encoding='utf-8', errors='ignore').read().split('\n')
    linee_conversazioni = open('movie_conversations.txt', encoding='utf-8', errors='ignore').read().split('\n')


    # Creazione di un dizionario che mappa l'ID di ogni linea di dialogo con il proprio testo
    id2line = {}
    for linea in linee:
        _linea = linea.split(' +++$+++ ')
        if len(_linea) == 5:
            id2line[_linea[0]] = _linea[4]


    # Creazione di una lista con tutti gli ID delle linee di conversazione
    convs = [ ]
    for linea in linee_conversazioni[:-1]:
        _linea = linea.split(' +++$+++ ')[-1][1:-1].replace("'","").replace(" ","")
        convs.append(_linea.split(','))


    # Creazione liste da popolare
    lista_domande = []
    lista_risposte = []

    # Divisione e ordinamento delle frasi in nelle due liste di domande (input) e risposte (output)
    for conv in convs:
        for i in range(len(conv)-1):
            lista_domande.append(id2line[conv[i]])
            lista_risposte.append(id2line[conv[i+1]])

    # A questo punto dovremmo avere due liste, domande e risposte, contenenti ciascuna tutte le frasi del database

    # Pulizia del testo
    # Creazione liste per frasi ripulite, da popolare
    lista_domande_pulite = []
    lista_risposte_pulite = []    

    # Cicli for che prendono in ingresso la linee di testo de lista_domande e lista_risposte,
    # le danno in pasto alla funzione pulizia_testo e popolano le liste_domande/risposte_pulite
    for domanda in lista_domande:
        lista_domande_pulite.append(pulizia_testo(domanda))
        
    for risposta in lista_risposte:
        lista_risposte_pulite.append(pulizia_testo(risposta))

    # ====
    # per non avere q&a composti da frasi troppo lunghe, o domanda e risposta rispettivamte troppo
    # o troppo poco lughi, è bene fare una cernita 'incrociata'

    # Impostiano una lunghezza minima ed una massima del numero di parole che q&a può avere
    min_lunghezza_linea = 2
    max_lunghezza_linea = 20

    # Filter out the domandas that are too short/long
    domande_brevi_temp = []
    risposte_brevi_temp = []

    i = 0
    for domanda in lista_domande_pulite:
        if len(domanda.split()) >= 2 and len(domanda.split()) <= 20:
            domande_brevi_temp.append(domanda)
            risposte_brevi_temp.append(lista_risposte_pulite[i])
        i += 1

    # Filter out the rispostas that are too short/long
    domande_brevi = []
    risposte_brevi = []

    i = 0
    for risposta in risposte_brevi_temp:
        if len(risposta.split()) >= 2 and len(risposta.split()) <= 20:
            risposte_brevi.append(risposta)
            domande_brevi.append(domande_brevi_temp[i])
        i += 1
    
    return domande_brevi
   
"""
    limit = 0
    for i in range(limit, limit+5):
        print(domande_brevi[i])
        print(risposte_brevi[i])
        print()
"""

#########################################################

# Creazione oggetto chatbot tramite la libreria chatterbot
chatbot = CB("HALL8000")

condizioni_uscita = ("!exit", "!quit", "!q")
nome_lista : list = preparazione_database

for i in range(10):
    print(nome_lista[i])

trainer = ListTrainer(chatbot)
trainer.train(nome_lista)

while True:
    query = input("[TU]   > ")
    if query in condizioni_uscita:
        break
    else:
        print(f"[HALL] > {chatbot.get_response(query)}")
