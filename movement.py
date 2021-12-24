import wrap,main

@wrap.on_key_down()
def management(keys):

    if wrap.K_w in keys:
        wrap.sprite.set_angle(main.pla, 0)
        wrap.sprite.move(main.pla, 0, -5)
    if wrap.K_s in keys:
        wrap.sprite.set_angle(main.pla, 180)
        wrap.sprite.move(main.pla, 0, 5)
    if wrap.K_a in keys:
        wrap.sprite.set_angle(main.pla, -90)
        wrap.sprite.move(main.pla, -5, 0)
    if wrap.K_d in keys:
        wrap.sprite.set_angle(main.pla, 90)
        wrap.sprite.move(main.pla, 5, 0)
