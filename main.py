from todo import TodoManager
from utils import print_menu

def main():
    manager = TodoManager()

    while True:
        print_menu()
        choice = input("선택: ")

        if choice == "1":
            task = input("할 일 입력: ").strip()
            if not task:
                print("빈 할 일은 추가할 수 없습니다.")
            else:
                manager.add_task(task)
        elif choice == "2":
            manager.show_tasks()
        elif choice == "3":
            manager.show_tasks()
            try:
                index = int(input("삭제할 번호: "))
                manager.remove_task(index)
            except ValueError:
                print("숫자를 입력해주세요.")
        elif choice == "4":
            print("프로그램 종료")
            break
        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    main()
