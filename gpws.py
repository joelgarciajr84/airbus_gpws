mimium_before_retard = 10 # feet
altitude = 1150 # feet
callouts_altitudes = [1000, 500, 300, 100, 50, 40, 30, 20, 10]
descent_rate = 1 # feet per minute

# Ajustando a altitude inicial para entrar no loop corretamente
altitude -= descent_rate

while altitude > 0:
    # print(altitude, descent_rate)
    if altitude < mimium_before_retard:
        print("RETARD, RETARD, RETARD")
        break
    elif altitude in callouts_altitudes:
        print(f"Callout: {altitude} feet")
    altitude -= descent_rate
