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


class IOSFactory(ComponentFactory):
    def create_button(self):
        return IOSButton()

    def create_checkbox(self):
        return IOSCheckbox()


class WINFactory(ComponentFactory):

    def create_button(self):
        return WinButton()

    def create_checkbox(self):
        return WinCheckbox()


class LinuxFactory(ComponentFactory):

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


class Application(object):
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


l_factory = LinuxFactory()
w_factory = WINFactory()
ios_factory = IOSFactory()


l_app = Application(l_factory)
l_app.button()
l_app.checkbox()
l_app.table()

w_app = Application(w_factory)
w_app.button()
w_app.checkbox()
w_app.table()

ios_app = Application(ios_factory)
ios_app.button()
ios_app.checkbox()
ios_app.table()
