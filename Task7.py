menu = {'Lagman': 120, 'Plov': '120', 'Borsh': 100}
menu['Besh barmak'] = 130
print(menu)
menu['Besh barmak'] = 135
print(menu)

del menu['Borsh']
print(menu)