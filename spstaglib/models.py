from django.db import models
from django.utils.translation import gettext as _
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.models import Orderable
from wagtailautocomplete.edit_handlers import AutocompletePanel
from wagtail.blocks import TextBlock
from wagtail.fields import StreamField, RichTextField
from wagtail.models import Page
from wagtail.admin.panels import (
    FieldPanel,
    InlinePanel,
    ObjectList,
    TabbedInterface,
)

# from wagtailcodeblock.blocks import CodeBlock

from core.models import CommonControlField
from core.forms import CoreAdminModelForm


class SPSVersion(CommonControlField):
    version = models.CharField(_("Version"), max_length=16, null=False, blank=False)
    begin_year = models.PositiveIntegerField(null=True, blank=True)
    begin_month = models.PositiveIntegerField(null=True, blank=True)
    end_year = models.PositiveIntegerField(null=True, blank=True)
    end_month = models.PositiveIntegerField(null=True, blank=True)

    @property
    def str_begin_year(self):
        return self.begin_year and str(self.begin_year) or ""

    @property
    def str_end_year(self):
        return self.end_year and str(self.end_year) or ""

    def __unicode__(self):
        return f"{self.version} {self.str_begin_year}-{self.str_end_year}"

    def __str__(self):
        return f"{self.version} {self.str_begin_year}-{self.str_end_year}"

    class Meta:
        verbose_name = _("SPS Version")
        verbose_name_plural = _("SPS Versions")

    panels = [
        FieldPanel("version"),
        FieldPanel("begin_year"),
        FieldPanel("begin_month"),
        FieldPanel("end_year"),
        FieldPanel("end_month"),
    ]

    base_form_class = CoreAdminModelForm


class OccurrenceNumber(models.Model):
    """
    Valores para ocorrência do elemento ou atributo. Exemplos:

    - Uma vez
    - Uma ou mais vezes
    - Zero ou uma vez
    - Zero ou mais vezes
    """
    text = models.CharField(_("Text"), max_length=256, null=False, blank=False, help_text=_('Uma vez'))

    def __unicode__(self):
        return self.text

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _("Occurrence number")
        verbose_name_plural = _("Occurrence numbers")

    panels = [
        FieldPanel("text"),
    ]

    base_form_class = CoreAdminModelForm
