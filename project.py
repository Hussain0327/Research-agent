
assignment = [] ## This is a float, this can be changed and removed and editted, ect

# [weights] is a tuples, this cant be changed, ex) the score on a test you scored.
weights = [
    ("Homework", 40),
    ("Quizzes", 20),
    ("Midterms", 20),
    ("Final", 20),
    ("Projects", 10),
]

# Def add assignment function allows user to add and enter assignment details
def add_assignment():
    title = input("Title: ").strip()
    due = input("Due date (e.g., 2025-09-26): ").strip()
    try:
        scored = float(input("Points scored: ").strip())
        possible = float(input("Points possible: ").strip())
    except ValueError:
        print("Invalid number. Try again.")
        return
    if possible <= 0:
        print("Points possible must be > 0.")
        return
    assignment.append((title, due, scored, possible))
    print("Added.")

def list_assignments():
    if len(assignment) == 0:
        print("No assignments yet.")
        return
    total_scored = 0.0
    total_possible = 0.0
    print("\nAssignments:")
    for i, item in enumerate(assignment, start=1):
        title, due, scored, possible = item
        pct = (scored / possible) * 100.0
        print(f"{i}. {title} (due {due}) — {scored}/{possible} = {pct:.1f}%")
        total_scored += scored
        total_possible += possible
    overall = (total_scored / total_possible) * 100.0 if total_possible > 0 else 0.0
    print(f"Total: {total_scored:.1f}/{total_possible:.1f} = {overall:.2f}%\n")

def grade_estimator():
    print("\nEnter your current average for each category (0–100).")
    total = 0.0
    for name, w in weights:
        while True:
            raw = input(f"{name} average (%), weight {w}%: ").strip()
            try:
                x = float(raw)
            except ValueError:
                print("Not a number, try again.")
                continue
            if x < 0 or x > 100:
                print("Enter 0–100.")
                continue
            total += x * (w / 100.0)
            break
    print(f"\nEstimated overall grade: {total:.2f}%\n")

def show_weights():
    print("\nCurrent weights:")
    for name, w in weights:
        print(f"- {name}: {w}%")
    print("Total should be 100%.\n")

def main_menu():
    while True:
        print("== Study Buddy v0.1 ==")
        print("1) Add assignment")
        print("2) List assignments")
        print("3) Show course weights")
        print("4) Grade estimator")
        print("5) Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_assignment()
        elif choice == "2":
            list_assignments()
        elif choice == "3":
            show_weights()
        elif choice == "4":
            grade_estimator()
        elif choice == "5":
            print("Bye.")
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main_menu()