import math


# Definierar funktionen
def f(x):
    return 4.3463 * math.pow(math.e, (0.0079 * x))


# Bestämmer startpunkten
x1, y1 = (280, 38.7)
totalSträcka = 0

# Stegar genom hela definitonsmängden med steglängden 0.1
for i in range(2800, 3920):
    x2 = (i + 1) / 10
    y2 = f(x2)

    # Sträckformeln
    s = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
    totalSträcka += s

    x1 = x2
    y1 = y2

print(totalSträcka)
