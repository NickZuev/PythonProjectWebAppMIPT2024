# PythonProjectWebAppMIPT2024
My Python web project as a part of respective MIPT course. It's an app mostly for ordinal calculations

## О приложении простыми словами:  
Наиболее ценной частью данного приложения будет та часть, которая отвечает за подсчёт [ординалов](https://en.wikipedia.org/wiki/Ordinal_number), вплоть до $\varepsilon_0$, однако помимо этого приложение будет предоставлять возможность проверить пользователю свои навыки устного счёта ординалов. 

## Функционал
Счёт ординалов, взаимодействие с пользователем с помощью бота для предоставляения ему задач и отображения результата, функционал для перевода строкового представления ординалов в ординалы и наоборот.

## Архитектура:
1. class OrdinalNumber - отвечает за расчёты ординалов
##### Методы:
1. cut_head - позволяет получить мажорирующее слагаемое в КНФ
2. is_zero - равен ли ординал нулю
3. is_number - проверяет натуральное ли число
4. copy - копирует ординал и возвращает как результат
5. <, >, $\leqslant$, $\geqslant$, =, $\neq$, +, $\cdot$, ^
6. get_string - возвращает строкове представление ординала в КНФ

Отдельно в main.py лежат много функций, отвечающие за работу бота.
