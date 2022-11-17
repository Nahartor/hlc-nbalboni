#Importar la libreria de csv de Python
#import csv

#Importar módulos concretos
from csv import DictReader, DictWriter

file_men_names="/home/nbalboni/github/hlc-nbalboni/ManejoArchivos/NombresComunesHombre.csv"
file_women_names="/home/nbalboni/github/hlc-nbalboni/ManejoArchivos/NombresComunesMujer.csv"
file_men_names_v2="/home/nbalboni/github/hlc-nbalboni/ManejoArchivos/NombresComunesHombre_v2.csv"

men_names=[]
women_names=[]

#Cargamos los nombres de mujer a una lista de diccionario
try:
    with open(file_women_names, 'r') as File:
        reader = DictReader(File)
        for row in reader:
            women_names.append(row)

except FileNotFoundError:
    print("El archivo {file_women_names} no existe, no se han podido cargar los nombres.")
except:
    print("Se ha producido un error inesperado.")
else:
    print(women_names)

#Cargamos los nombres de hombre a una lista de diccionario
try:
    with open(file_men_names, 'r') as File:
        reader = DictReader(File)
        for row in reader:
            men_names.append(row)

except FileNotFoundError:
    print("El archivo {file_men_names} no existe, no se han podido cargar los nombres.")
except:
    print("Se ha producido un error inesperado.")
else:
    print(men_names)

#Guardar datos en un archivo csv
header=["Numero","Nombre","Frecuencia","DeCadaMil"]

new_name={"Numero":"101", "Nombre":"LEO", "Frecuencia":"3", "DeCadaMil":"1"}

with open(file_men_names_v2, 'w') as File:
    writer= DictWriter(File,header)
    writer.writeheader()
    writer.writerows(men_names)
    writer.writerow(new_name)