import wrap, time

wrap.add_sprite_dir("img")
wrap.world.create_world(900, 700)
wrap.world.set_back_color(100, 200, 200)
wrap.world.set_title("MAZE")
pla = wrap.sprite.add("pacman", -12, 0, "player2")
wrap.sprite.add("img", 400, 350, "img")
import movement
