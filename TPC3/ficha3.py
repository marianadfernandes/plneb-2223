import re
import unidecode

file = open('dicionario_medico.txt', encoding="UTF8")

text = file.read()

# tornar caso único de descrição iniciada por minuscula em maiuscula
text = re.sub(r'^do (lat|gr)', lambda match: match.group(0).capitalize(), text, flags=re.MULTILINE)

# marcação de todos os termos
text = re.sub(r'\n\n(.*)((?:\n[0-9A-ZÁÀÂÉÍÓÚ])|(?:\n\n?\f[0-9A-ZÁÀÂÉÍÓÚ]))', r'\n\n#T=\1\2', text)

# remoção de \n encontrados no meio de descrições 
text = re.sub(r'\n\f', r'\f', text)

# remoção de todos os \f e marcação de termos
text = re.sub(r'\f', r'', text)
text = re.sub(r'#T=', r'', text)

# foi acrescentado \n? em relação à resolução da aula para captar \n entre termo e descrição
entries = re.findall(r'\n\n(.+)(\n?(?:\n.+)+)', text)

new_entries = []

new_entries = [(designation, description.strip()) for designation, description in entries]

file.close()

html = open('tpc3_dicionario.html', 'w', encoding='UTF8')

header = '''<html>
                <head>
                    <meta charset="utf-8"/>
                    <title>Dicionário Médico</title>
                    <style>
                        body {
                            background-color: #3b5249;
                            font-family: century gothic;
                        }
                        th, td{
                            border: 1px solid black;
                            border-collapse: collapse;
                            border-radius: 10px;
                            border-style: ridge;
                        }
                        th, tr:nth-child(even){
                            background-color: #a4b494;
                        }
                        tr:nth-child(odd){
                            background-color: #bec5ad;
                        }
                        td:nth-child(odd){
                            text-align: center;
                            font-weight: bold;
                        }
                        td:nth-child(even){
                            padding-left: 20px;
                        }
                        .container {
                            display: grid;
                            grid-template-columns: 1fr 20fr;
                        }
                        .box {
                            position: -webkit-sticky;
                            position: -moz-sticky;
                            position: -ms-sticky;
                            position: -o-sticky;
                            position: sticky;
                            top: 2px;
                            bottom: auto;
                            display: inline-block;
                            vertical-align: top;
                            height: 97vh;
                            overflow: auto;
                            text-align: center;
                            padding-top: 5px;
                            font-size: 1.2em;
                            line-height: 1.1em;
                            background-color: #bec5ad;
                            border-radius: 10px;
                            border: 1px solid black;
                            cursor: pointer;
                        }
                    </style>
                </head>
                <body>
                    <div class="container">
                        <div id="nav" class="box">'''

sidebar = ''
for i in range(ord('A'), ord('Z') + 1):
        sidebar += '<a href="#' + chr(i)+ '">' + chr(i) + '</a><br>'
                    
header2 = '''      </div>
                        <div class="table">
                            <table>
                                <tr>
                                    <th colspan="2">Dicionário Médico</th>
                                <tr>
                                    <th>Designação</th>
                                    <th>Descrição</th>
                                </tr>   
        '''

body = ''
i=0
for designation, description in new_entries:
    body += '<tr>'
    if i == 0:
        ascii = ord('A')
        body += '<td id="A">'+ designation + '</td>'
    elif i != 0 and (unidecode.unidecode(new_entries[i][0][0]).casefold() != unidecode.unidecode(new_entries[i-1][0][0]).casefold()):
        href = new_entries[i][0][0].upper()
        body += '<td id="'+ href + '">'+ designation + '</td>'  
    else:
        body += '<td>' + designation + '</td>'
    body += '<td>' + description + '</td>'
    body += '</tr>'
    i += 1

footer = '''    </table>
            </div>
        </div>
    </body>
</html>'''

html.write(header + sidebar + header2 + body + footer)

html.close()