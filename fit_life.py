import sys

sys.stdout.reconfigure(encoding='utf-8')

# Константы:
WATER_PER_KG = 30
BMI_HEIGHT = 2
ML_TO_L = 1000


# step 1
user_name = input('Приветствую тебя, как к тебе можно обращаться?')
user_age = int(input('Сколько вам полных лет?'))

# step 2
try:
    user_weight = float(input('Введите Ваш вес в кг (например, 70.5): '))
except ValueError:
    print('Вы ввели вес не так, как в примере, попробуйте еще раз')

try:
    user_height = float(input('Введите Ваш рост в метрах (например, 1.92): '))
except ValueError:
    print('Вы ввели рост не так, как в примере, попробуйте еще раз')

# Step 3
bmi = round(user_weight / (user_height ** BMI_HEIGHT), 1)
water_needed_ml = user_weight * WATER_PER_KG
water_needed_l = round(water_needed_ml / ML_TO_L, 1)

# Step 4
print(f'Приятно познакомиться {user_name}, Ваш возраст {user_age}')
print(f'Ваш Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_needed_l} л. в день')
print("Расчет окончен. Будьте здоровы!")
