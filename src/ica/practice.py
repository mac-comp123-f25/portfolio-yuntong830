income = {}
years = {
    "Susan": 1968,
    "Alice": 1995,
    "Bob": 1988
}
years2 = years.copy()
print("Susan's birth year:", years["Susan"])
years["Henry"] = 2004
del years2["Susan"]
print("years dictionary:", years)
print("years2 dictionary:", years2)