from django.http import HttpResponseRedirect
from django.urls import include, path
from django.utils.translation import gettext as _
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)
from wagtail.contrib.modeladmin.views import CreateView, EditView

from spstaglib.models import (
    SPSVersion,
    OccurrenceNumber,
    Example,
    SPSElement,
)


class SPSVersionCreateView(CreateView):
    def form_valid(self, form):
        self.object = form.save_all(self.request.user)
        return HttpResponseRedirect(self.get_success_url())


class SPSVersionEditView(EditView):
    def form_valid(self, form):
        self.object = form.save_all(self.request.user)
        return HttpResponseRedirect(self.get_success_url())


class SPSVersionAdmin(ModelAdmin):
    model = SPSVersion
    ordering = ("version",)
    create_view_class = SPSVersionCreateView
    edit_view_class = SPSVersionEditView
    menu_label = _("SPS Version")
    menu_icon = "folder"
    menu_order = 100
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = (
        False  # or True to exclude pages of this type from Wagtail's explorer view
    )
    list_display = (
        "version",
        "begin_year",
        "begin_month",
        "end_year",
        "end_month",
    )
    search_fields = (
        "version",
        "begin_year",
        "end_year",
    )


class OccNumCreateView(CreateView):
    def form_valid(self, form):
        self.object = form.save_all(self.request.user)
        return HttpResponseRedirect(self.get_success_url())


class OccNumEditView(EditView):
    def form_valid(self, form):
        self.object = form.save_all(self.request.user)
        return HttpResponseRedirect(self.get_success_url())


class OccNumAdmin(ModelAdmin):
    model = OccurrenceNumber
    ordering = ("text",)
    create_view_class = OccNumCreateView
    edit_view_class = OccNumEditView
    menu_label = _("Occurrence Number")
    menu_icon = "folder"
    menu_order = 100
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = (
        False  # or True to exclude pages of this type from Wagtail's explorer view
    )
    list_display = ("text",)
    search_fields = ("text",)


class ExampleCreateView(CreateView):
    def form_valid(self, form):
        self.object = form.save_all(self.request.user)
        return HttpResponseRedirect(self.get_success_url())


class ExampleEditView(EditView):
    def form_valid(self, form):
        self.object = form.save_all(self.request.user)
        return HttpResponseRedirect(self.get_success_url())


class ExampleAdmin(ModelAdmin):
    model = Example
    ordering = ("title",)
    create_view_class = ExampleCreateView
    edit_view_class = ExampleEditView
    menu_label = _("Examples")
    menu_icon = "folder"
    menu_order = 100
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = (
        False  # or True to exclude pages of this type from Wagtail's explorer view
    )
    list_display = ("title", "description", "xml_code_text", "xml_code_image")
    search_fields = (
        "title",
        "description",
    )


class SPSElementCreateView(CreateView):
    def form_valid(self, form):
        self.object = form.save_all(self.request.user)
        return HttpResponseRedirect(self.get_success_url())


class SPSElementEditView(EditView):
    def form_valid(self, form):
        self.object = form.save_all(self.request.user)
        return HttpResponseRedirect(self.get_success_url())


class SPSElementAdmin(ModelAdmin):
    model = SPSElement
    ordering = ("name",)
    create_view_class = SPSElementCreateView
    edit_view_class = SPSElementEditView
    menu_label = _("Elements")
    menu_icon = "folder"
    menu_order = 100
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = (
        False  # or True to exclude pages of this type from Wagtail's explorer view
    )
    list_display = (
        "name",
        "description",
    )
    search_fields = (
        "name",
        "description",
    )


class SPSAdminGroup(ModelAdminGroup):
    menu_label = _("SPS")
    menu_icon = "folder-open-inverse"
    menu_order = 200
    items = (
        SPSVersionAdmin,
        OccNumAdmin,
        ExampleAdmin,
        SPSElementAdmin,
    )


modeladmin_register(SPSAdminGroup)
