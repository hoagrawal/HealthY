def read_config(key):
    # Read property key from property file

    health_prop_file = open("healthY.properties", 'r')
    for line in health_prop_file:
        if key in line:
            keyval = line.rstrip().split("=")[1]
    return keyval