input_filename = 'country_info.txt'

countries = {}
with open(input_filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }
        # print(country_dict)
        countries[country.casefold()] = country_dict

print(countries)

# print("Choose one of the following countries: ")
# for country in countries:
#     print(country)
# input_country = input("> ")
# print(countries[input_country]['capital'])
