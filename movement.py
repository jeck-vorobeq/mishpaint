import wrap

pla = wrap.sprite.add("pacman", 100, 600, "player2")


@wrap.on_key_always(wrap.K_w,wrap.K_s,wrap.K_a,wrap.K_d)
def management(keys):
    global pla
    if wrap.K_w in keys:
        wrap.sprite.set_angle(pla, 0)
        wrap.sprite.move(pla, 0, -5)
    if wrap.K_s in keys:
        wrap.sprite.set_angle(pla, 180)
        wrap.sprite.move(pla, 0, 5)
    if wrap.K_a in keys:
        wrap.sprite.set_angle(pla, -90)
        wrap.sprite.move(pla, -5, 0)
    if wrap.K_d in keys:
        wrap.sprite.set_angle(pla, 90)
        wrap.sprite.move(pla, 5, 0)
