from django.db import models


class Client(models.Model):

    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    telegram_nickname = models.CharField(max_length=50)

    def __str__(self):
        return 'Client {} {}'.format(self.first_name, self.second_name)


class Application(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.IntegerField()

    def __str__(self):
        return 'Application №{} from {}'.format(self.id, self.client)


class Employee(models.Model):

    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    # number = models.CharField(max_length=50)

    def __str__(self):
        return 'Employee {} {}(№{})'.format(self.first_name, self.second_name, self.id)
