from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

#One class for each screen
class FirstScreen(Screen):

    def search_image(self):
        pass
class SecondScreen(Screen):

    def search_image(self):
        pass
    
#Manage the various screens
class RootWidget(ScreenManager):
    pass

#Main application area
class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()