
from pyscript import document

# Dictionary containing information about nonmetal elements.
# The chemical symbols serve as the dictionary keys.
NONMETALS = {
    "H": ("HYDROGEN", "H", 1, 1.008),
    "He": ("HELIUM", "He", 2, 4.003),
    "C": ("CARBON", "C", 6, 12.011),
    "N": ("NITROGEN", "N", 7, 14.007),
    "O": ("OXYGEN", "O", 8, 15.999),
    "F": ("FLUORINE", "F", 9, 18.998),
    "Ne": ("NEON", "Ne", 10, 20.180),
    "P": ("PHOSPHORUS", "P", 15, 30.974),
    "S": ("SULFUR", "S", 16, 32.065),
    "Cl": ("CHLORINE", "Cl", 17, 35.453),
    "Ar": ("ARGON", "Ar", 18, 39.948),
    "Se": ("SELENIUM", "Se", 34, 78.971),
    "Br": ("BROMINE", "Br", 35, 78.904),
    "Kr": ("KRYPTON", "Kr", 36, 83.798),
    "I": ("IODINE", "I", 53, 126.904),
    "Xe": ("XENON", "Xe", 54, 131.293),
    "Rn": ("RADON", "Rn", 86, 222)
}

def search_nonmetal(e):

    # Get the chemical symbol entered by the user.
    symbol_input = document.getElementById("nonmetal1").value.strip().title()

    # Retrieve the element information using get().
    result = NONMETALS.get(
        symbol_input,
        ("Element not found", "-", "-", "-")
    )

    # Display the element information.
    document.getElementById("name").innerText = result[0]
    document.getElementById("symbol").innerText = result[1]
    document.getElementById("number").innerText = result[2]
    document.getElementById("mass").innerText = result[3]
