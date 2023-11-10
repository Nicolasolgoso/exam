# Función para calcular el promedio de temperatura por semana
def calculate_average(*weeks):
    averages = [] # Lista para almacenar los promedios de cada semana
    for week in weeks:
        average = sum(week) / len(week)
        averages.append(average)
    return averages

# Función para encontrar el día más caluroso de cada semana
def hottest_day(*weeks):
    hottest_days = []  # Lista para almacenar los días más calurosos de cada semana
    for week in weeks:
        day_of_hottest_temp = week.index(max(week)) + 1  # Encuentra el día más caluroso
        hottest_days.append(day_of_hottest_temp)  # Agrega el número del día a la lista
    return hottest_days
# Función para encontrar las semanas con temperaturas en un rango específico
def mild_weeks(lower, upper, *weeks):
    result = [] # Lista para almacenar las semanas en el rango especificado
    for i, week in enumerate(weeks, start=1):
        if all(lower <= temp <= upper for temp in week):
            result.append(i)
    return result


# Función para calcular los cambios de temperatura día a día
def change_temperature(*weeks):
    changes = []  # Lista para almacenar las diferencias de temperatura ordenadas por día
    for week in weeks:
        change = [week[j] - week[j - 1] for j in range(1, len(week))]  # Calcula las diferencias de temperatura
        changes.append(change)  
    return changes 

week1 = [22, 24, 19, 21, 25, 23, 20]
week2 = [20, 22, 21, 23, 24, 22, 21]
week3 = [23, 21, 20, 22, 24, 25, 23]

print("Media de temperatura por semana:", calculate_average(week1, week2, week3))
print("Día más caluroso por semana:", hottest_day(week1, week2, week3))
print("Semanas con temperaturas entre 20-25°C:", mild_weeks(20, 25, week1, week2, week3))
print("Cambios de temperatura día a día:", change_temperature(week1, week2, week3))