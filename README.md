# Telegram_BOTv0.01
## О проекте
  Данный репозbторий содержит программу по запуску телеграм бота, применяющего модели стайл трансфера.
  
  В нем используются две основные модели. Первая - основана на использовании сети VGG19 и является медленной версией стайлтрансфера, однако позволяет переносить с любой картинки стиля, стиль на другую.
  
  Вторая модель - основана на использовании Генеративных состязательных моделей, построенная по архитектуре CycleGan. Код для Cyclegan был взят из репозитория [junyanz/pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) .

## Установка

  Вариант 1: скачать репозиторий с [DockerHub](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) и развернуть контейнер. Однако, в таком случае применение Cyclegan будет невозможны.
  
  Вариант 2: установть зависимости из файла requirements.txt, потом создать конфигурационный файл config.ini в корне программы. Шаблон файла:
  
  [Telegram] \
  token=123456789abcdefg
  
  После добавления файла, запустить bot.py.
  
  ## Примеры работы 
  Примеры работы программы можно посмотреть на [Drive Google](https://drive.google.com/drive/folders/1Yzz3Se4_b5pn7ZC1vithoWEbI3z7RE8P?usp=sharing)
  
  ![Добавление контента](https://github.com/0xABBE/Telegram_BOTv0.01/tree/main/images_readme/img1.png)
  
   ![Добавление стиля](https://github.com/0xABBE/Telegram_BOTv0.01/tree/main/images_readme/img2.png)
   
   ![Добавление VGG19 и получение итогового изображения](https://github.com/0xABBE/Telegram_BOTv0.01/tree/main/images_readme/img2.png)
   
  ## Cтруктура рабочей директории

1)CycleGan - содержит все файлы для работы с CycleGan и Pix2Pix, взятые с [junyanz/pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix). \
2)VGG19_Style_Transfer - содержит файлы модели переноса стиля на основе предобученной на Imagnet модели VGG19. \
3)keyboards - содержит файлы для маркапов бота. \
4)tmp - содержит временные файлы для каждого из пользователей (в своей папке), которые после завершения работы модели удаляются. \
5)bot.py - точка входа в программу и набор хендлеров бота. \
6)io_file - файл с функциями для загрузки, кадрирования и выгрузки картинок. \
7)requirements - список всех используемых зависимостей.
