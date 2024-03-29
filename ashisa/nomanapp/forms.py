from django import forms

class appointmentform(forms.Form):
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
    
    disease_category = forms.ChoiceField(choices=DISEASE_CATEGORIES, label='Disease Category')
    name = forms.CharField(max_length=100, label='Name')
    email = forms.EmailField(label='Email')
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control appointment_date'}), label='Date')
    time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control appointment_time'}), label='Time')
    phone = forms.CharField(max_length=15, label='Phone')