class ToDoList:
    tasks = []

    def addTask(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added to the ToDo list.')

    def viewTasks(self):
        if not self.tasks:
            print('No tasks in the ToDo list.')
        else:
            print('ToDo List:')
            for index, task in enumerate(self.tasks, start=1):
                print(f'{index}. {task}')

    def removeTask(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f'Task "{removed_task}" removed from the ToDo list.')
        else:
            print('Invalid task index. Please try again.')

def main():
    todoList = ToDoList()

    while True:
        print('\nOptions:')
        print('1. Add Task')
        print('2. View Tasks')
        print('3. Remove Task')
        print('4. Quit')

        choice = input('Enter your choice : ')

        if choice == '1':
            task = input('Enter the task: ')
            todoList.addTask(task)
        elif choice == '2':
            todoList.viewTasks();
        elif choice == '3':
            task_index = int(input('Enter the task index to remove: '))
            todoList.removeTask(task_index)
        elif choice == '4':
            print('Exiting the ToDo list program. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 4.')

main()
