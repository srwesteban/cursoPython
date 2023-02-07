
year = int(input("Ingrese en año:\n"))

def bisisesto(year):
    if year%4==0 and year%100 !=0:
        return f" el año {year} es bisiesto"
    elif year%100==0 and year%400==0:
                return f"el año {year} es bisiesto"
    else:
        return f"el año ", {year}, "no es bisiesto"

print(bisisesto(year))