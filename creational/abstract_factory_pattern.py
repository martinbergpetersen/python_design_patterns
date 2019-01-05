# Abstract factory pattern is a creational design pattern
# that let use create object of families related object
# without specifying the concrete implementation.

import abc


class ComponentFactory(object):  # FACTORY
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create_button(self):
        pass


class IOSFactory(ComponentFactory):
    def create_button(self):
        return IOSButton()


class WINFactory(ComponentFactory):

    def create_button(self):
        return WinButton()


class LinuxFactory(ComponentFactory):

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

    def button(self):
        button = self.factory.create_button()
        button.render()


l_factory = LinuxFactory()
w_factory = WINFactory()
ios_factory = IOSFactory()


l_app = Application(l_factory)
l_app.button()

w_app = Application(w_factory)
w_app.button()

ios_app = Application(ios_factory)
ios_app.button()
