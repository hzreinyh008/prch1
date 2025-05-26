
molecules = ["H2O", "BCl3", "BeCl2", "SF6", "CCl4", "IF7", "SF4", "ClF3", "NF3", "CO2", "CH4"]
hm = {
    "H2O": "sp3", "BCl3": "sp2",
    "BeCl2": "sp", "SF6": "sp3d2", "CCl4": "sp3",
    "IF7": "sp3d3", "SF4": "sp3d", "ClF3": "sp3",
    "NF3": "sp3", "CO2": "sp", "CH4": "sp3"
}
gm = {
    "H2O": "угловая", "BCl3": "плоский треугольник",
    "BeCl2": "линейная", "SF6": "октаэдр", "CCl4": "тетраэдр",
    "IF7": "пентагональная бипирамида", "SF4": "тригональная бипирамида", "ClF3": "тригональная пирамида",
    "NF3": "тригональная пирамида", "CO2": "линейная", "CH4": "тетраэдр"
}
nep = {
    "H2O": "2", "BCl3": "0",
    "BeCl2": "0", "SF6": "0", "CCl4": "0",
    "IF7": "0", "SF4": "1", "ClF3": "1",
    "NF3": "1", "CO2": "0", "CH4": "0"
}

def remove_molecule(index):

    if 0 <= index < len(molecules):
        molecules.pop(index)


def get_molecules():
    return molecules


def get_hybridization_molecule(molecule_name):

    try:
        return hm[molecule_name]

    except KeyError:

        return False

def get_geometry_molecule(molecule_name):
    try:
        return gm[molecule_name]

    except KeyError:

        return False

def get_nep_molecule(molecule_name):
    try:
        return nep[molecule_name]

    except KeyError:

        return False