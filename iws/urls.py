from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from iws import api

urlpatterns = [
    url(r'^api/risktype/$', api.RiskTypeList.as_view(), name='get_post_risktype'),
    url(r'^api/risktype/(?P<pk>[0-9]+)/$', api.RiskTypeDetail.as_view(), name='get_detail_risktype'),
    url(r'^api/field/$', api.FieldList.as_view(), name='get_post_field'),
    url(r'^api/field/(?P<pk>[0-9]+)/$', api.FieldDetail.as_view(), name='field_detail'),
    url(r'^api/form/$', api.FormAPIView.as_view()),

]