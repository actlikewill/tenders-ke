from django.contrib import admin
from tender.models import  Tender, TenderImage, TenderDocument


def model_inline(_model, _extra):
    class AdminInline(admin.StackedInline):
        model = _model
        extra = _extra

    return AdminInline


@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    inlines = [model_inline(TenderImage, 1), model_inline(TenderDocument, 1)]
