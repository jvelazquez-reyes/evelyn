from rest_framework import serializers
from .models import radioactiveSourcePackageReception

class radSourceRecSerializer(serializers.ModelSerializer):
    class Meta:
        model = radioactiveSourcePackageReception
        fields = ('remarks', 'remarks_description', 'supplier', 'receptionDateTime',
    'radionuclide', 'halfLife', 'requestedActivity', 'receivedActivity', 'radiationLevel_1m', 'radiationLevel_0m',
    'measurementEquipment', 'brandModel', 'serialNumberEquipment', 'serialNumberDetector',
    'detectorCalibrationDate', 'calibrationFactor', 'zoneLocation', 'rubbedSurface', 'smearReading',
    'equipmentUsed', 'brandModel_smearReading', 'serialNumberEquipment_smearReading',
    'serialNumberDetector_smearReading', 'packageAcceptanceReception', 'reasonsAcceptanceReception',
    'nameMedPhys')