### ЗАДАНИЯ ПИСАЛИСЬ НА PYTHON3

На python2 могут быть некорректные результаты из-за того, что по дефолту в python2
оператор деления `/` делит нацело. Мои скрипты не подразумевают запуск в python2

Для корректной работы на python2.x необходимо добавить следующий import в каждый скрипт:

`from __future__ import division`
