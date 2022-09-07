# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# ¬ not
# ⋁ or
# ⋀ and

x = int(input('ВВедите X: '))
y = int(input('ВВедите Y: '))
z = int(input('ВВедите Z: '))

if not(x or y or z) == (not x and not y and not z):
    print(True)
else:
    print(False)