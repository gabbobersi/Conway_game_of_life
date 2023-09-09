from UI_elements.button import Button

class UIManager:
    """
    This class is a Singleton, and manages all the UI elements.
    Its core function is to place all the UI elements on the screen, dynamically based on screen resolution.
    It's an alternative to manually sets coordinates for each UI element.

    Elements are placed vertically (with middle screen alignment) in the order they are added.
    Every element is referenced by its text (label), so it's easy to get it back.
    """
    def __init__(self, options):
        self.options = options
        self.ui_elements = []

    def add_button(self, title, width, height, background_color):
        x = (self.options.window_width - width) // 2
        y = 0   # Will be calculate in draw method
        button = Button(self.options.screen.get_screen(), title, True, x, y, width, height, background_color)
        self.ui_elements.append(button)

    def draw(self):
        offsett_from_top_screen = self.options.window_height // 10
        size_per_element = (self.options.window_height) // 6
        for i, element in enumerate(self.ui_elements):
            new_y = size_per_element * i
            element.update(new_y=new_y + offsett_from_top_screen)
            element.draw()

    def get_element(self, text):
        for element in self.ui_elements:
            if element.text == text:
                return element
        return None

    def clear_elements(self):
        self.ui_elements.clear()

    # Singleton
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(UIManager, cls).__new__(cls)
            cls._instance.value = None
        return cls._instance