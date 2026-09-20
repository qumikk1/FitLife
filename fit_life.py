import sys

sys.stdout.reconfigure(encoding='utf-8')

# step 1
user_name = input('Приветствую тебя, как к тебе можно обращаться?')
user_age = int(input('Сколько вам полных лет?'))

# step 2
user_weight = float(input('Какой у Вас вес (в кг)?'))
user_height = float(input('Какой у Вас рост (в метрах)?'))

# Step 3 
bmi = round(user_weight / (user_height ** 2), 1)
water_needed_ml = user_weight * 30
water_needed_l = round(water_needed_ml / 1000, 1)

# Step 4
print(f'Приятно познакомиться {user_name}, Ваш возраст {user_age}')
print(f'Ваш Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_needed_l} л. в день')
print("Расчет окончен. Будьте здоровы!")