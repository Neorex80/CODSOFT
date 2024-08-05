import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget, QMessageBox

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('To-Do List')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText('Enter a new task')
        layout.addWidget(self.task_input)

        btn_layout = QHBoxLayout()
        self.add_task_btn = QPushButton('Add Task', self)
        self.add_task_btn.clicked.connect(self.add_task)
        btn_layout.addWidget(self.add_task_btn)

        self.delete_task_btn = QPushButton('Delete Task', self)
        self.delete_task_btn.clicked.connect(self.delete_task)
        btn_layout.addWidget(self.delete_task_btn)

        layout.addLayout(btn_layout)

        self.task_list = QListWidget(self)
        layout.addWidget(self.task_list)

        self.setLayout(layout)

    def add_task(self):
        task = self.task_input.text()
        if task:
            self.task_list.addItem(task)
            self.task_input.clear()
        else:
            QMessageBox.warning(self, 'Warning', 'Task cannot be empty')

    def delete_task(self):
        selected_task = self.task_list.currentRow()
        if selected_task >= 0:
            self.task_list.takeItem(selected_task)
        else:
            QMessageBox.warning(self, 'Warning', 'No task selected')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())
