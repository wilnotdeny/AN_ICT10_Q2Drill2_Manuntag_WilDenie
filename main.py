from pyscript import document, when

# sets (one for each grade)
grade7 = {"Anne E. Nit", "So Phat"}
grade8 = {"Capa Lee", "Brent Faiyaz"}
grade9 = {"Eva N. Ko", "Art E. Mo"}
grade10 = {"Eman D. Lu", "Tom Ad"}

# the new members
new_members = set()


# Shows the member list and the total
def show_members():
    # combine all the sets using the | operator
    master = grade7 | grade8 | grade9 | grade10 | new_members

    document.getElementById("output").innerHTML = f"""
        <h4>All Members</h4>
        <p>{", ".join(master)}</p>
        <h4>Total Members: {len(master)}</h4>
    """


# Runs when the button is clicked
@when("click", "#add-btn")
def add_member(event):
    # get the names from the text boxes
    first = document.getElementById("first").value
    last = document.getElementById("last").value

    # add the new member to the set
    new_members.add(f"{first} {last}")

    # update the list
    show_members()


# show the starting list when the page loads
show_members()