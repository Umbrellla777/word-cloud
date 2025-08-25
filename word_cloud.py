import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
from PIL import Image

shapes = {
    "1": ("Квадрат", None),
    "2": ("Сердце", "mask_heart.png"),
    "3": ("Звезда", "mask_star.png"),
    "4": ("Облако", "mask_cloud.png"),
    "5": ("Кастом маска 1", "mask_castom1.png"),
    "6": ("Кастом маска 2", "mask_castom2.png"),
    "7": ("Кастом маска 3", "mask_castom3.png"),
}

colors = {
    "1": ("Яркая радуга", "rainbow"),
    "2": ("Плазма", "plasma"),
    "3": ("Океан", "ocean"),
    "4": ("Осень", "autumn"),
    "5": ("Зима", "winter"),
    "6": ("Весна", "spring"),
    "7": ("Лето", "summer"),
    "8": ("Классика (черно-белая)", "binary"),
    "9": ("Контраст (coolwarm)", "coolwarm")
}

backgrounds = {
    "1": ("Белый", "white"),
    "2": ("Черный", "black")
}

def generate_wordcloud(text_file, mask_file=None, output_file="wordcloud.png",
                       colormap="plasma", background="white"):
    with open(text_file, "r", encoding="utf-8") as f:
        text = f.read()

    mask = None
    if mask_file:
        mask_img = Image.open(mask_file).convert("L")
        mask = np.array(mask_img)

    wc = WordCloud(
        font_path="arial.ttf",  
        width=2000,
        height=2000,
        background_color=background,
        colormap=colormap,
        mask=mask,
        max_words=5000,  
        min_font_size=10, 
        collocations=False   
    ).generate(text)

    # Сохраняем итоговое облако
    wc.to_file(output_file)
    print(f"✅ Итоговое облако слов сохранено как {output_file}")

    # Отображаем
    plt.figure(figsize=(20, 20))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("Выбери форму облака:")
    for key, (name, _) in shapes.items():
        print(f"{key}. {name}")
    shape_choice = input("👉 Введи номер: ").strip()
    shape_name, mask_file = shapes.get(shape_choice, shapes["1"])

    print("\nВыбери цветовую схему:")
    for key, (name, _) in colors.items():
        print(f"{key}. {name}")
    color_choice = input("👉 Введи номер: ").strip()
    color_name, colormap = colors.get(color_choice, colors["2"])

    print("\nВыбери цвет фона:")
    for key, (name, _) in backgrounds.items():
        print(f"{key}. {name}")
    bg_choice = input("👉 Введи номер: ").strip()
    bg_name, background_color = backgrounds.get(bg_choice, backgrounds["1"])

    print(f"\n✅ Выбрана форма: {shape_name}, палитра: {color_name}, фон: {bg_name}")

    generate_wordcloud(
        text_file="words.txt",
        mask_file=mask_file,
        output_file="cloud.png",
        colormap=colormap,
        background=background_color
    )
