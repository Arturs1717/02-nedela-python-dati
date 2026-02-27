text = "Sveiki"
skaitlis = 10
decimals = 3.14
patiesiba = True
nekas = None

print(type(text))
print(type(skaitlis))
print(type(decimals))
print(type(patiesiba))
print(type(nekas))

print(bool(""))      # False - tukša virkne
print(bool("abc"))   # True - netukša virkne
print(bool(0))       # False - nulle
print(bool(5))       # True - nenulles skaitlis
print(bool(None))    # False

print(int("5") + 3)      # 8
print(float("3.14"))     # 3.14
print(str(100))          # "100"

# robežgadījumi
# print(int("abc"))      # ValueError
print(int(3.86))         # 3