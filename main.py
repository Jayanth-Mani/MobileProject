dowel_masses = {
  1: 4.8,
  2: 6.5,
  3: 8.2,
  4: 6.2,
  5: 7.3,
}

piece_mass = {
  "WhiteKing1": 51.9,
  "WhiteKnight2": 10.6,
  "BlackKnight3": 36.6,
  "BlackBishop4": 13.1,
  "BlacPawn5": 15.4,
  "BlackRook6": 36.6,
  "WhitePawn7": 15.0,
  "BlackQueen8": 46.7,
  "WhiteBishop9": 26.9,
  "WhiteQueen10": 47.3,
  "BlackKing11": 51.0,
  "WhiteRook12": 35.9

}
DOWEL_LENGTH = 30
def torque_solve(config, l):
    """
    Solves for pivot point of dowel, assumption that masses are at end of DOWEL
    config: list of masses which represents dowel, example [M1, M2, MD], DW = dowel mass
    Last argument of config will be dowel's mass
    l: length of dowel
    returns distance from left end of dowel of pivot
    """
    masses = [None] * (len(config) - 1)
    dowel_mass = config[-1]
    masses_without_dowel = config[:-1]
    for i, values in enumerate(masses_without_dowel):
        if isinstance(values, list): 
            # print(values)
            mass_sum = nested_sum(values)
        else: 
            mass_sum = values
        masses[i] = mass_sum
     # works for two masses per level
    # print(masses)
    pivot = (2 * masses[1] * l + dowel_mass * l) / (2 * (masses[0] + masses[1] + dowel_mass))
    return pivot

def nested_sum(L):
    total = 0  # don't use `sum` as a variable name
    for i in L:
        if isinstance(i, list):  # checks if `i` is a list
            total += nested_sum(i)
        else:
            total += i
    return total

#print(torque_solve([[13.1,36.6,6.5], 51.9, 4.8], DOWEL_LENGTH))
solution = []
def solve(config):
    for i, val in enumerate(config):
        if isinstance(val, list):
            solve(val)
    solution.append(torque_solve(config, DOWEL_LENGTH))

solve([[13.1,[36.6,36.6,4.4],6.5], 51.9, 4.8])
print(solution)