
from pyscript import document

# These are the existing members of the volleyball varsity team.
grade7_clubbies = {"SHELDON COOPER", "GEORGE COOPER", "BILLY SPARKS"}
grade8_clubbies = {"TIFFANY CO", "LOUIS VUITTON", "EMERALD HAZEL"}
grade9_clubbies = {"MADLINE MYERS", "THERESE MANALILI", "ANASTASIA UY"}
grade10_clubbies = {"CHEREE MENDOZA", "ANGELIE LIAMS", "BOBBIE BLUE"}

# Use union to combine all the grade-level sets into one set.
all_clubbies = grade7_clubbies | grade8_clubbies | grade9_clubbies | grade10_clubbies

def add_clubbie(e):

    # Get the first and last name entered by the user.
    first_name = document.getElementById("fname_input").value.strip()
    last_name = document.getElementById("lname_input").value.strip()

    # Combine the inputs and change the name to uppercase.
    new_clubbie = f"{first_name} {last_name}".strip().upper()

    # Add the new name to the set.
    if new_clubbie:
        all_clubbies.add(new_clubbie)

    # Arrange the names alphabetically.
    clubbies_list = "\n".join(sorted(all_clubbies))
    total_clubbies = len(all_clubbies)

    # Display the updated member list and total number.
    varsity_output = (
        f"ALL MEMBERS:\n{clubbies_list}"
        f"\n\nTOTAL MEMBERS: {total_clubbies}"
    )

    document.getElementById("output_box").innerText = varsity_output
