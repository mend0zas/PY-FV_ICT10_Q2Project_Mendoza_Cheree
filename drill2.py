
from pyscript import document

# These are the existing members of the volleyball varsity team.
grade7_clubbies = {"SHELDON COOPER", "GEORGE COOPER", "BILLY SPARKS"}
grade8_clubbies = {"TIFFANY CO", "LOUIS VUITTON", "EMERALD HAZEL"}
grade9_clubbies = {"MADLINE MYERS", "THERESE MANALILI", "ANASTASIA UY"}
grade10_clubbies = {"CHEREE MENDOZA", "ANGELIE LIAMS", "BOBBIE BLUE"}

# Use union to combine all the grade-level sets.
all_clubbies = grade7_clubbies | grade8_clubbies | grade9_clubbies | grade10_clubbies

def show_members():

    # Arrange the names alphabetically.
    clubbies_list = "\n".join(sorted(all_clubbies))

    # Count all the members.
    total_clubbies = len(all_clubbies)

    # Display the complete list.
    varsity_output = (
        f"ALL MEMBERS:\n{clubbies_list}"
        f"\n\nTOTAL MEMBERS: {total_clubbies}"
    )

    document.getElementById("output_box").innerText = varsity_output


def add_clubbie(e):

    # Get the first and last name entered by the user.
    first_name = document.getElementById("fname_input").value.strip()
    last_name = document.getElementById("lname_input").value.strip()

    # Combine the two inputs and convert them to uppercase.
    new_clubbie = f"{first_name} {last_name}".strip().upper()

    # Add the new member to the existing set.
    if new_clubbie:
        all_clubbies.add(new_clubbie)

    # Update the displayed member list.
    show_members()


# Display the original members when the page opens.
show_members()
