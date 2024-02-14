from django.db import models


# Create your models here.

class UserDetails(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    phone_number = models.CharField(max_length=15, blank=True, null=True)  # You might want to validate this further
    telephone_number = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    cnic = models.CharField(max_length=50, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'CSRP'


class RequistionForm(models.Model):
    DEPARTMENT_CHOICES = [
        ('CED', 'Department of Civil Engineering'),
        ('END', 'Department of Environmental Engineering'),
        ('ARD', 'Department of Architecture & Planning'),
        ('PED', 'Department of Petroleum Engineering'),
        ('UED', 'Department of Urban & Infrastructure Engineering'),
        ('EQD', 'Department of Earthquake Engineering'),
        ('EED', 'Department of Electrical Engineering'),
        ('CIS', 'Department of Computer & Information Systems Engineering'),
        ('ELD', 'Department of Electronic Engineering'),
        ('MED', 'Department of Mechanical Engineering'),
        ('TXD', 'Department of Textile Engineering'),
        ('IMD', 'Department of Industrial & Manufacturing Engineering'),
        ('ATD', 'Department of Automotive & Marine Engineering'),
        ('CSE', 'Department of Computer Science & Software Engineering'),
        ('DMT', 'Department of Mathematics'),
        ('DPH', 'Department of Physics'),
        ('DCY', 'Department of Chemistry'),
        ('HSD', 'Department of Humanities'),
        ('MMD', 'Department of Material Engineering'),
        ('MYD', 'Department of Metallurgical Engineering'),
        ('DEC', 'Department of Chemical Engineering'),
        ('PPD', 'Department of Polymer & Petrochemical Engineering'),
        ('BMD', 'Department of Biomedical Engineering'),
        ('FED', 'Department of Food Engineering'),
        ('EMD', 'Department of Economics & Management Sciences'),
        ('Dean(MME)', 'Dean(MME)'),
        ('Dean(ECE)', 'Dean(MME)'),
        ('Dean(ISH)', 'Dean(MME)'),
        ('Dean(CPE)', 'Dean(MME)'),
        ('Dean(AMS)', 'Dean(MME)'),
        ('VCS', 'Vice Chancellor’s Secretariat'),
        ('QMC/QEC', 'Quality Management Cell/Quality Enhancement Cell'),
        ('RO', 'Registrar Office'),
        ('DOF', 'Directorate of Finance'),
        ('AUD', 'Audit Department'),
        ('DW&S', 'Directorate of Works & Services'),
        ('DPD', 'Directorate of Planning & Development'),
        ('AKL', 'Engr. Abul Kalam Library'),
        ('EXD', 'Examinations Department'),
        ('MLD', 'Medical Department'),
        ('DSA', 'Department of Student Affairs'),
        ('DIL', 'Directorate of Industrial Liaison'),
        ('ITD', 'Information Technology Department'),
        ('NED Academy', 'NED Academy'),
        ('CCEE', 'Centre for Continuing Engineering Education'),
        ('CMPC', 'Centre for Multidisciplinary Postgraduate Courses'),
        ('UAFA', 'University Advancement & Financial Assistance"'),
        ('ORIC', 'DOffice of Research Innovation and Commercialization'),
        ('CINETIC', 'Center of Innovation, Entrepreneurship, Technology Incubation and Commercialization (CINETIC)'),
        ('PC', 'Procurement Cell'),
        ('NED-DICE-EIC', 'NED-DICE-Energy Innovation Centre'),
        ('NULL', 'Not Defined')
    ]
    
    REQUISTION_TYPE_CHOICES = [
        ('CR', 'Civil Requistions'),
        ('ER', 'Electrical Requistions'),
    ]

    department = models.CharField(
        max_length=2000,
        choices=DEPARTMENT_CHOICES,
        default='NULL',
        blank=True,
        null=True
    )

    requistion_type = models.CharField(
        max_length=300,
        choices=REQUISTION_TYPE_CHOICES,
        default='CR',
        blank=True,
        null=True
    )

    user_id = models.CharField(max_length=255)
    requistionsubject = models.CharField(max_length=300, blank=True, null=True)
    noofarticles = models.TextField(max_length=30, blank=True, null=True)
    requistiondescription = models.TextField(max_length=30, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    assignto = models.TextField(max_length=30, blank=True, null=True)
#    comment = models.TextField(max_length=300, blank=True, null=True)
    designation = models.TextField(max_length=300, blank=True, null=True)
    extensionnumber = models.CharField(max_length=15, blank=True, null=True)
    updatedon = models.DateField(auto_now_add=True)
    updatedtime = models.TimeField(auto_now_add=True, auto_now=False, blank=True)
    time = models.TimeField(auto_now_add=True, auto_now=False, blank=True)
    status = models.TextField(
        max_length=300,
        choices=REQUISTION_TYPE_CHOICES,
        default='OPEN',
        blank=True,
        null=True
    )

    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('IP', 'In Progress'),
        ('CLOSED', 'Closed')
    ]

    def __str__(self):
        return f"{self.requistionsubject} - {self.department}"
    
    class Meta:
        app_label = 'CSRP'


#class Comments(models.Model):
#    comment = models.TextField(max_length=300, blank=True, null=True)
#    owner = models.ForeignKey(RequistionForm, on_delete=models.CASCADE)
#    commentsubmiton = models.DateTimeField(auto_now_add=True)
#    commentposter = models.CharField(max_length=300, blank=True, null=True)

#    class Meta:
#        app_label = 'CSRP'

#    def __str__(self):
#        return f"{self.comment}"
    

class FeedbackForm(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    csrno = models.CharField(max_length=15, blank=True, null=True)
    phonenumber = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField(max_length=30, blank=True, null=True)

    class Meta:
        app_label = 'CSRP'

    def __str__(self):
        return f"{self.feedback}"

