
from pyscript import document

# Dictionary containing the names of the volleyball varsity members.
members = {
    "Cheree Mendoza": "Congratulations! You are now part of the School's Volleyball Varsity, Cheree Mendoza.",
    "Princess Schwab": "Congratulations! You are now part of the School's Volleyball Varsity, Princess Schwab.",
    "Zoey Ledres": "Congratulations! You are now part of the School's Volleyball Varsity, Zoey Ledres.",
    "Therese Reyes": "Congratulations! You are now part of the School's Volleyball Varsity, Therese Reyes.",
    "Elise Ramos": "Congratulations! You are now part of the School's Volleyball Varsity, Elise Ramos."
}

def add_names(e):

    # Get the user's first and last name.
    name1 = document.getElementById("input1").value.strip().title()
    name2 = document.getElementById("input2").value.strip().title()

    # Combine both inputs into a full name.
    fullname = name1 + " " + name2

    # Retrieve the message using the dictionary's get() method.
    message = members.get(
        fullname,
        "Sorry! Your name is NOT on the list, " + fullname + "."
    )

    # Display the result.
    document.getElementById("output1").innerText = message
