from PIL import Image


def save_ppm(filename, width, height, pixels):
    with open(filename, 'w') as f:
        f.write(f"P3\n{width} {height}\n255\n")
        for row in pixels:
            for (r, g, b) in row:
                f.write(f"{r} {g} {b} ")
            f.write("\n")


def create_canvas(w, h, color):
    return [[color for _ in range(w)] for _ in range(h)]


def draw_rect(canvas, x1, y1, x2, y2, color):
    for y in range(y1, y2):
        for x in range(x1, x2):
            canvas[y][x] = color


# ------------------------
# (a) Modelo 0 - bloco único
# ------------------------
def image0():
    w, h = 256, 256
    canvas = create_canvas(w, h, (180, 180, 180))  # cinza médio

    save_ppm("img0.ppm", w, h, canvas)
    Image.open("img0.ppm").show()


# ------------------------
# (b) Modelo 1 - rosto simples
# ------------------------
def image1():
    w, h = 256, 256
    canvas = create_canvas(w, h, (200, 200, 200))  # fundo claro

    # faixa superior
    draw_rect(canvas, 0, 0, 256, 128, (90, 90, 90))

    # olhos
    draw_rect(canvas, 60, 40, 100, 70, (220, 220, 220))
    draw_rect(canvas, 156, 40, 196, 70, (220, 220, 220))

    # boca (dois blocos)
    draw_rect(canvas, 70, 150, 110, 180, (80, 80, 80))
    draw_rect(canvas, 146, 150, 186, 180, (80, 80, 80))

    save_ppm("img1.ppm", w, h, canvas)
    Image.open("img1.ppm").show()


# ------------------------
# (c) Modelo 2 - quadrantes
# ------------------------
def image2():
    w, h = 256, 256
    canvas = create_canvas(w, h, (0, 0, 0))

    # 4 quadrantes
    draw_rect(canvas, 0, 0, 128, 128, (90, 90, 90))       # escuro
    draw_rect(canvas, 128, 0, 256, 128, (180, 180, 180))  # médio
    draw_rect(canvas, 0, 128, 128, 256, (200, 200, 200))  # claro
    draw_rect(canvas, 128, 128, 256, 256, (230, 230, 230))# mais claro

    save_ppm("img2.ppm", w, h, canvas)
    Image.open("img2.ppm").show()


# ------------------------
# (d) Modelo 3 - metade/metade
# ------------------------
def image3():
    w, h = 256, 256
    canvas = create_canvas(w, h, (220, 220, 220))  # claro

    # metade inferior escura
    draw_rect(canvas, 0, 128, 256, 256, (90, 90, 90))

    save_ppm("img3.ppm", w, h, canvas)
    Image.open("img3.ppm").show()


# ------------------------
# (e) Modelo 4 (o seu)
# ------------------------
def image4():
    w, h = 256, 256
    canvas = create_canvas(w, h, (0, 0, 0))
    cell = 64
    total = 16

    for row in range(4):
        for col in range(4):
            x1, y1 = col * cell, row * cell
            x2, y2 = x1 + cell, y1 + cell
            index = row * 4 + col

            gray = int(255 - (index * (255 / (total - 1))))
            color = (gray, gray, gray)

            draw_rect(canvas, x1, y1, x2, y2, color)

    save_ppm("img4.ppm", w, h, canvas)
    Image.open("img4.ppm").show()


# ------------------------
# EXECUÇÃO
# ------------------------
if __name__ == "__main__":
    image0()
    image1()
    image2()
    image3()
    image4()