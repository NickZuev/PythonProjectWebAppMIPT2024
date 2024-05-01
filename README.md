# PythonProjectWebAppMIPT2024
My Python web project as a part of respective MIPT course. It's an app mostly for ordinal calculations

## О приложении простыми словами:  
Наиболее ценной частью данного приложения будет та часть, которая отвечает за подсчёт [ординалов](https://en.wikipedia.org/wiki/Ordinal_number), вплоть до $\varepsilon_0$, однако помимо этого приложение будет предоставлять возможность проверить пользователю свои навыки устного счёта ординалов. 

## Функционал
Счёт ординалов, взаимодействие с пользователем с помощью сайта или бота для предоставляения ему задач и отображения результата, функционал для перевода строкового представления ординалов в ординалы и наоборот.

## Архитектура:
1. class App - отвечает за работу приложения
2. class ordinal - отвечает за расчёты ординалов
3. class converter - отвечает за представления ординала в виде строки и наоборот(в дальнейшем, быть может, будет заменён набором функций)
