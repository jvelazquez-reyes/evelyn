from django.contrib import admin
from .models import radioactiveSourcePackageReception

class MedPhysAdmin(admin.ModelAdmin):
    list_display = ('remarks', 'remarks_description', 'supplier', 'receptionDateTime',
    'radionuclide', 'halfLife', 'requestedActivity', 'receivedActivity', 'radiationLevel_1m', 'radiationLevel_0m',
    'measurementEquipment', 'brandModel', 'serialNumberEquipment', 'serialNumberDetector',
    'detectorCalibrationDate', 'calibrationFactor', 'zoneLocation', 'rubbedSurface', 'smearReading',
    'equipmentUsed', 'brandModel_smearReading', 'serialNumberEquipment_smearReading',
    'serialNumberDetector_smearReading', 'packageAcceptanceReception', 'reasonsAcceptanceReception',
    'nameMedPhys')

#Register your models here.
admin.site.register(radioactiveSourcePackageReception, MedPhysAdmin)