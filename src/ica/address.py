betsy_info = {
    'Name': 'Betsy Foobar',
    'Phone': 'x8012',
    'Street': '1600 Grand Avenue',
    'City': 'Saint Paul',
    'State': 'MN',
    'Email': 'bfoobar@macalester.edu'
}

tom_info = {
    'Name': 'Tom Riddle',
    'Phone': 'x8512',
    'Street': '1600 Grand Avenue',
    'City': 'Saint Paul',
    'State': 'MN',
    'Email': 'triddle@macalester.edu'
}
address_book = [
    betsy_info,
    tom_info,
    {
        'Name': 'Susan Fox',
        'Phone': 'x6553',
        'Street': '1600 Grand Avenue',
        'City': 'Saint Paul',
        'State': 'MN',
        'Email': 'fox@macalester.edu'
    }
]
address_book.append({
    'Name': 'Harry Potter',
    'Phone': 'x7777',
    'Street': '4 Privet Drive',
    'City': 'London',
    'State': 'UK',
    'Email': 'hpotter@hogwarts.edu'
})

address_book.append({
    'Name': 'Luna Lovegood',
    'Phone': 'x1234',
    'Street': 'Ottery St. Catchpole',
    'City': 'Devon',
    'State': 'UK',
    'Email': 'llovegood@hogwarts.edu'
})
print("Original address_book:")
for entry in address_book:
    print(entry)
print()
def filter_by_city(city, address_book):
    filtered = []
    for entry in address_book:
        if entry['City'] == city:
            filtered.append(entry)
    return filtered
print("People living in Saint Paul:")
filtered_list = filter_by_city('Saint Paul', address_book)
for person in filtered_list:
    print(person)
