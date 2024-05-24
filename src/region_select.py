def select_region_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        regions = []
        for line in lines:
            coordinates = line.strip().split(',')
            if len(coordinates) == 4:
                regions.append(tuple(map(int, coordinates)))
    return regions
