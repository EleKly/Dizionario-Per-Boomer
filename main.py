meme_dict = {
        "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
        "LOL": "Una risposta comune a qualcosa di divertente",
        "SHEESH": "leggera disapprovazione",
        "CREEPY": "spaventoso, inquietante",
        "PARA": "preoccuparsi per qualcosa, paranoiarsi",
            }
parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")

while True:
    if parola in meme_dict.keys():
        # Cosa fare se la parola è stata trovata?
        print(parola, meme_dict[parola])
    else:
        # Cosa fare se la parola non è stata trovata?
        print("La parola inserita non è presente nel mio database")
    x = input("Vuoi continuare? y o n?")
    if x == "n" :
        print("Arrivederci")
    break
