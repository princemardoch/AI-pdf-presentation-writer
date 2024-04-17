import pdfkit
from expose import write_expose

print('\n')
theme = input("Theme : ")

expose_list = write_expose(theme)


def write_in_html():
    p = '1'
    with open('expo.html', 'w') as clear:
        clear.write('')

    with open('expo.html', 'a') as w:
        w.write(""" 
                
                <!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exposé</title>
</head>
                <body>
        <section class="page_de_garde">
            <p class="copyr"> TeamLPM © tous droits réservés <br> Fait sur : WWW.GPTCORRECT.COM </p>
        </section>
        <section class="corps_expose"> """)

        for i in expose_list:
            w.write(f"""
            <section class="page {p.zfill(2)}">
                <p> {i} </p>
            </section> """)
            p = str(int(p) + 1)
        w.write("""
                
                </section>

                <style> * { margin: 0; padding: 0; font-family: Century Gothic; } corps_expose{display:flex; flex-direction:column;} p { font-size: 30px; padding: 40px 0px; } img { width: 800px; } .page_de_garde { height: 1288px; border-bottom: 5px solid black; } .page { page-break-before: always;} .copyr { color: gray; display: flex; font-size: 10px; text-align: center; align-content: center; align-items: center; justify-content: center; padding-top: 0px; } </style>
    
</body>
</html>
                
                """)

write_in_html()

config = pdfkit.configuration(wkhtmltopdf="/usr/local/bin/wkhtmltopdf")
# pdfkit.from_url('https://fr.wikipedia.org/wiki/Pablo_Escobar', 'test2.pdf', configuration=config)

# Chemin local vers le fichier HTML
chemin_fichier_html = 'expo.html'

from random import choice
def gen_name():
    caracteres = '1234567890azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN'
    liste_caracteres = []

    for _ in range(10):
        liste_caracteres.append(choice(caracteres))
    nom_fichier = ''.join(liste_caracteres)
    return nom_fichier

nom_fichier = gen_name()

# Chemin de sortie du fichier PDF
chemin_fichier_pdf = f'{nom_fichier}.pdf'

# Convertir le fichier HTML en PDF
pdfkit.from_url(chemin_fichier_html, chemin_fichier_pdf, configuration=config)



