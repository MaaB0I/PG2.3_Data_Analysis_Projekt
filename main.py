import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Übung 1: Daten einlesen und inspizieren
path = 'venv/CSV_Files/adult 2.csv'
data = pd.read_csv(path)

# Zeige die ersten und letzten 5 Zeilen
print(data.head())
print(data.tail())

# Zusammenfassung des DataFrames
print(data.info())

# Übung 2: Auswahl und Filterung

# Spalten auswählen und die ersten 10 Zeilen anzeigen
selected_columns = data[['age', 'occupation', 'income']]
print(selected_columns.head(10))

# Zeilen filtern, wo Einkommen > 50K
income_over_50k = data[data['income'] == '>50K']
print(income_over_50k)

# Einträge finden, wo Alter > 30 und Bildung = Bachelors
age_over_30_bachelors = data[(data['age'] > 30) & (data['education'] == 'Bachelors')]
print(age_over_30_bachelors)

# Übung 3: Datenbearbeitung

# Neue Spalte hinzufügen
data['age_decade'] = data['age'] / 10

# Werte in der Spalte 'income' aendern
data['income'].replace({'>50K': 'high', '<=50K': 'low'}, inplace=True)

# Zeilen mit unbekanntem Beruf entfernen
data = data[data['occupation'] != 'Unknown']

# Übung 4: Einfache Datenanalyse

# Deskriptive Statistiken für 'age'
print(data['age'].describe())

# Durchschnittsalter, gruppiert nach Einkommen
print(data.groupby('income')['age'].mean())

# Einzigartige Werte in 'education'
print(data['education'].unique())

# Übung 5: Visualisierung

# Boxplot für 'age' gruppiert nach 'income'
sns.boxplot(x='income', y='age', data=data)
plt.show()

# Scatter Plot für 'age' gegen 'hours-per-week', farbkodiert nach 'income'
sns.scatterplot(x='age', y='hours-per-week', hue='income', data=data)
plt.show()
