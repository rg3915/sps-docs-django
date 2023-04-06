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

from core.models import CommonControlField
from core.forms import CoreAdminModelForm


class SPSVersion(ClusterableModel, CommonControlField):
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

    def autocomplete_label(self):
        return str(self)

    autocomplete_search_field = "version"

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

    text = models.CharField(
        _("Text"), max_length=256, null=False, blank=False, help_text=_("Uma vez")
    )

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


class Presence(Orderable, CommonControlField):
    parent = ParentalKey("SPSBase", on_delete=models.CASCADE, related_name="presence")
    present_in = models.ForeignKey(
        "SPSBase",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="present_in",
    )
    occurrence_number = models.ForeignKey(
        OccurrenceNumber, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __unicode__(self):
        return f"{self.present_in} {self.occurrence_number}"

    def __str__(self):
        return f"{self.present_in} {self.occurrence_number}"

    class Meta:
        verbose_name = _("Presence")
        verbose_name_plural = _("Presence")

    panels = [
        FieldPanel("present_in"),
        FieldPanel("occurrence_number"),
    ]

    base_form_class = CoreAdminModelForm


class NoteBlock(Orderable, ClusterableModel, CommonControlField):
    parent = ParentalKey("SPSBase", on_delete=models.CASCADE, related_name="note_block")
    title = models.CharField(_("Title"), max_length=256, null=True, blank=True)
    text = RichTextField(_("Notes"), null=True, blank=True)

    def __unicode__(self):
        return self.title or ""

    def __str__(self):
        return self.title or ""

    class Meta:
        verbose_name = _("Note block")
        verbose_name_plural = _("Note blocks")

    panels = [
        FieldPanel("title"),
        FieldPanel("text"),
    ]

    base_form_class = CoreAdminModelForm


class Example(Orderable, ClusterableModel, CommonControlField):
    parent = ParentalKey("SPSBase", on_delete=models.CASCADE, related_name="example")
    title = models.TextField(_("Title"), null=True, blank=True)
    description = RichTextField(_("Description"), null=True, blank=True)
    # https://github.com/FlipperPA/wagtailcodeblock
    xml_code_text = models.TextField(_("XML Code"), null=True, blank=True)
    xml_code_image = models.ImageField(upload_to="xml_examples", null=True, blank=True)

    class Meta:
        verbose_name = _("Example")
        verbose_name_plural = _("Examples")

    panels = [
        FieldPanel("title"),
        FieldPanel("description"),
        FieldPanel("xml_code_text"),
        FieldPanel("xml_code_image"),
    ]

    base_form_class = CoreAdminModelForm


class SPSBase(ClusterableModel, CommonControlField):
    name = models.CharField(_("Name"), max_length=256, null=False, blank=False)
    description = RichTextField(_("Description"), null=True, blank=True)
    # versions
    sps_versions = models.ManyToManyField(
        SPSVersion,
        blank=True,
    )

    def __unicode__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"

    class Meta:
        indexes = [
            models.Index(
                fields=[
                    "name",
                ]
            ),
        ]

    panels_main = [
        FieldPanel("name"),
        FieldPanel("description"),
    ]
    panels_presence = [
        InlinePanel("presence", label=_("Presence"), classname="collapsed"),
    ]
    panels_example = [
        InlinePanel("example", label=_("Example"), classname="collapsed"),
    ]
    panels_note_block = [
        InlinePanel("note_block", label=_("Note block"), classname="collapsed"),
    ]
    panels_version = [
        AutocompletePanel("sps_versions"),
    ]
    edit_handler = TabbedInterface(
        [
            ObjectList(panels_main, heading=_("Main")),
            ObjectList(panels_version, heading=_("SPS Versions")),
            ObjectList(panels_presence, heading=_("Presence")),
            ObjectList(panels_example, heading=_("Examples")),
            ObjectList(panels_note_block, heading=_("Note blocks")),
        ]
    )
    base_form_class = CoreAdminModelForm


class SPSElement(SPSBase):
    """
    (*) Nome do elemento
    (*+) Aparece em
    (*+) Descrição do elemento
    (!+) attrs
    (!+) Título do exemplo
    (!+) Descrição textual do exemplo
    (!+) Exemplo XML
    (!+) Nota
    """

    attributes = models.ManyToManyField('SPSAttribute')

    class Meta:
        verbose_name = _("Element")
        verbose_name_plural = _("Elements")

    panels_attribute = [
        AutocompletePanel("attributes"),
    ]
    panels_main = [
        FieldPanel("name"),
        FieldPanel("description"),
    ]
    panels_presence = [
        InlinePanel("presence", label=_("Presence"), classname="collapsed"),
    ]
    panels_example = [
        InlinePanel("example", label=_("Example"), classname="collapsed"),
    ]
    panels_note_block = [
        InlinePanel("note_block", label=_("Note block"), classname="collapsed"),
    ]
    panels_version = [
        AutocompletePanel("sps_versions"),
    ]
    edit_handler = TabbedInterface(
        [
            ObjectList(panels_main, heading=_("Main")),
            ObjectList(panels_attribute, heading=_("Attributes")),
            ObjectList(panels_version, heading=_("SPS Versions")),
            ObjectList(panels_presence, heading=_("Presence")),
            ObjectList(panels_example, heading=_("Examples")),
            ObjectList(panels_note_block, heading=_("Note blocks")),
        ]
    )


class SPSAttribute(SPSBase):
    """
    (*) Nome do atributo
    (*+) Aparece em
    (*+) Descrição do atributo
    (!+) values
    (!+) Título do exemplo
    (!+) Descrição textual do exemplo
    (!+) Exemplo XML
    (!+) Nota
    """

    def autocomplete_label(self):
        return str(self)

    autocomplete_search_field = "name"

    class Meta:
        verbose_name = _("Attribute")
        verbose_name_plural = _("Attributes")
