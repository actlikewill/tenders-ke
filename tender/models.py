from django.db import models
import os


class Tender(models.Model):
    title = models.CharField(max_length=4096, null=False, blank=False)
    description = models.TextField()
    open_date = models.DateField(null=False, blank=False)
    close_date = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.title


def file_location(instance, filename):
    if not instance.tender.pk:
        raise ValueError("Tender must be saved before file can be attached")
    pk = instance.tender.pk
    filename = os.path.basename(filename)
    folder = instance.SAVE_FOLDER
    return f"media/tender_attachments/{pk}/{folder}/{filename}"


class AttachmentAbstractModel(models.Model):
    filename = models.CharField(max_length=1024, null=False, blank=False)
    size = models.CharField(max_length=1024, null=False, blank=False)
    mimetype = models.CharField(max_length=1024, null=False, blank=False)
    file = models.FileField(upload_to=file_location, max_length=2048)
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE, null=False)

    class Meta:
        abstract = True


class TenderDocument(AttachmentAbstractModel):
    SAVE_FOLDER = "documents"


class TenderImage(AttachmentAbstractModel):
    SAVE_FOLDER = "images"


