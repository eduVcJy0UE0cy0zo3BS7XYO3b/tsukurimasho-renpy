define N = Character("Nastya")
define M = Character("Masha")

label prestory:
    scene university hallway

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    return enter_hallway

label enter_hallway:

    return kitchen

label kitchen:

    return books

label books:

    return try_to_leave_hallway

label try_to_leave_hallway:

    return mashas_bedroom

label mashas_bedroom:

    return kitchen_check

label kitchen_check:

    return hallway_check

label hallway_check:

    return bedroom_catch

label bedroom_catch:

    return phone_ring

label phone_ring:

    return
