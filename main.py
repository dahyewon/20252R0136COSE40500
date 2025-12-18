from todo import TodoManager
from utils import print_menu

def main():
    manager = TodoManager()

    while True:
        print_menu()
        choice = input("선택: ")

        if choice == "1":
            task = input("할 일 입력: ")
            manager.add_task(task)
        elif choice == "2":
            manager.show_tasks()
        elif choice == "3":
            manager.show_tasks()
            index = int(input("삭제할 번호: "))
            manager.remove_task(index)
        elif choice == "4":
            print("프로그램 종료")
            break
        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    main()
