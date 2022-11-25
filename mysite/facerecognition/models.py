from django.db import models


class Face(models.Model):
    #이미지 이름
    name = models.CharField(max_length=50)
    #이미지를 저장 
    #mysite 안에 media폴더 생성 
    #media 폴더 안에 images 폴더 생성
    image = models.ImageField(upload_to = "images/", null=True, blank=True)

    def __str__(self):
        return self.name