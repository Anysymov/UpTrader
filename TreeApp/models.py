from django.db import models

# Список меню
class Menu(models.Model):

    menu_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Name: {self.menu_name}, ID: {self.id}"

# Список объектов меню (пунктов/линий)
# Связан со списком меню
class MenuObject(models.Model):

    line_name = models.CharField(max_length=100)
    menu_name = models.ForeignKey(Menu, on_delete=models.CASCADE)

    line_parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    line_url = models.URLField(blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['line_name', 'menu_name'], name="unique_name_and_menu")
        ]
    
    def __str__(self):
        return f"Name: {self.line_name}, ID: {self.id}"
