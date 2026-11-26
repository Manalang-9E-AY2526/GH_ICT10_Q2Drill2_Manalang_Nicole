# 2nd quarter drill 2 - student club directory
from pyscript import document


def add_member(e):

    # predefined theater club members
    club_members1 = {'Nicole Manalang', 'Alyanna Barlisan', 'Mae Kutosha'}
    club_members2 = {'Shiloh Briones', 'Sheirhalyn Gaddi', 'Ada dy'}
    club_members3 = {'Mel Avisala', 'Josua Ortiz', 'Alice Guo'}
    club_members4 = {'Mocha Manalang', 'Kemmy Ruth', 'Marygrace Piattos'}

    # get the entered first and last names
    first_name = document.getElementById('first_name').value.strip()
    last_name = document.getElementById('last_name').value.strip()

    # combine the names into one new member
    new_member = (first_name + " " + last_name).strip()
    new_member_set = {new_member}

    # combine all club members and the new member
    all_members = club_members1 | club_members2 | club_members3 | club_members4 | new_member_set

    # count the total number of unique members
    total_members = len(all_members)

    # arrange the names alphabetically
    members_list = "<br>".join(sorted(all_members))

    # display the member directory and total count
    document.getElementById('output').innerHTML = f'''
        <h3>Registered Members</h3>
        <p>{members_list}</p>
        <hr>
        <p>Total Members: {total_members}</p>
    '''
