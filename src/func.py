from datetime import timedelta, datetime
def rocket_parts():
    print("payload, propellant, structure")


rocket_parts()


def rocket_parts():
    return "payload, propellant, structure"
print(rocket_parts())

print(any([True, True, False]))
print(any([False, False, False]))
#print(any()) # thorow error


def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"


# print(distance_from_earth()) # t e
print(distance_from_earth("aa"))
print(distance_from_earth("Moon"))


def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")


print(arrival_time())

# keyなし
def variable_length(*args):
    print(args)

variable_length(1,2,3,4)

# keyあり
def variable_length(**kwargs):
    print(kwargs)
    for name, val in kwargs.items():
        print(f"{name}: {val}")


variable_length(a=1, b=2, c=3)
