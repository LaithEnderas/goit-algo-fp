# pythagoras tree with turtle
# користувач задає рівень рекурсії
# коментарі в простому стилі

import turtle

# параметри полотна
W, H = 1000, 800

# малюємо квадрат від даної точки з кутом повороту і розміром
def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.left(90)

# рекурсивне малювання дерева
def pythagoras_tree(t, size, level):
    # базовий випадок
    if level == 0 or size < 2:
        draw_square(t, size)
        return

    # малюємо поточний квадрат
    draw_square(t, size)

    # позиціонуємося до лівого верхнього кута
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.right(90)

    # розмір дочірніх квадратів
    # класичне співвідношення через прямокутний трикутник
    left_size = size * (2 ** 0.5) / 2
    right_size = size * (2 ** 0.5) / 2

    # гілка ліворуч
    t.left(45)
    pythagoras_tree(t, left_size, level - 1)
    t.right(45)

    # перейти до вершини правої гілки
    t.right(90)
    t.forward(size)
    t.left(90)

    # гілка праворуч
    t.right(45)
    pythagoras_tree(t, right_size, level - 1)
    t.left(45)

    # повертаємося в початковий стан для цього вузла
    t.left(90)
    t.forward(size)
    t.right(90)
    t.backward(size)

def main():
    # читаємо рівень рекурсії
    try:
        level = int(input("enter recursion level 0..12: ").strip() or "8")
    except:
        level = 8
    level = max(0, min(level, 12))  # обмеження для швидкодії

    screen = turtle.Screen()
    screen.setup(W, H)
    screen.title(f"pythagoras tree, level {level}")
    screen.tracer(False)  # пришвидшує відмальовування

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()

    # стартова позиція внизу по центру
    base = H * 0.18
    t.setpos(-base / 2, -H * 0.38)
    t.setheading(0)
    t.pendown()

    pythagoras_tree(t, base, level)

    screen.tracer(True)
    turtle.done()

if __name__ == "__main__":
    main()
