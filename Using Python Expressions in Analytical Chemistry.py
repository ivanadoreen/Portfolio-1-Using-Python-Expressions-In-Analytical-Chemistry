print("""
# PORTFOLIO 1: USING PYTHON EXPRESSIONS IN ANALYTICAL CHEMISTRY
     Description: This script calculates basic analytical chemistry formulas.
     Concepts Used: Variables and Assignments (`=`)
     Constants (Numbers and Strings)
     Mathematical Operators (`*`, `/`)
""")


print("\n" + "="*50)
print("USING PYTHON EXPRESSIONS IN ANALYTICAL CHEMISTRY ")
print("="*50 + "\n")

# ---------------------------------------------------------
# MOLARITY CALCULATION (M = moles / volume)
# ---------------------------------------------------------
print("#MOLARITY CALCULATION")

# Assigning values to variables
moles = 2.34
volume = 2

# Using the division operator (/) to calculate molarity
molarity = moles / volume
print("Molarity:", molarity, "mol/L" or "M")

moles = 0.325
volume = 450
molarity = moles / volume
print("Molarity:", molarity, "mmol/mL" or "M")

# ---------------------------------------------------------
# DILUTION FORMULA (C1V1 = C2V2)
# ---------------------------------------------------------
print("\n# DILUTION FORMULA (C1V1 = C2V2)")

# Defining initial concentration and volumes
c1 = 2
v1 = 10
v2 = 50

# Using multiplication (*) and division (/) to solve for C2
c2 = (c1 * v1) / v2
print("Final concentration:", c2, "M")

c1 = 8.5
v1 = 3
v2 = 15
c2 = (c1 * v1) / v2
print("Final concentration:", c2, "M")

# ---------------------------------------------------------
# pH CALCULATOR (Approximation)
# ---------------------------------------------------------
print("\n# pH CALCULATOR")

h_concentration = 0.201
# Mathematical expression calculating pH
ph = -4 * h_concentration  
print("pH:", ph)

h_concentration = 0.5043
# Mathematical expression calculating pH
ph = 1 * h_concentration 
print("pH:", ph)

# ---------------------------------------------------------
# SOLUTION PREPARATION (Mass = Molarity * Volume * Molar Mass)
# ---------------------------------------------------------
print("\n# SOLUTION PREPARATION")

molarity = 8.5
volume = 2
molar_mass = 58.44

# Multiplying three variables together to find the required mass
mass = molarity * volume * molar_mass
print("Mass needed:", mass, "g")

molarity = 0.1
volume = 1.5
molar_mass = 194.1896
mass = molarity * volume * molar_mass
print("Mass needed:", mass, "g")

# ---------------------------------------------------------
# IDEAL GAS LAW CALCULATOR (PV = nRT)
# ---------------------------------------------------------
print("\n# IDEAL GAS LAW CALCULATOR")

# 1. Define the constants and variables
# R is the ideal gas constant (L*atm / mol*K)
gas_constant_R = 0.0821  

# Hardcoded experimental data
moles_n = 2.5
volume_v = 10.0  # in Liters
temp_celsius = 25.0  

# 2. Mathematical Expressions
# First, convert Celsius to Kelvin (K = C + 273.15)
temp_kelvin = temp_celsius + 273.15

# Calculate Pressure: P = (n * R * T) / V
pressure_atm = (moles_n * gas_constant_R * temp_kelvin) / volume_v

# 3. Output the results
print("--- Experimental Conditions ---")
print("Moles (n):", moles_n, "mol")
print("Volume (V):", volume_v, "L")
print("Temperature:", temp_celsius, "C (", temp_kelvin, "K )")
print("-------------------------------")
print("Calculated Pressure:", pressure_atm, "atm")
print("\n" + "="*50)