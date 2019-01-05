import abc


class ComponentFactory(object):  # FACTORY
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create_button(self):
        pass

    @abc.abstractmethod
    def create_checkbox(self):
        pass

    def create_table(self):
        print "I am an universal table"


class IOSComponentFactory(ComponentFactory):
    def create_button(self):
        return IOSButton()

    def create_checkbox(self):
        return IOSCheckbox()


class WINComponentFactory(ComponentFactory):

    def create_button(self):
        return WinButton()

    def create_checkbox(self):
        return WinCheckbox()


class LinuxComponentFactory(ComponentFactory):

    def create_button(self):
        return LinuxButton()

    def create_checkbox(self):
        return LinuxCheckbox()


class Checkbox(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def render(self):
        pass


class WinCheckbox(Checkbox):

    def render(self):
        print "I am a WINDOW checkbox"


class LinuxCheckbox(Checkbox):

    def render(self):
        print "I am a LINUX checkbox"


class IOSCheckbox(Checkbox):

    def render(self):
        print "I am a IOS checkbox"


class Button(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def render(self):
        pass


class WinButton(Button):

    def render(self):
        print "I am a WINDOW button"


class LinuxButton(Button):

    def render(self):
        print "I am a LINUX button"


class IOSButton(Button):

    def render(self):
        print "I am a IOS button"


class GUI(object):
    def __init__(self, factory):
        self.factory = factory

    def button(self):
        button = self.factory.create_button()
        button.render()

    def checkbox(self):
        checkbox = self.factory.create_checkbox()
        checkbox.render()

    def table(self):
        self.factory.create_table()


l_factory = LinuxComponentFactory()
w_factory = WINComponentFactory()
ios_factory = IOSComponentFactory()


l_app = GUI(l_factory)
l_app.button()
l_app.checkbox()
l_app.table()

w_app = GUI(w_factory)
w_app.button()
w_app.checkbox()
w_app.table()

ios_app = GUI(ios_factory)
ios_app.button()
ios_app.checkbox()
ios_app.table()
