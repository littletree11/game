image black = "#000"
image white = "#fff"
image green = "#6ee2b4"
image gray = "#777676"


# part02 密室寻找物品 
screen find:
    if not flag_ticket:
        imagebutton auto "images/ticket_%s.png" action Jump('ticket') xalign 0.7 yalign 0.7
    if not flag_bear:
        imagebutton auto "images/bear_%s.png" action Jump('bear') xalign 0.4 yalign 0.8
    if not flag_ball:
        imagebutton auto "images/ball_%s.png" action Jump('ball') xalign 0.7 yalign 0.2


label ticket:
    小东 "这不是去年和小鹿一起去看电影的电影票吗？怎么会在这里？"
    $ flag_ticket = True
    jump find

label bear:
    小东 "这个小熊好可爱，要不就带走吧？"
    $ flag_bear = True
    jump find

label ball:
    小东 "这不是去年砸中我脑袋的棒球吗？怎么会在这里？"
    $ flag_ball = True
    jump find