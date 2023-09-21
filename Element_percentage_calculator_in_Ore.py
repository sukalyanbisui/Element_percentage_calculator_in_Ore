
# AUTHOR: Sukalyan Bisui
# DATE CREATED: 16 July 2023

import re
# Dictionary with the elements and their atomic masses
atomic_mass = {
    'H':1.00797, 'He':4.0026, 'Li':6.941, 'Be':9.01218, 'B':10.81,
    'C':12.011, 'N':14.0067, 'O':15.9994, 'F':18.998403, 'Ne':20.179, 'Na':22.98977,
    'Mg':24.305, 'Al':26.98154, 'Si':28.0855, 'P':30.97376, 'S':32.06, 'Cl':35.453,
    'K':39.0983, 'Ar':39.948, 'Ca':40.08, 'Sc':44.9559, 'Ti':47.9, 'V':50.9415,
    'Cr':51.996, 'Mn':54.938, 'Fe':55.847, 'Ni':58.7, 'Co':58.9332, 'Cu':63.546,
    'Zn':65.38, 'Ga':69.72, 'Ge':72.59, 'As':74.9216, 'Se':78.96,
    'Br':79.904, 'Kr':83.8, 'Rb':85.4678, 'Sr':87.62, 'Y':88.9059,
    'Zr':91.22, 'Nb':92.9064, 'Mo':95.94, 'Tc':98, 'Ru':101.07,
    'Rh':102.9055, 'Pd':106.4, 'Ag':107.868, 'Cd':112.41, 'In':114.82,
    'Sn':118.69, 'Sb':121.75, 'I':126.9045, 'Te':127.6, 'Xe':131.3,
    'Cs':132.9054, 'Ba':137.33, 'La':138.9055, 'Ce':140.12, 'Pr':140.9077,
    'Nd':144.24, 'Pm':145, 'Sm':150.4, 'Eu':151.96, 'Gd':157.25, 'Tb':158.9254,
    'Dy':162.5, 'Ho':164.9304, 'Er':167.26, 'Tm':168.9342, 'Yb':173.04,
    'Lu':174.967, 'Hf':178.49, 'Ta':180.9479, 'W':183.85, 'Re':186.207,
    'Os':190.2, 'Ir':192.22, 'Pt':195.09, 'Au':196.9665, 'Hg':200.59,
    'Tl':204.37, 'Pb':207.2, 'Bi':208.9804, 'Po':209, 'At':210,
    'Rn':222, 'Fr':223, 'Ra':226.0254, 'Ac':227.0278, 'Pa':231.0359,
    'Th':232.0381, 'Np':237.0482, 'U':238.029, 'Pu':242, 'Am':243,
    'Bk':247, 'Cm':247, 'No':250, 'Cf':251, 'Es':252, 'Hs':255,
    'Mt':256, 'Fm':257, 'Md':258, 'Lr':260, 'Rf':261, 'Bh':262,
    'Db':262, 'Sg':263, 'Uun':269, 'Uuu':272, 'Uub':277
}

# Function to calculate the percentage of metal in ore from its chemical formula
def calculate_percentage_from_formula(formula, metal_symbol):
    try:
        metal_mass = atomic_mass[metal_symbol]

        # Parse the chemical formula into elements and their counts
        elements = re.findall(r'([A-Z][a-z]*)(\d*)', formula)

        total_mass = 0
        metal_count = 0

        for element, count in elements:
            count = int(count) if count else 1
            element_mass = atomic_mass[element]
            total_mass += count * element_mass
            if element == metal_symbol:
                metal_count += count

        if total_mass == 0:
            raise ValueError("Invalid chemical formula.")

        percentage = (metal_count * metal_mass / total_mass) * 100
        return percentage
    except KeyError:
        return f"Element {metal_symbol} not found in atomic mass dictionary."
    except ValueError as e:
        return str(e)

# Input chemical formula and metal symbol from the user
chemical_formula = input("Enter the chemical formula of the ore compound: ")
metal_symbol = input("Enter the symbol of the element: ")

# Calculate the percentage of metal in ore
result = calculate_percentage_from_formula(chemical_formula, metal_symbol)

if isinstance(result, float):
    print(f"The percentage of {metal_symbol} in the ore is: {result:.2f}%")
else:
    print("Error:", result)