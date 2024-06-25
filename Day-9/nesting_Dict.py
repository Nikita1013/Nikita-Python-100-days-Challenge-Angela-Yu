# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}


# Nesting List in dictionary
# Nesting Dictionary in dictionary
travel_log = {
    "France": {"cities_visited": ["Paris","Lille","Dijon"], "total_visited": 12},
    "Germany":{"cities_visited": ["Berlin","Hamburg","Munich"], "total_visited": 5},
}


# Nestinf Dictionary in a List

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

print(travel_log)