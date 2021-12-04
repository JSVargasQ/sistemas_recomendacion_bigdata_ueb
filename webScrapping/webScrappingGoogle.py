import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession

def get_source(url):
    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)

def scrape_google(query):

    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.co.uk/search?q=" + query)

    links = list(response.html.absolute_links)
    google_domains = ('https://www.google.',
                      'https://google.',
                      'https://webcache.googleusercontent.',
                      'http://webcache.googleusercontent.',
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')

    for url in links[:]:
        if url.startswith(google_domains):
            links.remove(url)
    return links


def get_results(query):
    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.com.co/search?q=" + query)

    return response


def parse_results(response):
    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = ".IsZvec"

    results = response.html.find(css_identifier_result)

    output = []

    for result in results:
        try:
            texto1=result.find(css_identifier_text, first=True).text
        except:
            texto1="No Encontramos Descripcciones"
        item = {
            'title': result.find(css_identifier_title, first=True).text,
            'link': result.find(css_identifier_link, first=True).attrs['href'],
            'text': texto1
        }

        output.append(item)

    return output

def google_search(query):
    response = get_results(query)
    return parse_results(response)



df = pd.read_csv("https://raw.githubusercontent.com/mcarob/csvPandasVideojuegos/main/pruebaGeneral.csv", delimiter=";")
df = df.drop('Unnamed: 0', axis=1)
nombres=df['Name'].tolist()

print(nombres)
nombres=nombres[696:700]
print(nombres)

def comenzar(nombres):
    habilitados = ["wikipedia", "xbox", "playstation", "steam", "cosola", "videojuegos","games","juego"]
    cantidad = len(nombres)
    print(cantidad)
    resultados = []
    contador=0
    for i in nombres:
        contador+=1
        texto = "No Encontramos Descripcciones"
        results = google_search(i)
        for j in results:
            for k in habilitados:
                if (k in j.get("link")):
                    print(i)
                    try:
                        texto = j.get("text")
                        if("..." in texto):
                            texto=texto[:texto.find("...")]
                    except:
                        pass
                    break
            if (texto != "No Encontramos Descripcciones"):
                break

        pequeResultado = [i, texto]
        resultados.append(pequeResultado)
        print(contador)

    new_list = resultados
    df = pd.DataFrame(new_list)
    writer = pd.ExcelWriter('prueba2.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='respuesta', index=False)
    writer.save()
    print(resultados)


comenzar(nombres)
