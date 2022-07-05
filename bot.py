import os
import logging
import shutil
import VGG19_Style_Transfer.VGG19Style_Transfer as Model
import subprocess
from aiogram import Bot, Dispatcher, executor, types
from keyboards import client_kb, accept_kb, gan_kb
from io_file import *
import configparser
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

config = configparser.ConfigParser()
config.read("config.ini")


bot = Bot(config["Telegram"]["token"])

dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


async def on_startup(_):
    print("Начало работы бота.")


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет! Меня зовут Стайл Трансфер бот!\n" +
                                                 "Я могу взять изображения и применить к ним различные стили.")
    await bot.send_message(message.from_user.id, "Я могу использовать модель, основанную на применении "
                                                 "сверточной сети VGG19. Она более медленная, но позволяет "
                                                 "переносить почти любой стиль.\n"
                                                 "Так же могу применить стиль ранцузского художника Моне, с помощью"
                                                 "Gan модели.")
    await bot.send_message(message.from_user.id, "Для начала, отправьте 2 картинки с подписями style и content, если"
                                                 "хотите обучить VGG19, или одну с подписью content для Gan.")
    await bot.send_message(message.from_user.id, "ВАЖНО! Для первого варианта все картинки должны быть равных размеров,"
                                                 " иначе обе картинки будут уменьшины до самой маленькой "
                                                 "по ширине из двух, и самой маленькой по высоте.")


@dp.message_handler(commands="VGG19")
async def cmd_style_transfer_vgg19(message: types.Message):
    # путь до папки с картинками пользователя
    path = 'tmp/'+str(message.from_user.id)+'/'

    # проверка наличия нужных файлов
    if os.path.isfile(path + 'content.jpg') and os.path.isfile(path + 'style.jpg'):
        await bot.send_message(message.from_user.id, "Хороший выбор. Приступаю к обучению. Это займет некоторое время.")

        # уменьшение размеров картинок, если они не равны по размерам
        style_img, content_img, size = crop(style_path=path + "style.jpg",
                                            content_path=path + "content.jpg", device=device)
        input_img = content_img.clone()
        # обучение модели
        st_tr_model = Model.StyleTransferModel()
        img = st_tr_model.run_style_transfer(content_img.to(), style_img, input_img)
        # созранение и отправка результирующей какртинки
        save_image(img.to('cpu'), size, path+'output.jpg')
        await bot.send_photo(message.from_user.id, types.InputFile(path+'output.jpg'))
        await bot.send_message(message.from_user.id, "Хорошая картинка, не правда ли?")
        # удаление исходных картинок и дирректории
        shutil.rmtree(path)
        await bot.send_message(message.from_user.id, "Продолжить работу?", reply_markup=accept_kb)
    else:
        await bot.send_message(message.from_user.id, "Извините, но не все картинки были отправлены. "
                                                     "Для начал отправьте картинки c подписью style и content.")


@dp.message_handler(commands="Gan")
async def cmd_style_transfer_gan(message: types.Message):
    # путь до папки с картинками пользователя
    path = 'tmp/'+str(message.from_user.id)
    # проверка наличия необходимых файлов
    if os.path.isfile(path + '/content.jpg'):
        await bot.send_message(message.from_user.id,
                               "Хороший выбор. Приступаю к обучению. Это займет некоторое время. ")
        # консольная команда для запуска модели
        bashcommand = "python CycleGan/test.py --dataroot "+path\
                      + " --name style_monet_pretrained --model test --no_dropout"

        pr = subprocess.Popen(bashcommand)
        pr.wait()
        # отправка картинки
        await bot.send_photo(message.from_user.id,
                             types.InputFile("results/style_monet_pretrained/test_latest/images/content_fake.png"))
        await bot.send_message(message.from_user.id, "Хорошая картинка, не правда ли?")
        shutil.rmtree(path+'/')
        shutil.rmtree('results/')
        await bot.send_message(message.from_user.id, "Продолжить работу?", reply_markup=accept_kb)
    else:
        await bot.send_message(message.from_user.id, "Извините, но не все картинки были отправлены. "
                                                     "Для начал отправьте картинку content.")


@dp.message_handler(commands="accept")
async def cmd_accept(message: types.Message):
    await bot.send_message(message.from_user.id, "Если захотите продолжить, "
                                                 "то просто отправьте нужные картинки мне.")


@dp.message_handler(content_types=["photo"])
async def cmd_get_photo(message: types.Message):
    # путь до папки скартинками пользователя
    path = 'tmp/' + str(message.from_user.id) + '/'
    # если папки не существует, создать новую
    if not os.path.isdir(path):
        os.mkdir(path)
    # загрузка нужного типа файла
    if message.caption.lower() == "style":
        await message.photo[-1].download(path+"style.jpg")

        if os.path.isfile(path+'content.jpg') and os.path.isfile(path+'style.jpg'):
            await bot.send_message(message.from_user.id, "Можно приступить к выбору модели. Выберите одну.",
                                   reply_markup=client_kb)

    elif message.caption.lower() == "content":
        await message.photo[-1].download(path+"content.jpg")

        if os.path.isfile(path+'content.jpg') and os.path.isfile(path+'style.jpg'):
            await bot.send_message(message.from_user.id, "Можно приступить к выбору модели. Выберите одну.",
                                   reply_markup=client_kb)
        elif os.path.isfile(path+'content.jpg'):
            await bot.send_message(message.from_user.id, "Вы можете выбрать Gan или отправить еще одну картинку.",
                                   reply_markup=gan_kb)

    else:
        await bot.send_message(message.from_user.id, "Извините, но тип картинки не известен."
                                                     "Пожалуйста, отправьте картинку с подписью content или style")


@dp.message_handler(commands="Add_Style_Image")
async def cmd_add_image(message: types.Message):
    await bot.send_message(message.from_user.id, "Пожалуйста, отправьте картинку с подписью style")


@dp.message_handler(commands="help")
async def cmd_help(message: types.Message):
    await bot.send_message(message.from_user.id, "Список используемых команд")
    await bot.send_message(message.from_user.id, "/start - начать общение;\n"
                                                 "/help - список команд;\n"
                                                 "/VGG19 - начать обучение VGG19;\n"
                                                 "/Gan - начать обучение Gan;\n"
                                                 "/accept - продолжить работу с ботом")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
