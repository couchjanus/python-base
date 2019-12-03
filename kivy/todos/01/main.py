'''
Todos
=====

Todo application for management projects.

'''

__version__ = '0.1'

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ListProperty, AliasProperty

class Projects(Screen):

    data = ListProperty()

    def _get_data_for_widgets(self):
        pass

class TodoApp(App):

    def build(self):
        self.projects = Projects(name='projects')
        self.load_projects()
        root = ScreenManager()
        root.add_widget(self.projects)
        return root

    def load_projects(self):
        pass

if __name__ == "__main__":
    TodoApp().run()
