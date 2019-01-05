# Abstract factory pattern is a creational design pattern
# that let use create object of families related object
# without specifying the concrete implementation.

import abc


class Dialog(object):  # FACTORY
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create_button(self):
        pass

    def render(self):
        button = self.create_button()
        button.render()


class IOSDialog(Dialog):
    def create_button(self):
        return IOSButton()


class WinDialog(Dialog):

    def create_button(self):
        return WinButton()


class LinuxDialog(Dialog):

    def create_button(self):
        return LinuxButton()


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

    def render(self):
        self.factory.render()


l_dialog = LinuxDialog()
w_dialog = WinDialog()
ios_dialog = IOSDialog()


l_app = Application(l_dialog)
l_app.render()
w_app = Application(w_dialog)
w_app.render()
ios_app = Application(ios_dialog)
ios_app.render()
