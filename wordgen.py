## from standard library
import random
import time


#### dependencies

try:
    import pyperclip
    print('[pyperclip module loaded]')
except ImportError:
    print('Error, pyperclip is required, please install it using "pip install pyperclip"')


try:
    import pynput
    from pynput import keyboard
    print('[pynput module loaded]')
except ImportError:
    print('Error, pynput is required, please install it using "pip install pynput"')
    


####



#### Version notes
# GIT RELEASE 2.5.2 (Final)

#### Istruzioni
# Premi [ALT + b] per generare una frase casuale e metterla negli appunti
# Premi [ALTGR + m] per fermare lo script completamente
print("-[INFO]-------------")
print("Premi [ALT + b] per generare una frase casuale e metterla negli appunti.")
print("Per chiudere lo script, chiudi semplicemente il terminale.")
print("--------------------")

#################### Inizio dizionario ####################
# Il dizionario è suddiviso in tuples, index = 0: singolari; index = 1: plurali.

Cose = [
    
    ("un cane", "i cani"),
    ("un coniglio", "i conigli"),
    ("Mario", "delle mele")

    ]

Verbi = [

    ("è come", "sono come"),
    ("mangia", "mangiano"),
    ("prende a pugni", "prendono a pugni"),

    ]






Avverbi = [
    "con molta forza", "abilmente", "orribilmente", "terribilmente",
]

Collegamenti = [

    "poichè", "perchè", "dato che",
    "poi", "in seguito",
    "e", 
    "eppure", "ma",
    "e nel mentre", "mentre", 
    "quando all'improvviso"

]


#################### Fine dizionario #################### 




#### Generatore di proposizione
def gen_prop():

    pluralità = random.randint(0, 1)
    avverbio = random.randint(0, 5)

    def avv():
        if avverbio == 0:
            return random.choice(Avverbi)
        else:
            return ""


    parola1 = random.choice(Cose)
    parola2 = random.choice(Verbi)
    parola3 = random.choice(Cose)



    return( 

    parola1[pluralità], 
    
    avv(),

    parola2[pluralità], 
    
    parola3[random.randint(0, 1)], 
    
    avv()
    
    )

#### Generatore di periodi


def gen_periodi():

    def agg_proposizione():
        collegamento = random.choice(Collegamenti)
        return (collegamento, *gen_prop())
    
    def bonus():
        bonus1 = random.randint(0, 7)
        if bonus1 == 0:
            return agg_proposizione()
        else:
            return ""

    
    risultato = (*gen_prop(), *bonus(), *bonus())
    stringa_ris = ' '.join(map(str, risultato))
    output = (stringa_ris.replace("  "," "))
    return output

#### DEBUG SECTION
#(none)

#### RUN SECTION

def RUN():
    # Run main funcition
    gen_periodi()

    # Copies output to clipboard
    output = gen_periodi()
    pyperclip.copy(output)

    # Print (and shows) what's been copied to the clipboard
    print(output)


### COMBINAZIONE PER AGGIORNARE SCRIPT
def Key_listnerS():

    ### combinazioni di tasti di trigger
    COMBINATIONS = [
        {keyboard.Key.alt, keyboard.KeyCode(char="b")},
    ]

    def execute():
        ### inserisci evento
        RUN()

    ## key listener code
    current = set()
    def on_press(key):
        if any([key in COMBO for COMBO in COMBINATIONS]):
            current.add(key)
            if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
                execute()

    def on_release(key):
        if any([key in COMBO for COMBO in COMBINATIONS]):
            current.remove(key)

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


Key_listnerS()
