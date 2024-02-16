from django.db import models

# Create your models here.
class Register(models.Model):
    Name =models.CharField(max_length=50)
    Mobile=models.CharField(max_length=20)
    Email=models.EmailField(max_length=30)
    Password=models.CharField(max_length=20)

class FillDetails(models.Model):
    Name = models.CharField(max_length=50)
    Photo= models.ImageField()
    Father_Name= models.CharField(max_length=50)
    Age=models.IntegerField()
    Dob=models.DateField()
    Address=models.CharField(max_length=100)
    Aadhar=models.BigIntegerField()
    Doj=models.DateField()
    Education=models.CharField(max_length=100)
    Profession=models.CharField(max_length=100)
    Office_Address=models.CharField(max_length=100)
    Phone_no = models.BigIntegerField()
    Monthly_Rent=models.IntegerField()
    Deposit=models.IntegerField()
    Maintain_Charge=models.IntegerField()


class Floor(models.Model):
    FLOOR_CHOICES = [
        ('A', 'Floor A'),
        ('B', 'Floor B'),
        ('C', 'Floor C'),
    ]

    floor_type = models.CharField(max_length=1, choices=FLOOR_CHOICES)

    def __str__(self):
        return self.floor_type



class Room(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    room_number = models.IntegerField(choices=[(i, i) for i in range(1, 13)])

    def __str__(self):
        return f"{self.floor} - Room {self.room_number}"

class Complaints(models.Model):
    user_name = models.ForeignKey(FillDetails, on_delete=models.CASCADE)
    user_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    complaint_date = models.DateField()

    def __str__(self):
        return f"{self.user_room} - {self.user_name}  - {self.complaint_date}"