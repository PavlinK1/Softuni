#Key
countries = input().split(', ')
#Values
capitals = input().split(', ')

zipped_dict = dict(zip(countries, capitals))

for(country, capital) in zipped_dict.items():
    print(f"{country} -> {capital}")
