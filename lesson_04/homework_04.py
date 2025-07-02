from operator import index

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""



##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(f'Замінили абзац на пробіл:\n{adwentures_of_tom_sawer}')

# task 02 ==
""" Замініть .... на пробіл
"""
### замінюємо .... на пробіли (одна крапка - один пробіл)
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

### split() за замовчуванням розбиває рядок на список слів, ігноруючи всі пробіли між ними
### " ".join обьеднує рядок з пробілами між словами
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split()) #
print(f'Замінили "...." на пробіл:\n{adwentures_of_tom_sawer}')

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

count = adwentures_of_tom_sawer.count("h")
print(f'Літера "h" зустрічається у тексті {count} разів')

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

words = adwentures_of_tom_sawer.split()
count = 0
for word in words:
    if word[0].isupper():
        count += 1
print(f'У тексті {count} слів, кортрі починаються з великої літери')


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

index = adwentures_of_tom_sawer.find("Tom", 2)
print(f'Слово "Tom" другий раз зустрічається на {index} позиції')


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".")
# невеличкий костиль, бо не зміг по іншому позбутись пустого елементу у кінці списка
adwentures_of_tom_sawer_sentences.reverse()
del adwentures_of_tom_sawer_sentences[0]
adwentures_of_tom_sawer_sentences.reverse()
print(f'Розділення по кінцю речення:\n{adwentures_of_tom_sawer_sentences}')
# Думаю що є більш красиве і привильне рішення. На жаль я його не знайшов

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

print(f'Четверте речення:\n{adwentures_of_tom_sawer_sentences[3]}')
print(f'Четверте речення у нижньому регістрі:\n{adwentures_of_tom_sawer_sentences[3].lower()}')

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
words = "By the time"
for i, sentence in enumerate(adwentures_of_tom_sawer_sentences): # дає індекс реченню на кожній ітерації.
    if words in sentence:
        print(f'Речення яке почитнається з "By the time" знайдено:\n{sentence}\n і його номер {i + 1}')

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

last_sentence = adwentures_of_tom_sawer_sentences[-1]
last_sentence = last_sentence.strip()
words_quantity = last_sentence.split(" ")
print(f'Кількість слів у останньому реченні дорівнює {len(words_quantity)}')