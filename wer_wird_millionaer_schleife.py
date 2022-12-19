fragen = [
    "100 € Frage: Wo findet die Fußball WM 2022 statt?",
    "200 € Frage: Wie heißt die Straße, an der die Gesamtschule Wasseramselweg liegt?",
    "300 € Frage: In welchem Fußballverein spielt Mbappé?",
    "400 € Frage: Welche Farbe ergibt sich, wenn man blau und rot mischt?",
    "1000 € Frage: Wer hat die WM 2022 gewonnen?",
    "2000 € Frage: Was ist das höchste Gebäude in Köln?"
]

antworten = [
    "Katar",
    "Am Wassermann",
    "PSG",
    "lila",
    "Argentinien",
    "Colonius"
    ]

for i in range(len(fragen)):
    print(fragen[i])

    antwort = input()

    if antwort == antworten[i]:
        print("RICHTIG!")
    else:
        print("Leider falsch!")
        print("Die richtige Antwort ist: ", antworten[i])

    print("-"*100)