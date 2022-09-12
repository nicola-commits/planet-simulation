from body import Body
import thorpy

class ShortNumber(float):
    def __init__(self, value):
        super().__init__()

class Creator:
    def __init__(self):
        pass

    def show(self, screensize=(800, 600)):
        application = thorpy.Application((800, 600), "ThorPy Overview")

        addbtn = thorpy.Clickable("Add planet")
        thorpy.makeup.add_basic_help(addbtn, "Clickable:\nCan be hovered and pressed.")

        slider = thorpy.SliderX(80, (0, 1e64), "Mass: ", type_=float,
                                initial_value=6e24)

        title_element = thorpy.make_text("Overview example", 22, (255, 0, 0))

        elements = [addbtn, slider]
        central_box = thorpy.Box(elements=elements)
        central_box.fit_children(margins=(30, 30))  # we want big margins
        central_box.center()  # center on screen
        central_box.set_main_color((220, 220, 220, 180))  # set box color and opacity

        background = thorpy.Background(elements=[title_element, central_box])
        thorpy.store(background)

        menu = thorpy.Menu(background)
        menu.play()

        application.quit()

