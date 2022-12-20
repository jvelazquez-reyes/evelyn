from django.db import models
import string
import random

# Create your models here.
# def generate_unique_code():
#     length = 8

#     while True:
#         code = ''.join(random.choices(string.ascii_uppercase, k=length))
#         if radioactiveSourcePackageReception.objects.filter(code=code).count() == 0:
#             break

#     return code

class radioactiveSourcePackageReception(models.Model):
    #code = models.CharField(max_length=10, default=generate_unique_code, unique=True)
    # Appendix B: NOM-040-NUCL-2016
    # External inspection of the package
    remarks = models.CharField(max_length=120)
    remarks_description = models.TextField()
    # Package identification
    supplier = models.CharField(max_length=120)
    receptionDateTime = models.DateTimeField()
    radionuclide = models.CharField(max_length=20)
    halfLife = models.DurationField() # Will need to handle time conversion
    requestedActivity = models.DecimalField(max_digits=8, decimal_places=2)
    receivedActivity = models.DecimalField(max_digits=8, decimal_places=2)
    # Radiological examination of the package
    radiationLevel_1m = models.DecimalField(max_digits=8, decimal_places=2) # Will need to handle activity units
    radiationLevel_0m = models.DecimalField(max_digits=8, decimal_places=2)
    measurementEquipment = models.CharField(max_length=50)
    brandModel = models.CharField(max_length=120)
    serialNumberEquipment = models.CharField(max_length=50)
    serialNumberDetector = models.CharField(max_length=50)
    detectorCalibrationDate = models.DateTimeField()
    calibrationFactor = models.CharField(max_length=50)
    # Surface contamination check (when there is suspicion of contamination)
    # Would be great if these fields pop up when requested (perhaps with a button)
    zoneLocation = models.TextField()
    rubbedSurface = models.TextField()
    smearReading = models.DecimalField(max_digits=8, decimal_places=2) # Will need to handle activitiy units
    equipmentUsed = models.CharField(max_length=50)
    brandModel_smearReading = models.CharField(max_length=120)
    serialNumberEquipment_smearReading = models.CharField(max_length=50)
    serialNumberDetector_smearReading = models.CharField(max_length=50)
    packageAcceptanceReception = models.CharField(max_length=20)
    reasonsAcceptanceReception = models.TextField()
    nameMedPhys = models.CharField(max_length=50)











