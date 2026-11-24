# Tagesaufgaben

Die Übungen werden Schritt für Schritt umfangreicher. Arbeitet in eurem Tempo.

1. **Ticket-Rechner:** Wiederholt Eingaben, Typumwandlung, Rechnung und f-Strings. [Deutsch](01-ticket-rechner/task-de.md) · [English](01-ticket-rechner/task-en.md)
2. **Textwerkstatt:** Bereinigt einen Namen und baut daraus einen Benutzernamen. [Deutsch](02-textwerkstatt/task-de.md) · [English](02-textwerkstatt/task-en.md)
3. **Zeit-Umrechner:** Rechnet Minuten in Stunden und Restminuten um. [Deutsch](03-zeit-umrechner/task-de.md) · [English](03-zeit-umrechner/task-en.md)
4. **Event-Generator:** Erstellt aus Eingaben eine persönliche Event-Seite als HTML. [Deutsch](04-event-generator/task-de.md) · [English](04-event-generator/task-en.md)


## Arbeitsablauf

Öffnet das WSL-Terminal und ersetzt `<URL-des-Repositories>` durch die URL eures GitHub-Repositories:

```bash
git clone <URL-des-Repositories> ILP-21
cd ILP-21
git switch solution
code .
```

Der Branch `solution` ist bereits vorbereitet. Löst dort eure Aufgaben in VS Code und testet eure Programme im WSL-Terminal.

Speichert am Ende eure Dateien und pusht die Ergebnisse aus dem Repository-Ordner auf den Branch `solution`:

```bash
git add .
git commit -m "Tagesaufgabe"
git push origin solution
```

Viel Erfolg!
