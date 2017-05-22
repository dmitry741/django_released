class Carusel():

    def __init__(self, caption, text, button_text, button_link, active, class_name, alt, short_link):
        self.caption = caption
        self.button_text = button_text
        self.button_link = button_link

        self.text = text
        self.active = active
        self.class_name = class_name
        self.alt = alt
        self.short_link = short_link

    def __str__(self):
        return self.caption


class ProjectPage():

    def __init__(self, caption, grey_caption, text_list, button_text, button_link):
        self.caption = caption
        self.button_text = button_text
        self.button_link = button_link

        self.grey_caption = grey_caption
        self.text_list = text_list

    def __str__(self):
        return self.caption


class MyProjectStructure:

    def __init__(self):
        self.carusel = []
        self.indicators = []
        self.stack = []
