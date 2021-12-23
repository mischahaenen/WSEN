# string format
x = 100/7
y = 2/7
print("Zahlen:", x, y)

# Format e
print(f"Format e Standard: {x:e} {x:e} {y:e}")
print(f"Format e, nach Komma: {x:.3e}")
print(f"Format e, gesamt: {x:12.3e}")

# format f
print(f"Format f, Standard: {x:f} {x:f} {y:f}")
print(f"Format f, nach Komma: {x:.25f}")
print(f"Format f, gesamt: {x:15.10f}" )

# Format %
print(f"Format % Standard: {x:%} {y:%}")
print(f"Format %, nach Komma: {y:.3%}")
print(f"Format %, gesamt: {y:12.3%}")

# Tabelle mit verschiedenen Objekten
artname ={23:"Apfel",8:"Banane",42:"Pfirsisch"}
anzahl ={23:1, 8:3, 42:5}
epreis ={23:2.95, 8:1.45, 42:3.05}
print(f"{'Nr':>4}{'Name':>12}{'Anz':>4}{'EP':>13}{'GP':>13}")
for x in 23, 8, 42:
    print(f"{x:04d}{artname[x]:>12}{anzahl[x]:4d}{epreis[x]:8.2f} Euro {anzahl[x]*epreis[x]:8.2f} Euro")

