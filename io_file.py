from PIL import Image
import torch
import torchvision.transforms as transforms
import matplotlib.pyplot as plt


# загрузка картинки нужного размера
def image_loader(image_name, imsize, device=torch.device('cpu')):

    loader = transforms.Compose([
        transforms.Resize(imsize),
        transforms.CenterCrop(imsize),
        transforms.ToTensor()])

    image = Image.open(image_name)
    image = loader(image).unsqueeze(0)
    return image.to(device, torch.float)


# отображение картинки
def imshow(tensor, title=None):

    plt.ion()
    unload = transforms.ToPILImage()
    image = tensor.cpu().clone()
    image = image.squeeze(0)
    image = unload(image)
    plt.imshow(image)
    if title is not None:
        plt.title(title)
    plt.pause(0.001)


# уменьшение размера картинок, если одна меньше другой
def crop(style_path, content_path, device=torch.device('cpu')):

    loader = transforms.ToTensor()
    style_img = loader(Image.open(style_path))
    content_img = loader(Image.open(content_path))
    styleH, styleW = style_img.shape[1], style_img.shape[2]
    contentH, contentW = content_img.shape[1], content_img.shape[2]
    H = min(styleH, contentH)
    W = min(styleW, contentW)
    loader2 = transforms.Compose([
        transforms.Resize((H, W)),
        transforms.CenterCrop((H, W)),
        transforms.ToTensor()])
    content_img = loader2(Image.open(content_path)).unsqueeze(0).to(device, torch.float)
    style_img = loader2(Image.open(style_path)).unsqueeze(0).to(device, torch.float)
    return style_img, content_img, (H, W)


# сохранение картинки
def save_image(img, size, path_name):
    img = img.view(3, size[0], size[-1])
    unload = transforms.ToPILImage()
    img = unload(img)
    img.save(path_name)
