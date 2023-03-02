DOWEL_MASSES = {
  1: 4.8,
  2: 6.5,
  3: 8.2,
  4: 6.2,
  5: 7.3,
}

PIECE_MASSES = {
  "WhiteKing1": 51.9,
  "WhiteKnight2": 10.6,
  "BlackKnight3": 36.6,
  "BlackBishop4": 13.1,
  "BlackPawn5": 15.4,
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
    Solves for pivot point of dowel, assumes that there are two masses per dowel
    config: list of masses which represents dowel, example [M1, M2, LES, MD], 
    M1: Mass on left side of dowel
    M2: Mass on right side of dowel
    LES are the lengths of the masses to the end of the dowe;
    LE1: length from end for M1
    LE2: length from end for M2
    MD = dowel mass
    Last argument of config will be dowel's mass
    l: length of dowel
    returns distance from left end of dowel of pivot, sum of mass one, two, and the dowel as well as a tuple of LEs
    Example Config: [13.1,36.6, (1,2), 6.5]
    Mass one is 13.1 grams, Mass two is 3.3 grams
    Mass one is 1 cm from left end of dowel, Mass two is 2 cm from right end of dowel
    Mass of the dowel is 6.5 grams
    """
    dowel_mass = config[-1]
    les = config[-2]
    masses = config[:-2]
    print(les)
    le1 = les[0]
    le2 = les[1]
    pivot = (masses[1] * l + dowel_mass * l / 2 + masses[0] * le1 - masses[1] * le2) / (masses[0] + masses[1] + dowel_mass)
    return pivot, sum(masses) + dowel_mass, (le1, le2)

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
    pivot_res = [pivot1, pivot2, pivot_val, edge_len]
    if not pivot1:
        pivot_res = [pivot2, pivot_val, edge_len]
    if not pivot2:
        pivot_res = [pivot1, pivot_val, edge_len]
    if not pivot1 and not pivot2:
        pivot_res = [pivot_val, edge_len]
    return pivot_res, mass_sum


configuration = [[PIECE_MASSES["WhiteKing1"], [PIECE_MASSES["BlackKnight3"], PIECE_MASSES["WhiteBishop9"], [1,1], DOWEL_MASSES[3]], [1,1],DOWEL_MASSES[2]], [PIECE_MASSES["BlackQueen8"], [PIECE_MASSES["WhiteRook12"], PIECE_MASSES["BlackPawn5"], [1,1], DOWEL_MASSES[5]], [1,1], DOWEL_MASSES[4]], [1,1], DOWEL_MASSES[1]]

solution, _ = solve(configuration)
print(solution)