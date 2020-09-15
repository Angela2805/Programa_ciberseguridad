try: 
    import os
except ImportError: 
    os.system('pip install os') 
    print('Installing os...') 
    print('Ejecuta de nuevo tu script...') 
    exit() 
try: 
    import requests
except ImportError: 
    os.system('pip install request') 
    print('Installing request...') 
    print('Ejecuta de nuevo tu script...') 
    exit() 
try: 
    import sys
except ImportError: 
    os.system('pip install sys') 
    print('Installing sys...') 
    print('Ejecuta de nuevo tu script...') 
    exit() 
try: 
    from bs4 import BeautifulSoup as bs
except ImportError: 
    os.system('pip install bs4') 
    print('Installing bs4...') 
    print('Ejecuta de nuevo tu script...') 
    exit() 
try: 
    import webbrowser 
except ImportError: 
    os.system('pip install webbrowser') 
    print('Installing webbrowser...') 
    print('Ejecuta de nuevo tu script...') 
    exit() 
#Angela Guadalupe García Ibarra
"""Este programa utiliza la librería webbroswer para abrir la página deseada
    La librería bs4 para ver si la página está en función y su estatus
    y las librerías os y sys para poder tener acceso a realizar modificaciones 
    en el sistema 
"""

print("Este script navega en las páginas de noticas de la UANL")
inicioRango = int(input("Pagina inicial para buscar: "))
finRango = int(input("Pagina final para buscar: "))
dependencia = input("Ingrese las siglas de la Facultad a buscar: ")
#con este if hacemos que empecemos con el número más alto
if inicioRango > finRango:
    inicioRango,finRango = finRango,inicioRango
for i in range (inicioRango,finRango,1):
    url = "https://www.uanl.mx/noticias/page/"+str(i)
    pagina = requests.get (url)
    #En caso de encontrar error con el estatus de la página mostrará "Página no encontrada"
    if pagina.status_code != 200:
        raise TypeError("Página no encontrada")
    else:
        soup = bs(pagina.content,"html.parser")
        info = soup.select("h3 a")
        for etiqueta in info:
            url2 = etiqueta.get("href")
            pagina2 = requests.get(url2)
            if pagina2.status_code == 200:
                soup2 = bs(pagina2.content,"html.parser")
                parrafos = soup2.select("p")    
                for elemento in parrafos:
                    if dependencia in elemento.getText():
                        print ("Abriendo",url2)
                        webbrowser.open(url2)
                        break
    

