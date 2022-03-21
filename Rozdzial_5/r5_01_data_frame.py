# program r5_01_data_frame.py
# pandas

import sys

try:
    import pandas as pd
    print("Moduł pandas wczytany.")
    import matplotlib.pyplot as plt
    print("Moduł matplotlib obecny.")
except ImportError as impErr:
    print("Brak modułu", impErr.args[0][16:].replace("'", ""))
    print("Zainstaluj: pip install", impErr.args[0][16:].replace("'", ""))
    sys.exit(0)

# Jest ok, działamy dalej
source_data = "http://otwartedane.gdynia.pl/portal/data/city/6/3/data.csv"

# Zapasowa kopia - stan na 16.06.2021 roku
# source_data = "https://raw.githubusercontent.com/abixadamj/helion-python/main/Rozdzial_5/data.csv"
print(f"Dane źródłowe: {source_data}")

# Tworzymy tzw. "DataFrame"
try:
    df = pd.read_csv(source_data)
    print("Pobrano dane źródłowe.")
except:
    print("UWAGA! Wystąpił błąd.")
    exit(0)

# Wyświetlamy dane pobrane z sieci
print("----[ informacje o danych źródłowych ]---")
print(df)
print("----------------")
