from django.db import models

# Create your models here.
class Appointment(models.Model):
    DISEASE_CATEGORIES = [
        ('Wound Care', 'Wound Care'),
        ('Colo-Rectal Care', 'Colo-Rectal Care'),
        ('Uro Care', 'Uro Care'),
        ('Orthopedic', 'Orthopedic'),
        ('Vericose Vein', 'Vericose Vein'),
        ('Abscess and Cyst', 'Abscess and Cyst'),
        ('Corn and Warts', 'Corn and Warts'),
        ('Planter Fascitis', 'Planter Fascitis'),
        ('Hydrocele', 'Hydrocele'),
        ('Musculoskeletal Disorder', 'Musculoskeletal Disorder'),
        ('Diabetes', 'Diabetes'),
        ('Hypertension', 'Hypertension'),
        ('Obesity', 'Obesity'),
        ('Paralysis', 'Paralysis'),
        ('Artheritis', 'Artheritis'),
        ('Other', 'Other'),
    ]
    
    disease_category = models.CharField(max_length=100, choices=DISEASE_CATEGORIES)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    phone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name