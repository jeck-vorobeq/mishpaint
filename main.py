import wrap,time


wrap.add_sprite_dir("img")
wrap.world.create_world(800, 700)
wrap.world.set_back_color(100, 200, 200)
wrap.world.set_title("MAZE")
pla = wrap.sprite.add("pacman", 100, 600, "player2")
wrap.sprite.add("img", 100, 600,"img")
import movement
