from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file('frontend/main.kv')

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
        #RootWidget is initalized
        return RootWidget()

MainApp().run()