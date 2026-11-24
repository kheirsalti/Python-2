print("Ticket-Rechner")
name = input("Dein Name : ")
anzahl = int (input ("Anzhal die Tickets : "))

price = float(input("Price die Tickets :"))

print(f"{name} Kauft {anzahl} Tickets")
mul = anzahl * price
print(f"Gesamteprice :  {mul} Euro")