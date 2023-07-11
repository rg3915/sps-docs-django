from django.urls import include, path

from backend.spstaglib import views as v

app_name = 'spstaglib'


# A ordem das urls é importante por causa do slug.
spselement_urlpatterns = [
    # path('', v.spselement_list, name='spselement_list'),  # noqa E501
    path('create/', v.SPSElementCreateView.as_view(), name='spselement_create'),  # noqa E501
    # path('<slug:slug>/', v.spselement_detail, name='spselement_detail'),  # noqa E501
    # path('<slug:slug>/update/', v.spselement_update, name='spselement_update'),  # noqa E501
    # path('<slug:slug>/delete/', v.spselement_delete, name='spselement_delete'),  # noqa E501
]

urlpatterns = [
    path('spselement/', include(spselement_urlpatterns)),
]
