from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from home.views import index
from login.views import *
#from employee.views import *
from employeeall.views import * 
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	
    url(r'^$', home1),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$','django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home1),
    #url(r'^add/addemployee/$',contact),
    url(r'^addemployee/$',contact),
    url(r'^search/$',search),
	url(r'allsearch/$',allsearch),
	url(r'edit/(\d+)$',edit),
	url(r'^display/$',display),
	url(r'^find/$',find),	
	url(r'^edithistory/$',edithistory),
	url(r'^filterhistory/$',filteremp),
	url(r'emphis/(\d+)$',emphis),
	url(r'emp/(\d+)$',emp),
	url(r'empinfo/(\d+)$',empinfo),
	url(r'^addproject/$',addproject),
	url(r'^showproject/$',showproject),
	url(r'empproject/(\d+)$',empproject),
	url(r'^disemppro/$',disemppro),
	url(r'phonehis/(\d+)$',phonehis),
	url(r'designationhis/([\w ]+)$',designationhis),
	url(r'^addorganization/$',addorganization),
	url(r'^displayorg/$',displayOrg),
	url(r'editOrg/(\d+)$',editOrg),
	url(r'^adddepartment/$',addDepartment),
	url(r'^displaydept/$',displayDept),
	url(r'editDept/(\d+)$',editDept),
	url(r'orginfo/(\d+)$',orginfo),
	url(r'org_dept/(\d+)$',org_dept),
	url(r'deptinfo/(\d+)$',deptinfo),
	url(r'org_employee/(\d+)$',org_employee),
	url(r'dept_employee/(\d+)$',dept_employee),
	url(r'org_project/(\d+)$',org_project),
	url(r'edit_project/(\d+)$',edit_project),
	url(r'project_history/(\d+)$',project_history),
	url(r'dept_history/(\d+)$',dept_history),
	url(r'org_history/(\d+)$',org_history),
	url(r'fileupload/[\w]+/[\w]+/([\w]+.[\w]+)$',fileupload),
	url(r'viewproject/(\d+)$',viewproject),
	url(r'^addcomment/$',addcomment	),
	url(r'^addact/$',addact),
	url(r'^showallact/$',showallact),
	url(r'^addchapter/$',addchapter),
	url(r'^showallchapter/$',showallchapter),
	url(r'^addsection/$',addsection),
	url(r'^showallsection/$',showallsection),
	url(r'editAct/(\d+)$',editAct),
	url(r'editChapter/(\d+)$',editChapter),
	url(r'editSection/(\d+)$',editSection),
	url(r'act_chapter/(\d+)$',act_chapter),
	url(r'chapter_section/(\d+)$',chapter_section),
	url(r'act_section/(\d+)$',act_section),
	url(r'showact/(\d+)$',showact),
	url(r'showchapter/(\d+)$',showchapter),
	url(r'act_history/(\d+)$',acthistory),
	url(r'chapter_history/(\d+)$',chapterhistory),
	url(r'section_history/(\d+)$',sectionhistory),
	url(r'^addapp/$',addapp),
	url(r'^showallapp/$',show_all_app),
	url(r'editapp/(\d+)$',edit_app),
	url(r'app_history/(\d+)$',app_history),
	url(r'^adddur/$',add_dur),
	url(r'^showalldur/$',show_all_dur),
	url(r'editdur/(\d+)$',edit_dur),
	url(r'dur_history/(\d+)$',dur_history),
	url(r'^addpad/$',add_pad),
	url(r'^showallpad/$',show_all_pad),
	url(r'editpad/(\d+)$',edit_pad),
	url(r'pad_history/(\d+)$',pad_history),
	url(r'^addrem/$',add_rem),
	url(r'^showallrem/$',show_all_rem),
	url(r'editrem/(\d+)$',edit_rem),
	url(r'rem_history/(\d+)$',rem_history),
	url(r'^add_desig/$',add_deg),
	url(r'^showalldesig/$',show_all_desig),
	url(r'editdesig/(\d+)$',edit_desig),
	url(r'desig_history/(\d+)$',desig_history),
	url(r'^addthirdparty/$',add_third),
	url(r'^showallparty/$',show_third),
	url(r'editparty/(\d+)$',edit_party),
	url(r'party_history/(\d+)$',party_history),
	url(r'desig_app/(\d+)$',desig_app),
	url(r'desig_dur/(\d+)$',desig_dur),
	url(r'desig_pad/(\d+)$',desig_pad),
	url(r'desig_rem/(\d+)$',desig_rem),
	url(r'appact/(\d+)$',app_act),
	url(r'appchapter/(\d+)$',app_chapter),
	url(r'appsection/(\d+)$',app_section),
	url(r'projectparty/(\d+)$',project_party),
    # Examples:
    #url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += patterns('',
       (r'^media/(?P<path>.*)$', 'django.views.static.serve',
{'document_root':'/static/'}),
    ) 


