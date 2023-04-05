from django.http import HttpResponseRedirect
from django.urls import include, path
from django.utils.translation import gettext as _
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)
from wagtail.contrib.modeladmin.views import CreateView, EditView

from spstaglib.models import SPSVersion


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
    ordering = ("version", )
    create_view_class = SPSVersionCreateView
    edit_view_class = SPSVersionEditView
    menu_label = _("SPS Version")
    menu_icon = "folder"
    menu_order = 100
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = (
        False  # or True to exclude pages of this type from Wagtail's explorer view
    )
    list_display = ("version", "begin_year", "begin_month", "end_year", "end_month", )
    search_fields = ("version", "begin_year", "end_year", )


class SPSAdminGroup(ModelAdminGroup):
    menu_label = _("SPS")
    menu_icon = "folder-open-inverse"
    menu_order = 200
    items = (SPSVersionAdmin, )


modeladmin_register(SPSAdminGroup)
