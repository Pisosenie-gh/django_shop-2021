from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
User = get_user_model()





class ImageCategory(models.Model):

    name = models.CharField("Название категории картинок", max_length=250, default=None)
    description = models.CharField("Описание категории картинок", max_length=250, default=None)

    def __str__(self):
        return f"Категория картинок {self.name}"

    class Meta:
        verbose_name = 'Категория картинок'
        verbose_name_plural = 'Категории картинок'


class ImageChapter(models.Model):

    name = models.CharField("Название раздела картинок", max_length=250, default=None)
    description = models.TextField("Описание раздела картинок",default=None)
    category = models.ForeignKey(ImageCategory, on_delete=models.CASCADE, verbose_name='Категория', null=False)

    def __str__(self):
        return f"Раздел картинок {self.name}"

    class Meta:
        verbose_name = 'Раздел картинок'
        verbose_name_plural = 'Разделы картинок'


class Images(models.Model):

    name = models.CharField("Название картинки", max_length=250, default=None)
    description = models.TextField("Описание картинки", default=None)
    image = models.ImageField(upload_to='images/', verbose_name='Картинка', null=False, default=None)
    category = models.ForeignKey(ImageChapter, on_delete=models.CASCADE, verbose_name='Раздел картинки', null=False)

    def __str__(self):
        return f"Картинка {self.name}"

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'


class Lapbook(models.Model):

    name = models.CharField("Название Лэпбука", max_length=250, default=None)
    description = models.TextField("Описание Лэпбука",  default=None, null=True)

    def __str__(self):
        return f"Лэпбук {self.name}"

    class Meta:
        verbose_name = 'Лэпбук'
        verbose_name_plural = 'Лэпбуки'


class LapbookImage(models.Model):

    task = models.ForeignKey(Lapbook, on_delete=models.CASCADE, default=None)
    image = models.FileField(blank=True, upload_to='lapbook/', verbose_name='Картинка')

    def __str__(self):
        return f"Фото для лэпбука {self.task.name}"

    class Meta:
        verbose_name = 'Лэпбук фото'
        verbose_name_plural = 'Лэпбуки фото'


class AbstractCategory(models.Model):

    name = models.CharField("Название темы конспектов", max_length=250, default=None)
    description = models.CharField("Описание темы конспектов", max_length=250, default=None)

    def __str__(self):
        return f"Категория конспекта {self.name}"

    class Meta:
        verbose_name = 'Категория конспекта'
        verbose_name_plural = 'Категории конспектов'


class Abstract(models.Model):

    name = models.CharField("Название Конспекта", max_length=250, default=None)

    description = models.TextField("Описание Конспекта", default=None, null=True)
    text = models.TextField("Текст Конспекта", default=None,  null=True)
    theme = models.ForeignKey(AbstractCategory, on_delete=models.CASCADE, verbose_name='Тема конспекта', null=True, default=None)
    user_fio = models.CharField("ФИО автора", max_length=250, default=None, null=True)
    user_image = models.CharField("Ссылка на аватар автора", max_length=250, default=None, null=True)
    date = models.DateTimeField("Дата публикации", auto_now=True)

    def __str__(self):
        return f"Конспект {self.name}"

    class Meta:
        verbose_name = 'Конспект'
        verbose_name_plural = 'Конспекты'


class AbstractImage(models.Model):

    task = models.ForeignKey(Abstract, on_delete=models.CASCADE, default=None)
    image = models.FileField(blank=True, upload_to='abstract/', verbose_name='Картинка')

    def __str__(self):
        return f"Фото для Конспекта {self.task.name}"

    class Meta:
        verbose_name = 'Конспект фото'
        verbose_name_plural = 'Конспекты фото'


class HolidayCategory(models.Model):

    name = models.CharField("Название темы праздника", max_length=250, default=None)
    description = models.CharField("Описание темы праздника", max_length=250, default=None)

    def __str__(self):
        return f"Категория праздника {self.name}"

    class Meta:
        verbose_name = 'Категория праздника'
        verbose_name_plural = 'Категории праздников'


class Holiday(models.Model):

    name = models.CharField("Название праздника", max_length=250, default=None)
    description = models.TextField("Описание праздника", default=None, null=True)
    text = models.TextField("Текст праздника", default=None,  null=True)
    theme = models.ForeignKey(HolidayCategory, on_delete=models.CASCADE, verbose_name='Тема праздника', null=True, default=None)
    user_fio = models.CharField("ФИО автора", max_length=250, default=None, null=True)
    user_image = models.CharField("Ссылка на аватар автора", max_length=250, default=None, null=True)
    date = models.DateTimeField("Дата публикации", auto_now=True)

    def __str__(self):
        return f"Праздник {self.name}"

    class Meta:
        verbose_name = 'Праздник'
        verbose_name_plural = 'Праздники'


class HolidayImage(models.Model):

    task = models.ForeignKey(Holiday, on_delete=models.CASCADE, default=None)
    image = models.FileField(blank=True, upload_to='holiday/', verbose_name='Картинка')

    def __str__(self):
        return f"Фото для праздника {self.task.name}"

    class Meta:
        verbose_name = 'Праздник фото'
        verbose_name_plural = 'праздники фото'


class DevelopmentCategory(models.Model):

    name = models.CharField("Название темы разработки", max_length=250, default=None)
    description = models.CharField("Описание темы разработки", max_length=250, default=None)

    def __str__(self):
        return f"Категория разработки {self.name}"

    class Meta:
        verbose_name = 'Категория разработки'
        verbose_name_plural = 'Категории разработки'


class Development(models.Model):

    name = models.CharField("Название разработки", max_length=250, default=None)
    description = models.TextField("Описание разработки", default=None, null=True)
    text = models.TextField("Текст разработки", default=None,  null=True)
    theme = models.ForeignKey(DevelopmentCategory, on_delete=models.CASCADE, verbose_name='Тема разработки', null=True, default=None)
    user_fio = models.CharField("ФИО автора", max_length=250, default=None, null=True)
    user_image = models.CharField("Ссылка на аватар автора", max_length=250, default=None, null=True)
    date = models.DateTimeField("Дата публикации", auto_now=True)

    def __str__(self):
        return f"Разработка {self.name}"

    class Meta:
        verbose_name = 'Разработка'
        verbose_name_plural = 'Разработки'


class DevelopmentImage(models.Model):

    task = models.ForeignKey(Development, on_delete=models.CASCADE, default=None)
    image = models.FileField(blank=True, upload_to='development/', verbose_name='Картинка')

    def __str__(self):
        return f"Фото для Разработки {self.task.name}"

    class Meta:
        verbose_name = 'Разработка фото'
        verbose_name_plural = 'Разработки фото'


class RegistrationCategory(models.Model):

    name = models.CharField("Название темы оформления", max_length=250, default=None)
    description = models.CharField("Описание темы оформления", max_length=250, default=None)

    def __str__(self):
        return f"Категория оформления {self.name}"

    class Meta:
        verbose_name = 'Категория оформления'
        verbose_name_plural = 'Категории оформления'


class Registration(models.Model):

    name = models.CharField("Название оформления", max_length=250, default=None)
    description = models.TextField("Описание оформления", default=None, null=True)
    text = models.TextField("Текст оформления", default=None,  null=True)
    theme = models.ForeignKey(RegistrationCategory, on_delete=models.CASCADE, verbose_name='Тема оформления', null=True, default=None)
    user_fio = models.CharField("ФИО автора", max_length=250, default=None, null=True)
    user_image = models.CharField("Ссылка на аватар автора", max_length=250, default=None, null=True)
    date = models.DateTimeField("Дата публикации", auto_now=True)

    def __str__(self):
        return f"Оформление {self.name}"

    class Meta:
        verbose_name = 'Оформление'
        verbose_name_plural = 'Оформления'


class RegistrationImage(models.Model):

    task = models.ForeignKey(Development, on_delete=models.CASCADE, default=None)
    image = models.FileField(blank=True, upload_to='registration/', verbose_name='Картинка')

    def __str__(self):
        return f"Фото для Оформления {self.task.name}"

    class Meta:
        verbose_name = 'Оформление фото'
        verbose_name_plural = 'Оформление фото'


class CraftsCategory(models.Model):

    name = models.CharField("Название темы поделок", max_length=250, default=None)
    description = models.CharField("Описание темы поделок", max_length=250, default=None)

    def __str__(self):
        return f"Категория поделок {self.name}"

    class Meta:
        verbose_name = 'Категория поделки'
        verbose_name_plural = 'Категории поделок'


class Crafts(models.Model):

    name = models.CharField("Название поделок", max_length=250, default=None)
    description = models.TextField("Описание поделок", default=None, null=True)
    text = models.TextField("Текст поделок", default=None,  null=True)
    theme = models.ForeignKey(CraftsCategory, on_delete=models.CASCADE, verbose_name='Тема поделок', null=True, default=None)
    user_fio = models.CharField("ФИО автора", max_length=250, default=None, null=True)
    user_image = models.CharField("Ссылка на аватар автора", max_length=250, default=None, null=True)
    date = models.DateTimeField("Дата публикации", auto_now=True)

    def __str__(self):
        return f"Поделка {self.name}"

    class Meta:
        verbose_name = 'Поделка'
        verbose_name_plural = 'Поделки'


class CraftsImage(models.Model):

    task = models.ForeignKey(Development, on_delete=models.CASCADE, default=None)
    image = models.FileField(blank=True, upload_to='crafts/', verbose_name='Картинка')

    def __str__(self):
        return f"Фото для Поделки {self.task.name}"

    class Meta:
        verbose_name = 'Поделка фото'
        verbose_name_plural = 'Поделки фото'


class GamesCategory(models.Model):

    name = models.CharField("Название темы игр", max_length=250, default=None)
    description = models.CharField("Описание темы игр", max_length=250, default=None)

    def __str__(self):
        return f"Категория игр {self.name}"

    class Meta:
        verbose_name = 'Категория игры'
        verbose_name_plural = 'Категории игр'


class Games(models.Model):

    name = models.CharField("Название игры", max_length=250, default=None)
    description = models.TextField("Описание игры", default=None, null=True)
    text = models.TextField("Текст игры", default=None,  null=True)
    theme = models.ForeignKey(GamesCategory, on_delete=models.CASCADE, verbose_name='Тема игры', null=True, default=None)
    user_fio = models.CharField("ФИО автора", max_length=250, default=None, null=True)
    user_image = models.CharField("Ссылка на аватар автора", max_length=250, default=None, null=True)
    date = models.DateTimeField("Дата публикации", auto_now=True)

    def __str__(self):
        return f"Игра {self.name}"

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'


class GamesImage(models.Model):

    task = models.ForeignKey(Development, on_delete=models.CASCADE, default=None)
    image = models.FileField(blank=True, upload_to='games/', verbose_name='Картинка')

    def __str__(self):
        return f"Фото для Игры {self.task.name}"

    class Meta:
        verbose_name = 'Игра фото'
        verbose_name_plural = 'Игры фото'


class Contests(models.Model):

    name = models.CharField("Название конкурса", max_length=250, default=None)
    description = models.TextField("Описание конкурса", default=None, null=True)
    text = models.TextField("Текст конкурса", default=None,  null=True)
    date = models.DateTimeField("Дата публикации", auto_now=True)
    user_fio = models.CharField("ФИО автора", max_length=250, default=None, null=True)
    user_image = models.CharField("Ссылка на аватар автора", max_length=250, default=None, null=True)
    likes = models.ManyToManyField(User, related_name='likes')

    def number_of_likes(self):
        return self.likes.count()



    def __str__(self):
        return f"Конкурс {self.name}"

    class Meta:
        verbose_name = 'Конкурс'
        verbose_name_plural = 'Конкурсы'


class ContestsImage(models.Model):

    task = models.ForeignKey(Contests, on_delete=models.CASCADE, default=None)
    image = models.FileField(blank=True, upload_to='contests/', verbose_name='Картинка')

    def __str__(self):
        return f"Фото для Конкурса {self.task.name}"

    class Meta:
        verbose_name = 'Конкурс фото'
        verbose_name_plural = 'Конкурсы фото'


class Reviews_Contests(models.Model):

    user_name = models.CharField("USER NAME", blank=True, max_length=5000)
    name = models.CharField("ФИО", max_length=500, null=False)
    user_photo = models.CharField("Ссылка на фото ", max_length=500, null=False)
    text = models.TextField("Комментарий", null=False)
    task = models.ForeignKey(Contests, verbose_name="Конкурс", on_delete=models.CASCADE)

    def __str__(self):
        return f"Комментарий для Конкурса {self.task.name}"

    class Meta:
        verbose_name = 'Конкурс комментарий'
        verbose_name_plural = 'Конкурсы комментарии'


class Reviews_Games(models.Model):

    user_name = models.CharField("USER NAME", blank=True, max_length=5000)
    name = models.CharField("ФИО", max_length=500, null=False)
    user_photo = models.CharField("Ссылка на фото ", max_length=500, null=False)
    text = models.TextField("Комментарий", null=False)
    task = models.ForeignKey(Games, verbose_name="Игра", on_delete=models.CASCADE)

    def __str__(self):
        return f"Комментарий для игры {self.task.name}"

    class Meta:
        verbose_name = 'Игры комментарий'
        verbose_name_plural = 'Игры комментарии'


class Reviews_Crafts(models.Model):

    user_name = models.CharField("USER NAME", blank=True, max_length=5000)
    name = models.CharField("ФИО", max_length=500, null=False)
    user_photo = models.CharField("Ссылка на фото ", max_length=500, null=False)
    text = models.TextField("Комментарий", null=False)
    task = models.ForeignKey(Crafts, verbose_name="Поделка", on_delete=models.CASCADE)

    def __str__(self):
        return f"Комментарий для Поделка {self.task.name}"

    class Meta:
        verbose_name = 'Комментарий Поделка'
        verbose_name_plural = 'Комментарий Поделка'


class Reviews_Registration(models.Model):

    user_name = models.CharField("USER NAME", blank=True, max_length=5000)
    name = models.CharField("ФИО", max_length=500, null=False)
    user_photo = models.CharField("Ссылка на фото ", max_length=500, null=False)
    text = models.TextField("Комментарий", null=False)
    task = models.ForeignKey(Registration, verbose_name="Оформление", on_delete=models.CASCADE)

    def __str__(self):
        return f"Комментарий для оформления {self.task.name}"

    class Meta:
        verbose_name = 'Оформление комментарий'
        verbose_name_plural = 'Оформление комментарий'



class Reviews_Development(models.Model):

    user_name = models.CharField("USER NAME", blank=True, max_length=5000)
    name = models.CharField("ФИО", max_length=500, null=False)
    user_photo = models.CharField("Ссылка на фото ", max_length=500, null=False)
    text = models.TextField("Комментарий", null=False)
    task = models.ForeignKey(Development, verbose_name="Разработка", on_delete=models.CASCADE)

    def __str__(self):
        return f"Комментарий для Разработки {self.task.name}"

    class Meta:
        verbose_name = 'Разработки комментарий'
        verbose_name_plural = 'Разработки комментарий'


class Reviews_Holiday(models.Model):

    user_name = models.CharField("USER NAME", blank=True, max_length=5000)
    name = models.CharField("ФИО", max_length=500, null=False)
    user_photo = models.CharField("Ссылка на фото ", max_length=500, null=False)
    text = models.TextField("Комментарий", null=False)
    task = models.ForeignKey(Holiday, verbose_name="Праздник", on_delete=models.CASCADE)

    def __str__(self):
        return f"Комментарий для Праздника {self.task.name}"

    class Meta:
        verbose_name = 'Праздник комментарий'
        verbose_name_plural = 'Праздник комментарий'


class Reviews_Abstract(models.Model):

    user_name = models.CharField("USER NAME", blank=True, max_length=5000)
    name = models.CharField("ФИО", max_length=500, null=False)
    user_photo = models.CharField("Ссылка на фото ", max_length=500, null=False)
    text = models.TextField("Комментарий", null=False)
    task = models.ForeignKey(Abstract, verbose_name="Конспект", on_delete=models.CASCADE)

    def __str__(self):
        return f"Комментарий для Конспекта {self.task.name}"

    class Meta:
        verbose_name = 'Конспект комментарий'
        verbose_name_plural = 'Конспект комментарий'


class Reviews_Lapbook(models.Model):

    user_name = models.CharField("USER NAME", blank=True, max_length=5000)
    name = models.CharField("ФИО", max_length=500, null=False)
    user_photo = models.CharField("Ссылка на фото ", max_length=500, null=False)
    text = models.TextField("Комментарий", null=False)
    task = models.ForeignKey(Lapbook, verbose_name="Лэпбук", on_delete=models.CASCADE)

    def __str__(self):
        return f"Комментарий для Лэпбука {self.task.name}"

    class Meta:
        verbose_name = 'Лэпбук комментарий'
        verbose_name_plural = 'Лэпбук комментарий'


class Reviews_Images(models.Model):

    user_name = models.CharField("USER NAME", blank=True, max_length=5000)
    name = models.CharField("ФИО", max_length=500, null=False)
    user_photo = models.CharField("Ссылка на фото ", max_length=500, null=False)
    text = models.TextField("Комментарий", null=False)
    task = models.ForeignKey(Images, verbose_name="Картинка", on_delete=models.CASCADE)

    def __str__(self):
        return f"Комментарий для Картинки {self.task.name}"

    class Meta:
        verbose_name = 'Картинка комментарий'
        verbose_name_plural = 'Картинка комментарий'

