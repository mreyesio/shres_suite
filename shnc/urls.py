# shnc/urls
from django.conf.urls import url
from shnc import views,views_hr,views_bills

#template tagging
app_name = 'shnc'
urlpatterns = [
    url(r'^user_login/$',views.user_login ,name='user_login'),
    url(r'^welcome/$',views.welcome ,name='welcome'),
    url(r'^admin/$',views.AdminListView.as_view(),name='admin_list'),
    url(r'^admin//(?P<pk>\d+)/$',views.AdminDetailView.as_view(),name='admin_details'),
    
#####################################################################################    
    url(r'^bills/$',views_bills.BillListView.as_view(),name='bill_list'),
    url(r'^bills/(?P<pk>\d+)/$',views_bills.BillDetailView.as_view(),name='bill_details'),
    url(r'^bills/new/$',views_bills.CreateBillView.as_view() ,name='bill_new'),

    
    # url(r'^hr/add_nurse/$',views.add_nurse ,name='add_nurse'),
#####################################################################################
    url(r'^hr/view_nurses/$',views_hr.LpnListView.as_view() ,name='lpn_list'),
    url(r'^hr/(?P<pk>\d+)/$',views_hr.LpnDetailView.as_view() ,name='lpn_details'),
    url(r'^hr/new/$',views_hr.CreateLpnView.as_view() ,name='lpn_new'),
    url(r'^hr/(?P<pk>\d+)/edit/$',views_hr.LpnUpdateView.as_view() ,name='lpn_update'),
    url(r'^hr/(?P<pk>\d+)/remove/$',views_hr.LpnDeleteView.as_view() ,name='lpn_remove'),
#####################################################################################
    url(r'^admin/add_user/$',views.add_user ,name='add_user'),
     
]