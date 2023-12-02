# Uir_2023
## Ru description
Программы написаны на python версии 3.11.5.

Каждая из лабораторных работ хранится в отдельной папке вида `lab<number_of_lab>`

Решение в виде програмы вида `lab<number_of_lab>.py`

Решение в виде блок схемы:
* В формате png вида `diagram_lab<number_of_lab>.png`
* В формате json вида `diagram_lab<number_of_lab>.json`
> Сайт для создания блок-схем: https://programforyou.ru/block-diagram-redactor в него можно импортировать json файл с блок схемой.

Проверка:
* С помощью таблиц эксель вида `Check_lab<number_of_lab>.xlsx`
* С помощью сторонних в виде сохраненного скриншота  `Check_lab<number_of_lab>_<number_of_exr>.jpeg`
Отчет в виде текстового файла `Otchet_lab<number_of_lab>.docx`

Так же для некотрых программ есть wiki.
---
### Задания лабораторных работ:
- [x] lab 1

  1. Даны произвольные x,y,z. Вычислить a,b, если:
      * a = |5-2*e|/((1+x^2)*(y - tg(z)))
      * b = |y-4|+((y-x)^2)/6+((x-y)^2)/7
  2. Вычислить значение функции f(x) = a*(x^b+x)/3-x^(3/4), где a = 2,b = -1 – константы, x изменяется от 4 до 5.5 с шагом h= 0.15.
  3. Вычислить значение функции f(x) = sqrt(ln(cos(sqrt(x))))) , при x от 1 до 3 с шагом h = 0.1.
  4. Треугольник задан координатами (x1, y1), (x2, y2), (x3, y3) своих вершин. Найти периметр и площадь треугольника. 
  5. Скорость первого автомобиля V1 км/ч, второго — V2 км/ч, расстояние между ними S км. Определить расстояние между ними через T часов, если автомобили удаляются друг от друга. Данное расстояние равно сумме начального расстояния и общего пути, проделанного       автомобилями; общий путь = время · суммарная скорость.
Входные данные: ввести четыре любых числа V1, V2, S, T   (1<= V1, V2, S, T <=100).
Выходные данные: вывести расстояние между автобусами через Т часов с точностью до 4 цифр в дробной части.
  6. Даны два ненулевых числа. Найти сумму, разность, произведение и частное их квадратов. 
Входные данные: ввести два целых числа  а и b (1<=a,b<=100).
Выходные данные: вывести сумму, разность, произведение и частное их квадратов  с точностью до 3 цифр в дробной части в разных строках.
  7. Найти значение функции y = 3x6 – 6x2 – 7 при данном значении x. 
Входные данные: ввести одно целое число  x (-10<=x<=10).
Выходные данные: вывести  значение y.
  8. Найти решение системы линейных уравнений вида 
A1·x + B1·y = C1,
A2·x + B2·y = C2,
заданной своими коэффициентами A1, B1, C1, A2, B2, C2, если известно, что данная система имеет единственное решение. Воспользоваться формулами 
x = (C1·B2 – C2·B1)/D,        y = (A1·C2 – A2·C1)/D,
где D = A1·B2 – A2·B1.
Входные данные: ввести шесть любых  чисел A1, B1,С1, A2, B2, С2 (-10<= A1, B1,С1, A2, B2, С2 <=10).
Выходные данные: вывести в первой строке значение х, а  во второй строке y  с точностью до 4 цифр в дробной части.
  9.Три предпринимателя - Давыдов, Петров и Максимов вложили в совместную организацию предприятия по производству специальной дачной мебели деньги. Первый вложил 60 тыс. руб., второй - 90 тыс. руб., а третий - 150 тыс. руб. Они получили прибыль в размере 117 тыс. руб. Сколько денег из прибыли получит каждый из предпринимателей при условии распределения ее пропорционально их вкладам?

- [x] lab2
      
  1. Реализовать просто разовую игру. Для запуска раунда надо перезапускать скрипт. Камень-ножниы-бумага.
  2. Реализовать игру с последующим приглашением повторить игру.
  3. Реализовать турнирную игру. При запуске игры пользователю выводится сообщение с выбором режима игры. Если выбран просто игра, то возвращается режим из ур.2. Если выбирает турнир, то предлагается ввести кол-во раундов. После этого проигрывается заданное кол-во   раундов и выводится итог турнира. Например: «Поздравляю, Вы победили со счетом 2:1»
  4. Необходимо заполнить матрицу А[n*n] по одному из описанных алгоритов. Затем отразить ее "зеркально" вправо, получив при этом матрицу размера B[n*2n]. Полученную матрицу B отразить "зеркально" вниз, полив матрицу C [2n*2n].
     
- [ ]

  
## ENG description
The program is written in python version 3.11.5.
Each of the laboratory works is stored in a separate folder of the form `lab<number_of_lab>`
The solution is in the form of a program like `lab<number_of_lab>.py`

A solution in the form of a flowchart:
* In png format of the form `diagram_lab<number_of_lab>.png`
* In json format of the form `diagram_lab<number_of_lab>.json`
> Website for creating flowcharts: https://programforyou.ru/block-diagram-redactor you can import a json file with a flowchart into it.

Verification:
* Using excel tables of the form `Check_lab<number_of_lab>.xlsx`
* Using third-party saved screenshot `Check_lab<number_of_lab>_<number_of_exr>.jpeg`
Report as a text file `Otchet_lab<number_of_lab>.docx`
---
### Lab tasks:
- [x] lab 1

  1. Arbitrary x,y,z are given. Calculate a,b if:
    * a = |5-2*e|/((1+x^2)*(y - tg(z)))
    * b = |y-4|+((y-x)^2)/6+((x-y)^2)/7
  2. Calculate the value of the function f(x) = a*(x^b+x)/3-x^(3/4), where a = 2, b = -1 are constants, x varies from 4 to 5.5 in increments of h= 0.15.
  3. Calculate the value of the function f(x) = sqrt(ln(cos(sqrt(x))))) , for x from 1 to 3 in increments of h = 0.1.
  4. A triangle is defined by the coordinates (x1, y1), (x2, y2), (x3, y3) of its vertices. Find the perimeter and area of the triangle.
  5. The speed of the first car is V1 km/h, the second is V2 km/h, the distance between them is S km. Determine the distance between them in T hours if the cars are moving away from each other. This distance is equal to the sum of the initial distance and the total distance traveled by cars; total distance = time · total speed.
Input data: enter any four numbers V1, V2, S, T (1<= V1, V2, S, T <=100).
Output data: output the distance between buses in T hours with an accuracy of 4 digits in the fractional part.
  6. Two non-zero numbers are given. Find the sum, difference, product and quotient of their squares.
Input data: enter two integers a and b (1<=a,b<=100).
Output data: output the sum, difference, product and quotient of their squares with an accuracy of 3 digits in the fractional part in different lines.
  7. Find the value of the function y = 3x6 – 6x2 – 7 for a given value x.
Input data: enter a single integer x (-10<=x<=10).
Output: Output the value of y.
  8. Find a solution to a system of linear equations of the form
A1·x + B1·y = C1,
A2·x + B2·y = C2,
given by its coefficients A1, B1, C1, A2, B2, C2, if it is known that this system has a unique solution. Use formulas
x = (C1·B2 – C2·B1)/D, y = (A1·C2 – A2·C1)/D,
where D = A1·B2 – A2·B1.
Input data: Enter any six numbers A1, B1, C1, A2, B2, C2 (-10<= A1, B1, C1, A2, B2, C2 <=10).
Output data: print the value of x in the first line, and y in the second line with an accuracy of 4 digits in the fractional part.
  9. Three entrepreneurs - Davydov, Petrov and Maximov invested money in the joint organization of the enterprise for the production of special country furniture. The first invested 60 thousand rubles, the second - 90 thousand rubles, and the third - 150 thousand rubles. They made a profit of 117 thousand rubles. How much money will each of the entrepreneurs receive from the profit, provided it is distributed in proportion to their contributions?

- [x] lab 2
  1. Implement just a one-time game. To start a round, you need to restart the script. Rock-paper-scissor.
  2. Implement the game followed by an invitation to repeat the game.
  3. Implement a tournament game. When starting the game, the user is presented with a message indicating the choice of game mode. If just a game is selected, then the mode from level 2 returns.
  If you select a tournament, you are prompted to enter the number of rounds. After this, the specified number of rounds is played and the result of the tournament is displayed. For example: “Congratulations, you won with a score of 2:1”
  4. It is necessary to fill out the matrix A[n*n] using one of the described algorithms. Then “mirror” it to the right, resulting in a matrix of size B[n*2n].
  The resulting matrix B is “mirrored” downwards, filling the matrix C [2n*2n].
