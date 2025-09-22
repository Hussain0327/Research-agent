
# Enhanced Turtle Drawing Program
import turtle


def draw_spiral(t, turns, length, pen_size, colors):
    """Draw a colorful spiral with the turtle."""
    t.pensize(pen_size)
    for i in range(turns):
        t.pencolor(colors[i % len(colors)])
        t.forward(length + i * 5)
        t.right(89)  # 89 for a more interesting spiral


def main():
    import random
    # Set up the screen
    s = turtle.Screen()
    s.bgcolor("black")
    s.title("Interactive Turtle Spiral!")

    # Greet the user
    print("Welcome to the Interactive Turtle Spiral!")
    name = input("What's your name? ").strip().title()
    print(f"Hi, {name}! Let's make some art.")

    # Get user preferences
    try:
        turns = int(input("How many turns should the spiral have? (e.g. 50): "))
        length = int(input("What should be the starting length? (e.g. 20): "))
        pen_size = int(input("Pen size? (e.g. 3): "))
    except ValueError:
        print("Invalid input, using default values.")
        turns, length, pen_size = 50, 20, 3

    # Choose color palette
    palettes = {
        'rainbow': ["red", "orange", "yellow", "green", "blue", "purple"],
        'cool': ["#00BFFF", "#1E90FF", "#00FA9A", "#20B2AA", "#7FFFD4"],
        'warm': ["#FF6347", "#FF8C00", "#FFD700", "#FF4500", "#FF1493"]
    }
    print("Color palettes: rainbow, cool, warm")
    palette_choice = input("Choose a color palette: ").strip().lower()
    colors = palettes.get(palette_choice, palettes['rainbow'])

    # Set up the turtle
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    # Draw the spiral
    draw_spiral(t, turns, length, pen_size, colors)

    # Write a message in the center
    t.penup()
    t.goto(0, 0)
    t.pencolor("white")
    t.write(f"Art by {name}", align="center", font=("Arial", 16, "bold"))

    s.mainloop()

if __name__ == "__main__":
    main()
