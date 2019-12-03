'''
Todos
=====

Todo application for management projects.

'''

__version__ = '0.1'

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import ListProperty, StringProperty, \
        NumericProperty, BooleanProperty, AliasProperty
from kivy.uix.boxlayout import BoxLayout

class ProjectView(Screen):

    project_index = NumericProperty()
    project_title = StringProperty()
    project_description = StringProperty()


class ProjectListItem(BoxLayout):
    project_description = StringProperty()
    project_title = StringProperty()
    project_deadline = StringProperty()
    project_index = NumericProperty()

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
        self.transition = SlideTransition(duration=.35)
        root = ScreenManager(transition=self.transition)
        root.add_widget(self.projects)
        return root

    def load_projects(self):
        pass

    def go_projects(self):
        pass

    def add_project(self):
        self.projects.data.append({'title': 'New project', 'description': '', 'deadline': ''})
        project_index = len(self.projects.data) - 1
        self.edit_project(project_index)

    def edit_project(self, project_index):
        pass

    def del_project(self, project_index):
        pass

if __name__ == "__main__":
    TodoApp().run()
