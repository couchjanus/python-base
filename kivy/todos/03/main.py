'''
Todos
=====

Todo application for management projects.

'''

__version__ = '0.1'

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ListProperty, StringProperty, \
        NumericProperty, BooleanProperty, AliasProperty

from kivy.uix.boxlayout import BoxLayout

class ProjectListItem(BoxLayout):
    project_description = StringProperty()
    project_title = StringProperty()
    project_index = NumericProperty()
    project_deadline = StringProperty()

class Projects(Screen):

    data = ListProperty()


    def _get_data_for_widgets(self):
        return [{
            'project_index': index,
            'project_title': item['title'],
            'project_description': item['description'],
            'project_deadline': item['deadline']}
            for index, item in enumerate(self.data)]

    data_for_widgets = AliasProperty(_get_data_for_widgets, bind=['data'])

class TodoApp(App):

    def build(self):
        self.projects = Projects(name='projects')
        self.load_projects()
        root = ScreenManager()

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
