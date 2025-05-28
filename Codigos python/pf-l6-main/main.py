import requests

def trivia_fetch(num):
    url = f"http://numbersapi.com/{num}?json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "No se pudo obtener la trivia"}

def main():
  opcion = 0
  print("Bienvenido a la API de Trivias!")
  while opcion != 2:
    print("Selecciona una opción: \n 1) Comenzar trivia \n 2) Salir de la trivia")
    opcion = int(input()) 
    if opcion == 1:
       print ("Ingresa un numero entero para comenzar la trivia: ")
       num = float(input())
       if num % 1 == 0:
          print(trivia_fetch(num))
          print("")
       else:
          print("Opción no valida")
    elif opcion == 2:
       print("Gracias por jugar")
    else:
       print("Opción no valida")
          
if __name__ == "__main__":
    main()


    

