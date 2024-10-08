#! python3

# trafficLightSimulator

market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'

    #add this line to know that the bug happened, this checks the sanity of the program - sanity check
    # assert 'red' in stoplight.values(), 'Neither is red!' + str(stoplight)

switchLights(market_2nd)