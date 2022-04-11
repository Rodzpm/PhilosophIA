import os
import openai
from googletrans import Translator
cls = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

openai.api_key = "Put your key here" 
lang = "fr" #Default language: French

def rep(query):
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Summarize this for a second-grade student:\n"+query,
    temperature=0.7,
    max_tokens=3000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response.choices[0].text

def run():
    cls()
    logo = """    
  ____  _     _ _                       _     ___    _    
 |  _ \| |__ (_) | ___  ___  ___  _ __ | |__ |_ _|  / \   
 | |_) | '_ \| | |/ _ \/ __|/ _ \| '_ \| '_ \ | |  / _ \  
 |  __/| | | | | | (_) \__ \ (_) | |_) | | | || | / ___ \ 
 |_|   |_| |_|_|_|\___/|___/\___/| .__/|_| |_|___/_/   \_\\
                                 |_|                      
    """
    print(logo,"\n")
    ans = input("[1] Lancer\n[2] Quitter\n - ")
    if ans == "1":
        translator = Translator()
        r = input("\nVotre texte (le copier sur une seule ligne): ")
        print("\nAnalyse en cours...\n")
        print(translator.translate(rep(translator.translate(r, dest='en').text), dest=lang).text)
        input("\nAppuyer sur une touche pour continuer...")
        run()
    if ans == "2":
        pass
    else:
        input("Veuillez entrer une réponse valide\nAppuyer sur une touche pour continuer...")
    

if __name__ == "__main__":
    run()
