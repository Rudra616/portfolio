from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    message = models.TextField()
    send_time = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.name


from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    icon_class = models.CharField(max_length=100, help_text="Font Awesome class e.g., fab fa-html5")
    tags = models.CharField(max_length=200, help_text="Comma-separated tags like Python, Django")

    def __str__(self):
        return self.name


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return f"{self.project.name} Image"