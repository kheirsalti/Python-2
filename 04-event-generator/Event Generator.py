import random

event_number = random.randint(1000, 9999)

ev_n = input("Enter Event Name : ")
ev_ort = input("Enter Event ort : ")
ev_be = input ("Enter Event Beschreibung : ")
m_p = int(input("Enter Maximale Pläze : "))
anm = int(input("Enter Bisherige Anmeldungen : "))
f_p = m_p - anm
f_v = f_p > 0

html =f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{ev_n}</title>
</head>
<body>
    <h1>{ev_n}</h1>
    <p>{ev_be}</p>

    <h2> Eventdaten</h2>
    <ul>
        <li>Eventnummer:{event_number} </li>
        <li>Ort:{ev_ort} </li>        
    </ul>

    <h2>Plätze</h2>
    <ul>
        <li>Maximale Plätze:{m_p}</li>
        <li>Anmeldungen:{anm}</li>
        <li>Freie Plätze:{f_p}</li>
        <li>Pläzte verfügbar:{f_v}</li>
    </ul>

</body>
</html>"""
print(html)
with open("event.html", "w", encoding="utf-8") as file:
    file.write(html)
