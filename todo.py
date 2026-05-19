import json
import os
from datetime import datetime

TODO_FILE = "todos.json"

def load_todos():
    """Load todos from file."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

def save_todos(todos):
    """Save todos to file."""
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=2)

def display_todos(todos):
    """Display all todos."""
    print("\n" + "=" * 50)
    print("   📝 YOUR TO-DO LIST")
    print("=" * 50)

    if not todos:
        print("  No tasks yet! Add one below.")
        return

    done = [t for t in todos if t["done"]]
    pending = [t for t in todos if not t["done"]]

    if pending:
        print(f"\n  ⏳ PENDING ({len(pending)})")
        for i, todo in enumerate(todos):
            if not todo["done"]:
                print(f"  [{i+1}] ○ {todo['task']}  ({todo['date']})")

    if done:
        print(f"\n  ✅ COMPLETED ({len(done)})")
        for i, todo in enumerate(todos):
            if todo["done"]:
                print(f"  [{i+1}] ✓ {todo['task']}  ({todo['date']})")

    print()

def add_todo(todos):
    """Add a new todo."""
    task = input("  Enter task: ").strip()
    if not task:
        print("  ⚠️  Task cannot be empty!")
        return
    todos.append({
        "task": task,
        "done": False,
        "date": datetime.now().strftime("%b %d, %Y")
    })
    save_todos(todos)
    print(f"  ✅ Added: {task}")

def complete_todo(todos):
    """Mark a todo as complete."""
    display_todos(todos)
    if not todos:
        return
    try:
        num = int(input("  Enter task number to complete: ")) - 1
        if 0 <= num < len(todos):
            if todos[num]["done"]:
                print("  ⚠️  Already completed!")
            else:
                todos[num]["done"] = True
                save_todos(todos)
                print(f"  ✅ Completed: {todos[num]['task']}")
        else:
            print("  ⚠️  Invalid number!")
    except ValueError:
        print("  ⚠️  Please enter a valid number!")

def delete_todo(todos):
    """Delete a todo."""
    display_todos(todos)
    if not todos:
        return
    try:
        num = int(input("  Enter task number to delete: ")) - 1
        if 0 <= num < len(todos):
            removed = todos.pop(num)
            save_todos(todos)
            print(f"  🗑️  Deleted: {removed['task']}")
        else:
            print("  ⚠️  Invalid number!")
    except ValueError:
        print("  ⚠️  Please enter a valid number!")

def clear_completed(todos):
    """Clear all completed todos."""
    before = len(todos)
    todos[:] = [t for t in todos if not t["done"]]
    save_todos(todos)
    cleared = before - len(todos)
    print(f"  🗑️  Cleared {cleared} completed task(s)!")

def main():
    """Main app function."""
    print("\n" + "=" * 50)
    print("   📝 PYTHON TO-DO LIST APP")
    print("   Your tasks are saved automatically!")
    print("=" * 50)

    todos = load_todos()

    while True:
        print("\n  MENU:")
        print("  1. 📋 View tasks")
        print("  2. ➕ Add task")
        print("  3. ✅ Complete task")
        print("  4. 🗑️  Delete task")
        print("  5. 🧹 Clear completed")
        print("  6. 🚪 Exit")
        print("-" * 50)

        choice = input("  Choose (1-6): ").strip()

        if choice == "1":
            display_todos(todos)
        elif choice == "2":
            add_todo(todos)
        elif choice == "3":
            complete_todo(todos)
        elif choice == "4":
            delete_todo(todos)
        elif choice == "5":
            clear_completed(todos)
        elif choice == "6":
            print("\n  👋 Goodbye! Your tasks are saved.\n")
            break
        else:
            print("  ⚠️  Invalid choice!")

if __name__ == "__main__":
    main()
