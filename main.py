
# Import the tools for the html to function
from pyscript import document

# Sets of different grade levels of the Social Studies club
grade_7 = {"Saturnina", "Narcisa", "Paciano"}
grade_8 = {"Basilio", "Isagani", "Simoun"}
grade_9 = {"Segunda", "Leonor", "Josephine"}
grade_10 = {"Francisco", "Teodora", "Jose"}

# Union of the the four sets into one master set.
all_members = grade_7 | grade_8 | grade_9 | grade_10

# Display the current members and their total count.
def update_output():
    total_members = len(all_members)

    # Display the set aka the club members directly on the html using f-string.
    document.getElementById("output").innerHTML = f"""
        <h4>Current Club Members</h4>
        <p>{all_members}</p>
        <hr>
        <h4>Total Club Members: {total_members}</h4>
    """

# Add a new member when the button is clicked.
def result_checker(event):
    global all_members

    # Get the names entered by the user.
    first_name = document.getElementById("first_name").value.strip().title()
    last_name = document.getElementById("last_name").value.strip().title()

    # Combine the first and last names using an f-string.
    full_name = f"{first_name} {last_name}".strip()

    # When the name is finalized, create a set
    new_member = {full_name}

    # Using union operator to combine the new member set and the master set aka all numbers
    all_members = all_members | new_member

    # Refresh the member directory.
    update_output()

# Display the original members immediately when the page loads.
update_output()
