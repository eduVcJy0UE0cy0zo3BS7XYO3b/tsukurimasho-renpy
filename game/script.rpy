define N = Character("Настя", who_color="#6d3345")
define M = Character("Маша", who_color="#1e2231")

define audio.door_close = "sfx100v2_door_03.ogg"
define audio.door_open = "sfx100v2_door_05.ogg"

define audio.shelve_close = "wood_close_01.ogg"
define audio.shelve_open = "wood_squeak_01.ogg"

define audio.door_knocking_light = "triKnock04.ogg"
define audio.door_knocking_heavy = "triKnock01.ogg"
define audio.take_key = "keys_07.ogg"
define audio.key_open_door = "lock_open_01.ogg"
define audio.wear_off1 = "Cloth_01.ogg"
define audio.wear_off2 = "Cloth_02.ogg"

define audio.keyring = "keys_06.ogg"
define audio.meow = "Meow.ogg"
define audio.cats_footstep = "sfx100v2_footstep_wood_01.ogg"

define audio.university_clock_alarm = "doorbell-old-tring.ogg"
define audio.mashas_clock_ticking = "clock.ogg"

define audio.crowd = "crowd_-_school_excursion.mp3"
define audio.masha_theme = "masha_theme.ogg"
define audio.nasya_theme = "nasya_theme.ogg"

define audio.pour = "pour_tea.wav"
define audio.squish = "squish.wav"
define audio.happy_end = "Curious Critters (Extended Version) 1.mp3"

define audio.complete_mission = "gmae.ogg"
define audio.happy_end = "Curious Critters (Extended Version) 1.mp3"
define audio.mobile_phone = "chirptone.ogg"

define audio.footstep1 = "hard-footstep1.wav"
define audio.footstep2 = "hard-footstep2.wav"
define audio.footstep3 = "hard-footstep3.wav"
define audio.footstep4 = "hard-footstep4.wav"

define audio.bedroom_closet_open = "door_01.ogg"
define audio.bedroom_closet_close = "door_02.ogg"

define audio.searching = "2 Part Invention in B Minor.mp3"
define audio.puzzling = "Desolate Part II.mp3"
define audio.calm = "Curious Critters (Extended Version) 1.mp3"


label start:
    jump prestory

    
label prestory:
    scene cg university clock
    with dissolve
    pause
    play sound university_clock_alarm volume 0.1
    pause
    play music crowd volume 0.2
    scene bg hallway
    with dissolve
    pause
    show nastya normal at left:
        yalign -0.1
    with dissolve
    pause
    show masha normal at right:
        yalign 0.1
    with dissolve
    M ""
    show masha embrace
    M ""
    show nastya hmm
    N ""
    M ""
    N ""
    play sound keyring
    M ""
    show masha happy
    pause
    hide masha
    with dissolve
    pause
    show nastya sad
    with dissolve
    pause
    jump the_hall

    
label the_hall:
    play music mashas_clock_ticking
    scene cg clock
    with dissolve
    pause
    play sound door_knocking_light
    $ renpy.pause(5.0)
    pause
    scene bg hall
    with dissolve
    pause
    play sound door_knocking_heavy
    $ renpy.pause(5.0)
    pause
    play sound key_open_door
    pause
    play sound [door_open, door_close, footstep1, footstep2, footstep3, footstep4]
    $ renpy.pause(3.0)
    show nastya normal weared at center:
        yalign -0.1
    with dissolve
    pause
    N ""
    hide nastya with dissolve
    play sound [wear_off1, wear_off2]
    $ renpy.pause(3.0)
    jump books_pass

    
label books_pass:
    scene cg bookshelf
    with wipeleft
    jump kitchen

    
label kitchen:
    play music calm volume 0.2
    scene bg kitchen
    with wipeleft
    show nastya normal at center:
        yalign -0.1
    with dissolve
    N ""
    play sound pour_tea volume 2.0
    N ""
    play sound squish volume 2.0
    pause
    jump books

    
label books:
    scene cg bookshelf
    with wiperight
    show nastya normal at center:
        yalign -0.1
    with dissolve
    N ""
    jump try_to_leave_hallway

    
label try_to_leave_hallway:
    scene bg hall
    with wiperight
    
    show nastya normal at center:
        yalign -0.1
    with dissolve

    N ""
    play music puzzling
    N ""
    scene cg shelves closed
    N ""
    play sound shelve_open
    scene cg shelves right with dissolve
    play sound [meow, keyring]
    $ renpy.pause(1.0)
    N ""
    jump bedroom

label bedroom:
    scene bg bedroom
    with CropMove(0.5)

    play music searching volume 0.2

    show nastya normal at center:
        yalign -0.1
    # with dissolve

    N ""
    N ""
    play sound [bedroom_closet_open, keyring, meow]
    N ""
    play sound bedroom_closet_close
    N ""
    jump kitchen_check

    
label kitchen_check:
    scene bg kitchen
    with CropMove(0.5, mode='slideleft')
    show nastya normal at center:
        yalign -0.1
    N ""
    jump hallway_check

    
label hallway_check:
    scene cg shelves right with dissolve
    show nastya normal at center:
        yalign -0.1
    N ""
    play sound shelve_open
    scene cg shelves both with dissolve
    play sound [meow, keyring]
    $ renpy.pause(1.0)
    N ""
    jump bedroom_catch

    
label bedroom_catch:
    scene bg bedroom
    with CropMove(0.5)

    show nastya normal at center:
        yalign -0.1
        
    N ""
    play sound bedroom_closet_open
    scene cg bedroom ending with dissolve
    $ renpy.pause(2.0)
    play music happy_end volume 0.2
    N ""
    jump phone_ring

    
label phone_ring:
    play sound mobile_phone
    N ""
    M ""
    N ""
    M ""
    jump creditss

label creditss:
    scene black
    play music searching volume 0.2
    show text "{color=#fff}Над новеллой работали:{/color}" with dissolve
    $ renpy.pause(2.0)
    show text "{color=#fff}Сюжет и код\n\nliltechude{/color}"
    $ renpy.pause(4.0)
    show text "{color=#fff}Спрайты Маши\n\nNika{/color}"
    $ renpy.pause(4.0)
    show text "{color=#fff}Спрайты Насти\n\nElena{/color}"
    $ renpy.pause(4.0)
    show text "{color=#fff}Звуки\n\nСообщество OpenGameArt{/color}"
    $ renpy.pause(4.0)
    show text "{color=#fff}Музыка\n\nMatthew Pablo{/color}"
    $ renpy.pause(4.0)
    show text "{color=#fff}Спасибо за прохождение!{/color}"
    $ renpy.pause(10.0)
