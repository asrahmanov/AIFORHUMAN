# Проект: AI FOR HUMAN

## Описание

Данный проект представляет собой сервис уведомлений, который использует мощь OpenAI для создания и отправки интеллектуальных уведомлений. Проект использует Docker и Docker Compose для контейнеризации и легкого развертывания.

---

## Требования

Для запуска проекта необходимы следующие компоненты:

- Docker
- Docker Compose
- OpenAI API ключ

---

## Установка

### 1. Установка Docker

Docker — это платформа для разработки, доставки и запуска контейнеризированных приложений. Для установки Docker следуйте официальной инструкции:

- [Инструкция по установке Docker](https://docs.docker.com/get-docker/)

#### Для Linux:

```bash
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

Для MacOS:

Docker Desktop можно установить с официального сайта:

	•	Скачать Docker Desktop для Mac - https://www.docker.com/products/docker-desktop

Для Windows:

Также установите Docker Desktop:

	•	Скачать Docker Desktop для Windows - https://www.docker.com/products/docker-desktop

2. Установка Docker Compose

Docker Compose позволяет управлять многоконтейнерными приложениями. Для установки Docker Compose:

Для Linux:

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

Для MacOS и Windows:
Docker Compose уже включён в Docker Desktop, и его не нужно устанавливать отдельно.


Получение ключа API от OpenAI

Для того чтобы проект мог взаимодействовать с OpenAI, необходимо зарегистрироваться и получить API ключ:

	1.	Перейдите на сайт OpenAI. - https://openai.com/
	2.	Зарегистрируйтесь или войдите в систему.
	3.	Перейдите в раздел API и создайте новый ключ.
	4.	Скопируйте ключ и сохраните его.

Настройка переменных окружения

После получения ключа OpenAI, необходимо настроить файл .env для вашего проекта.

	1.	Создайте файл .env в корневой директории проекта, если он ещё не существует.
	2.	Добавьте в него следующие строки:

```
OPENAI_API_KEY=ваш_ключ_api_openai
```

Замените ваш_ключ_api_openai на реальный ключ, который вы получили на сайте OpenAI.

Запуск проекта

После того как Docker и Docker Compose установлены, и API ключ добавлен в файл .env, выполните следующие команды для запуска проекта:

Соберите контейнеры:
```bash
docker-compose build
```
Запустите проект:

```bash
docker-compose up
```



