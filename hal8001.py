# Attenzione: versione di chatbot richiesta: 1.0.4
# Attenzione: versione di python richiesta: 3.7.0

# Importazione librerie:
import re
import time
from chatterbot import ChatBot as CB
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

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


linee = open('full_dialog.txt', encoding='utf-8', errors='ignore').read().split('\n')           # Caricamento file di testo

id2line : dict = {}                                         # Creazione di un dizionario che mappa l'ID di ogni linea di dialogo con il proprio testo
lista_linee : list = []

id_conversazione = ''

for linea in linee:
    _linea = linea.split('\t')
    if id_conversazione != _linea[2]:                       # controllo che l'ID della conversazione non sia cambiato
        id_conversazione = _linea[2]                        # se l'id è cambiato, aggiornamento del nuovo controllo con il nuovo ID
        lista_linee : list = []                             # azzeramento della lista lista_linee
        troppo_lunga = False

    lunghezza_linea = len(_linea[1].split())
    if lunghezza_linea <= 30:                                   # se la lunghezza della linea di testo è maggiore di un x numero di parole
        if troppo_lunga == False:                               # controllo che non sia mai stata trovata una frase oltre il limite in questa key del dizionario
            lista_linee.append(pulizia_testo(_linea[1]))        # pulizia testo a aggiunta alla lista lista_linee della linea di conversazione in esame
            id2line[id_conversazione] = lista_linee             # aggiornamento della key del dizionario con la lista_linee aggiornata
        else:
            lista_linee : list = []                             # azzeramento lista
            id2line[id_conversazione] = lista_linee 

    else:
        troppo_lunga = True                                 # set variabile: da qua in poi bisogna azzerare le linee precedenti e non fare scrivere nulla dopo; almeno fino al prossimo cambio di ID
        lista_linee : list = []                             # azzeramento lista
        id2line[id_conversazione] = lista_linee             # inserimento lista azzerata nella chiave del dizionario


condizioni_uscita = ("!exit", "!quit", "!q")                # Creazione oggetto chatbot tramite la libreria chatterbot

chatbot = CB("HALL8000")
trainer = ListTrainer(chatbot)

indice = 0
lista_conversazione : list = []

while indice < len(id2line):                                # ciclo che dura per tutta la lunghezza del dizionario
    lista_conversazione = list(id2line.values())[indice]             
    trainer.train(lista_conversazione)                      # train del bot
    
    indice += 1                                             # avanzamento indice (e quindi key) e conversazione nel dizionario
    lista_conversazione : list = []                         # azzeramento lista, pronta per essere popolata e per nuovo training


print('========== PROGETTO CHATBOT HALL8001 ==========')
print('==========          /start/          ==========/n')
while True:
    query = input("[TU]   > ")
    if query in condizioni_uscita:
        break
    else:
        print(f"[HALL] > {chatbot.get_response(query)}")

print('/n==========           /end/           ==========')
print('========== PROGETTO CHATBOT HALL8001 ==========')
