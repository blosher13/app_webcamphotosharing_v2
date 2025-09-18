from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
import time, os, webbrowser

Builder.load_file('frontend/main.kv')

#One class for each screen
class CameraScreen(Screen):

    def start(self):
        self.ids.webcam.opacity = 1
        self.manager.current_screen.ids.webcam.play = True
        self.manager.current_screen.ids.webcam_button.text = 'Stop Webcam'
        self.ids.webcam.texture = self.ids.webcam._camera.texture    
    
    def end(self):
        self.ids.webcam.opacity = 0
        self.manager.current_screen.ids.webcam_button.text = 'Start Webcam'
        self.manager.current_screen.ids.webcam.play = False
        self.ids.webcam.texture = None    
    
    def capture(self):
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.filepath = f'photos/{current_time}.png'
        self.ids.webcam.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath
class ImageScreen(Screen):
    link_error_message = 'Create a link first!'

    def create_link(self):
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        abs_file_path = os.path.abspath(file_path)
        self.full_file_path = f'file:///{abs_file_path}'
        self.ids.url_link.text = self.full_file_path

    def copy_link(self):
        try:
            Clipboard.copy(self.full_file_path)
        except:
            self.ids.url_link.text = self.link_error_message
    def open_link(self):
        try:
            webbrowser.open(self.full_file_path)
        except:
            self.ids.url_link.text = self.link_error_message

    
#Manage the various screens
class RootWidget(ScreenManager):
    pass

#Main application area
class MainApp(App):

    def build(self):
        #RootWidget is initalized
        return RootWidget()

MainApp().run()