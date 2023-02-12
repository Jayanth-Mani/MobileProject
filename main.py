import random
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
    config: list of masses which represents dowel, example [M1, M2, MD], 
    M1: Mass on left side of dowel
    M2: Mass on right side of dowel
    DW = dowel mass
    OPTIONAL ARGUMENTS:
    L1: length from end for M1
    L2: length from end for M2
    Last argument of config will be dowel's mass
    l: length of dowel
    returns distance from left end of dowel of pivot
    """
    dowel_mass = config[-1]
    masses = config[:-1]
    # works for two masses per level
    # le1 = random.randint(1,4)
    # le2 = random.randint(1,4)
    le1 = 0
    le2 = 0
    pivot = ( masses[1] * l + dowel_mass * l / 2 + masses[0] * le1 + masses[1] * le2) / (masses[0] + masses[1] + dowel_mass)
    return pivot, sum(masses) + dowel_mass, (le1, le2)


#print(torque_solve([[13.1,36.6,6.5], 51.9, 4.8], DOWEL_LENGTH))
solution = ""
def solve(config):
    mod_config = config.copy()
    m1 = config[0]
    m2 = config[1]
    pivot1 = []
    pivot2 = []
    if isinstance(config[0], list):
        pivot1, m1 = solve(config[0])
    if isinstance(config[1], list):
        pivot2, m2 = solve(config[1])
    mod_config[0] = m1
    mod_config[1] = m2
    pivot_val, mass_sum, edge_len = torque_solve(mod_config, DOWEL_LENGTH)
    if not pivot1:
        pivot_res = [pivot2, pivot_val, edge_len]
    if not pivot2:
        pivot_res = [pivot1, pivot_val, edge_len]
    if not pivot1 and not pivot2:
        pivot_res = [pivot_val, edge_len]
    return pivot_res, mass_sum

solution, _ = solve([[13.1,[36.6,36.6,4.4],6.5], 51.9, 4.8])
print(solution)