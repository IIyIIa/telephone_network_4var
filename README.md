# telephone_network_4var
Разработать АИС для компании RingCell. Система должна регистрировать звонки с домашних и мобильных номеров и автоматически снимать с баланса израсходованную сумму. 
У компании есть различные абонентские планы. 
БД должна содержать данные о клиентах и зарегистрированных на них устройств, звонках и балансах.

Состав работы:

1) Idef0, Idef3, DFD диаграммы
2) Диаграммы UML (Use Cases Diagram + Class Diagram)
3) Схема БД
4) GitHub репозиторий с двумя ветками
5) Сквозные и модульные тесты
6) Реализация взаимодействия с БД через SQL запросы
7) Реализация взаимодействия с БД через ORM
8) Реализация шаблона проектирования

В проекте должна быть реализована авторизация, пароли хранятся в виде хеша.
В БД должно быть минимум 2 таблицы со связью один ко многим.
Необходимо реализовать добавление, удаление, изменение и поиск с фильтром. (каждая функция реализована как с SQL запросами, так и с ORM).

Для своего проекта выберите любой паттерн из списка:

1) Builder
2) Abstract Factory
3) Adapter
4) Chain of responsibility
5) Command
6) Observer
7) State
8) Strategy
