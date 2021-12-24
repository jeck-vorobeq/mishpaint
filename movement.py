import wrap,main

@wrap.on_key_down()
def management():

    if wrap.K_w:
        wrap.sprite.set_angle(main.pla, 45)
        wrap.sprite.move(main.pla, 5, -5)
    if wrap.K_s :
        wrap.sprite.set_angle(main.pla, 135)
        wrap.sprite.move(main.pla, 5, 5)
    if wrap.K_a:
        wrap.sprite.set_angle(main.pla, 90)
        wrap.sprite.move(main.pla, 5, 0)

