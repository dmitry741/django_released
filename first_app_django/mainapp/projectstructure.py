class BaseProject:
    def __init__(self, caption, button_text, button_link):
        self.caption = caption
        self.button_text = button_text
        self.button_link = button_link


    def __str__(self):
        return self.caption


class Carusel(BaseProject):

    def __init__(self, caption, text, button_text, button_link, active, class_name, alt):
        super().__init__(caption, button_text, button_link)
        self.text = text
        self.active = active
        self.class_name = class_name
        self.alt = alt


class ProjectPage(BaseProject):

    def __init__(self, caption, grey_caption, text_list, button_text, button_link):
        super().__init__(caption, button_text, button_link)
        self.grey_caption = grey_caption
        self.text_list = text_list


class MyProjectStructure:

    def __init__(self):
        self.carusel = []
        self.indicators = []
        self.stack = []
