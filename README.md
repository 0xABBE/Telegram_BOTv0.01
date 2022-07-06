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
  
  После добавления файла, запустить бота.
  
  ## Примеры работы 
  Примеры работы программы можно посмотреть на [Drive Google](https://drive.google.com/drive/folders/1Yzz3Se4_b5pn7ZC1vithoWEbI3z7RE8P?usp=sharing)
  
  ![](https://drive.google.com/file/d/1PhIjErnH6hWNVDAlU0H1MNU47XViuP3u/view?usp=sharing)
