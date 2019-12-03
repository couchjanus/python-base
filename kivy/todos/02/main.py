'''
Todos
=====

Todo application for management projects.

'''

__version__ = '0.1'

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ListProperty, AliasProperty
from kivy.uix.boxlayout import BoxLayout

class Projects(Screen):

    data = ListProperty()

    def _get_data_for_widgets(self):
        pass

class TodoApp(App):

    def build(self):
        self.load_projects()
        # Create the manager
        root = ScreenManager()
        # Когда вы создаете экран, вам обязательно нужно дать ему имя:
        self.projects = Projects(name='projects')
        root.add_widget(self.projects)
        return root

    def load_projects(self):
        pass

    def go_projects(self):
        pass

    def add_project(self):
        pass

    def edit_project(self, project_index):
        pass

    def del_project(self, project_index):
        pass

if __name__ == "__main__":
    TodoApp().run()
