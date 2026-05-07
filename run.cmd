@echo off
REM Збірка Docker-образу
docker build -t euler-method .

REM Запуск контейнера з ENV та портом
docker run --rm -p 5000:5000 -e STUDENT_NAME="Самсонов Віталій" -e GROUP="АІ-233" -e MODE="eco" euler-method

REM Відкриття результату
start result.png
