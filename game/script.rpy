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

define audio.pour = "pour_tea.wav"
define audio.squish = "squish.wav"

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
    M "Насть~"
    show masha embrace
    M "Настя."
    show nastya hmm
    N "Оо.. привет"
    M "У меня к тебе есть одна небольшая просьба.."
    N "Слушаю."
    M "Завтра я уезжаю на один день на дачу.."
    M "..."
    M "И..."
    N "И что?"
    M "Не могла бы ли ты прийти покормить кошку?"
    N "Мм.. хорошо."
    play sound keyring
    show masha happy
    M "Вот ключи, как пройти надеюсь помнишь.  Если что, пиши-звони, я на связи."
    N "..."
    M "Спасибо большое!  Я у тебя в долгу~"
    hide masha
    with dissolve
    show nastya sad
    with dissolve
    "Сегодня Настя пришла на пары после ночного дежурства на промышленном контуре.  Поняла на что подписалась только спускаясь к выходу и прокручивая предметы в кармане, где среди прочих был тяжелый, необычной формы ключ."
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
    N "Да, тут ничего не поменялось за пол года."
    N "..."
    N "Вроде никого нет."
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
    N "Чайник горячий ещё.  Это вроде специальный какой-то, для чайной церемонии.  Провести без Маши я конечно не смогу, но залить кипятком гринфилд точно под силам."
    play sound pour_tea volume 2.0
    N ""
    play sound squish volume 2.0
    N "Горечевато что-то."
    N "Второй день пришибленной хожу.  Или уже не первый?"
    N "Как же хочу это всё закончить.  Не знаю сколько это можно всё совмещать.  Работа, лабы, семинары..."
    "Вздох Насти приподнял салфетку с кружкой из-под чая."
    N "От такого точно не остынет."
    N "Может книжки посмотреть какие на стеллаже есть.."
    jump books


label books:
    scene cg bookshelf
    with wiperight
    show nastya normal at center:
        yalign -0.1
    with dissolve
    N ".."
    N "..."
    N "...."
    N "Из нового -- выпуски местных газет за 93ий год.  Не получается спросить зачем она так изучает всё.  Обучение на ИстФаке должно включать интерес к предмету..  Но что бы так.."
    jump try_to_leave_hallway


label try_to_leave_hallway:
    scene bg hall
    with wiperight

    show nastya normal at center:
        yalign -0.1
    with dissolve

    N "Да, чай получился хорошим, но кровать дома тонизирует лучше."
    N ".."
    "Настя уже собиралась надевать пиджак, но в один момент резко замерла."
    play music puzzling
    N "А ключи... куда подевались?"
    N "......"
    N "......."
    N "Не помню что бы клала их в полку, но..."
    scene cg shelves closed
    N "Нет, я бы точно помнила, подходи я к этим полкам."
    hide nastya
    play sound shelve_open
    scene cg shelves right with dissolve
    play sound [meow, keyring]
    $ renpy.pause(1.0)
    N "Что за.."
    N " ...Он точно заскочил в спальню."
    jump bedroom

label bedroom:
    scene bg bedroom
    with CropMove(0.5)

    play music searching volume 0.2

    show nastya normal at center:
        yalign -0.1
    # with dissolve

    N "Под кроватью нет."
    N "За дверью нет."
    N "На подоконике нет."
    N "Остался шкаф."
    play sound [bedroom_closet_open, keyring, meow]
    N "Опять?  Откуда он убегает вообще!?"
    play sound bedroom_closet_close
    N "Ну, погоди!"
    jump kitchen_check


label kitchen_check:
    scene bg kitchen
    with CropMove(0.5, mode='slideleft')
    show nastya normal at center:
        yalign -0.1
    N ".."
    jump hallway_check


label hallway_check:
    scene cg shelves right with dissolve
    # show nastya normal at center:
    #     yalign -0.1
    N "А с левой что?"
    play sound shelve_open
    scene cg shelves both with dissolve
    play sound [meow, keyring]
    $ renpy.pause(1.0)
    N "Теперь точно не уйдёшь!!"
    jump bedroom_catch


label bedroom_catch:
    scene bg bedroom
    with CropMove(0.5)

    show nastya normal at center:
        yalign -0.1

    N "Вся комната осмотрена, а дверь из спальни закрыта.  Теперь ему не сбежать."
    play sound [bedroom_closet_open, complete_mission]
    scene cg bedroom ending with dissolve
    $ renpy.pause(2.0)
    play music happy_end volume 0.2
    N "Вот ты где, засранец."
    jump phone_ring


label phone_ring:
    play sound mobile_phone
    N "Да."
    M "Доброе утро!"
    N "Что такое."
    M "Я ведь поздаровалась..."
    N "Коту еды положила, это всё?"
    M "Храни тебя господь от всех бед... ..Ты ещё в доме?"
    N "А.. Да, за кошаком твоим гонялась, ключи стянул, гадюка такая."
    M "Ахаха~ Да, он иногда любит играться."
    N "Так зачем звонишь?  Давай сразу."
    M "Амм... ..можешь зайти в спальню?"
    N "Здесь, куда дальше?"
    M "На столе должна лежать тетрадочка.  Она там одна по идее лежит."
    N "Вижу, что с ней?"
    M "Хорошо~  Сейчас подъедет курьер на машине.  Передай ему тетрадку и скажи ему адрес куда тебя подвезти."
    N "И всё?"
    M "Да.  Ещё раз спасибо за помощь.  Как приеду, заварю тебе тот малиновый чай."
    N "Хорошо.  Увидимся."
    N "Пока-пока~"
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
