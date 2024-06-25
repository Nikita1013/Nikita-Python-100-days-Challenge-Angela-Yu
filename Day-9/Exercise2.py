travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille","Dijon"],
        "total_visited" : 12
    },
    {
        "country": "Germany",
        "citied_visited": ["Berlin","Hamburg","Munich"],
        "total_visited" : 5
    },
]

# TODO: Write the functin that will allow new country to be added to the travel_log
def add_new_country(country_visited,cities_visited, times_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["cities_visited"] = cities_visited
    new_country["total_visited"]: times_visited
    travel_log.append(new_country)

add_new_country("Russia",2,["Moscow","Saint Petersburg"])
print(travel_log)