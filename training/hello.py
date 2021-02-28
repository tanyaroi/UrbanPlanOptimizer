lbs_to_kg = 0.453592
kg_to_lbs = 1 / lbs_to_kg
selected_ratio = -1

weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ").upper()

unit_upper = unit.upper()

if unit_upper == "K":
    selected_ratio = kg_to_lbs

elif unit_upper == "L":
    selected_ratio = lbs_to_kg

if selected_ratio != -1:
    print(f"Your weight is {weight*selected_ratio}")
else:
    print("Wrong Choice!")



