
# Portfolio Flask Project

Dit project bevat een Flask-webapplicatie die is verbonden met een MySQL-database, waarbij mijn persoonlijke interesses worden weergegeven op een webpagina. Hieronder volgt een overzicht van wat ik heb gedaan om de databaseverbinding te testen en de applicatie werkend te krijgen.

## Installatie en Configuratie

### 1. MySQL geïnstalleerd en geconfigureerd
Ik heb MySQL geïnstalleerd en ervoor gezorgd dat de MySQL-client werkt. Daarnaast heb ik de **MySQL bin-directory** toegevoegd aan het systeem-Path, zodat ik de `mysql`-commando's in de terminal kan uitvoeren. Dit heb ik gecontroleerd met:

```bash
mysql --version
```

### 2. Verbinding gemaakt met de MySQL-server
Om verbinding te maken met de MySQL-server op OEGE, heb ik het volgende commando gebruikt:

```bash
mysql -h oege.ie.hva.nl -u geesths -p
```

Daarna heb ik mijn wachtwoord ingevoerd: `NxXY6UbR$/D2nC4P`.

### 3. Database en tabel aangemaakt
Ik heb de database `zgeesths` gebruikt en daarin een tabel aangemaakt voor mijn persoonlijke interesses:

```sql
USE zgeesths;

CREATE TABLE personal_interests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    interest VARCHAR(255) NOT NULL,
    description TEXT
);
```

Vervolgens heb ik mijn persoonlijke interesses toegevoegd:

```sql
INSERT INTO personal_interests (interest, description)
VALUES
('Coding', ' 	Ik doe code.'),
('Traveling', 'vind rijzen leuk.'),
('Reading', ' 	lees veel.');
```

### 4. Flask-applicatie geconfigureerd
In mijn Flask-app heb ik de functie `get_personal_interests` aangepast om de data uit de MySQL-database op te halen:

```python
def get_personal_interests():
    connection = mysql.connector.connect(
        host="oege.ie.hva.nl",
        user="geesths",
        password="NxXY6UbR$/D2nC4P",
        database="zgeesths"
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM personal_interests")
    interests = cursor.fetchall()
    connection.close()
    return interests
```

### 5. Databaseverbinding getest
Om de verbinding met de database te testen, heb ik een nieuwe route toegevoegd aan `app.py`:

```python
@app.route('/check_db_connection')
def check_db_connection():
    try:
        connection = mysql.connector.connect(
            host="oege.ie.hva.nl",
            user="geesths",
            password="NxXY6UbR$/D2nC4P",
            database="zgeesths"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        db_name = cursor.fetchone()
        connection.close()
        return f"Succesvol verbonden met de database: {db_name[0]}"
    except mysql.connector.Error as err:
        return f"Databaseverbinding mislukt. Foutmelding: {err}"
```

Ik heb de verbinding getest door naar de volgende URL te gaan:
```
http://127.0.0.1:5000/check_db_connection
```

### 6. Persoonlijke interesses weergegeven op de webpagina
Om mijn persoonlijke interesses weer te geven, heb ik de route `/personal_interests` toegevoegd:

```python
@app.route('/personal_interests')
def personal_interests():
    try:
        interests = get_personal_interests()
        if not interests:
            return "Geen gegevens beschikbaar."
        return render_template('personal_interests.html', interests=interests)
    except Exception as e:
        return f"Databaseverbinding mislukt: {e}"
```

### 7. HTML-pagina voor persoonlijke interesses
In `personal_interests.html` heb ik een tabel aangemaakt waarin mijn persoonlijke interesses worden weergegeven:

```html
<table>
  <thead>
    <tr>
      <th>Interesse</th>
      <th>Beschrijving</th>
    </tr>
  </thead>
  <tbody>
    {% for interest in interests %}
    <tr>
      <td>{{ interest['interest'] }}</td>
      <td>{{ interest['description'] }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
```

### 8. Applicatie uitgevoerd
Ik heb de Flask-applicatie gestart met het volgende commando:

```bash
flask run
```

Ik heb de verbinding en de persoonlijke interesses gecontroleerd door naar de volgende URL's te gaan:
- Voor de verbindingstest: `http://127.0.0.1:5000/check_db_connection`
- Voor de weergave van persoonlijke interesses: `http://127.0.0.1:5000/personal_interests`

---

Dit document beschrijft de stappen die ik heb uitgevoerd om de MySQL-database in te stellen en de persoonlijke interesses op een webpagina in de Flask-applicatie weer te geven.
