from django.db import models


class SoinsSelect(models.Model):
    extensionsCils = models.BooleanField(default=False)
    lashLift = models.BooleanField(default=False)
    lashLiftTeinture = models.BooleanField(default=False)
    browLift = models.BooleanField(default=False)
    browLift3dFiller = models.BooleanField(default=False)
    browliftTeinture = models.BooleanField(default=False)
    browlifthenne = models.BooleanField(default=False)
    browlif3dTeinture = models.BooleanField(default=False)
    browlif3dhenne = models.BooleanField(default=False)
    hennaBrow = models.BooleanField(default=False)
    teinture = models.BooleanField(default=False)
    epilationSourcil = models.BooleanField(default=False)
    soin3d = models.BooleanField(default=False)
