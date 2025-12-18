class TodoManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"추가됨: {task}\n")

    def show_tasks(self):
        if not self.tasks:
            print("할 일이 없습니다.")
            return

        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")
    
    def remove_task(self, index):
        if 1 <= index <= len(self.tasks):
            removed = self.tasks.pop(index - 1)
            print(f"삭제됨: {removed}\n")
        else:
            print("존재하지 않는 번호입니다.\n")
