# НоДиАБОИ Анализ данных NBA
Это проект по дисциплине "Наука о данных и анализ больших объемов информации", который позволяет проанализировать информацию по статистике матчей и статистике игроков в лиге NBA
# Предустановка
* Windows 10 (x64)
* ELK Stack (поставляется вместе с дистрибутивом)
* Подключение к интернету
* 5ГБ свободного места на диске
# Стек технологий
* Python 3.12
* ELK
# Руководство по эксплаутации
При запуске main.exe программа запустит ElasticSearch и Kibana. 
После установки соединения будет написано сообщение об этом и будут доступны на выбор несколько вариантов
* Скачивание данных в указаном диапазоне лет
  * После выбора данного варианта на вход будет ожидаться год начала диапазона и год конца диапазона
  * После ввода диапазона лет будет запущен скрипт скачивания с API данных по данному диапазону
* Загрузка всех скачаных данных в ElasticSearch с помощью Logstash
  * После выбора данного варианта запустится LogStash, который перенесет все скачанные данные в ElasticSearch
* Выход из программы
  * После выбора данного варианта программа завершит свою работу
  * Также будет выведено сообщение с просьбой завершить работу ElasticSearch, Kibana и Logstash

После выполнения каждого из пунктов будет выведено сообщение с выбором: продолжать работу программы или завершить ее