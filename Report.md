# Практическое задание №1. База Linux
В данной практической работе необходимо было развернуть 3 виртуальные машины, сконфигурировать и настроить их определенным образом

Работа выполнена с помощью Oracle VM VirtualBox и Ubuntu Server 20.04.4

# 1. Ubuntu A

Сперва был создан пользователь и сконфигурирован hostname:

![info](./Assets/Images/ConfA.png)

Далее был сконфигурирован интерфейс с определенным ip:

![info](./Assets/Images/SetUpA.png)

Был развернут http сервер на порту 5000:

![info](./Assets/Images/A5000.png)

# 2. Ubuntu B

Созданый пользователь и hostname для второй машины:

![info](./Assets/Images/ConfB.png)

Далее сконфигурировано 2 виртуальных интерфейса с разными ip:

![info](./Assets/Images/SetUpB.png)

Конфигурация запросов в Ubuntu B через порт 5000:

![info](./Assets/Images/B5000.png)

Разрешение на переброс пакетов:

![info](./Assets/Images/SysctlB.png)


# 3. Ubuntu C

Как и для двух предыдущих машин был создан пользователь и сконфигурирован hostname:

![info](./Assets/Images/ConfC.png)

Далее был сконфигурирован интерфейс с определенным ip:

![info](./Assets/Images/SetUpC.png)

