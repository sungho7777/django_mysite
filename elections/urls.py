from django.conf.urls import url
from . import views

app_name = 'elections'
urlpatterns = [
    url(r'^$', views.index, name = 'home'),
    url(r'^areas/(?P<area>[가-힣]+)/$', views.areas), #수정
    url(r'^areas/(?P<area>[가-힣]+)/results$', views.results), #추가. 꼭 r'^areas/(?P<area>[가-힣]+)/$' 보다 밑에 적어주세요.
    url(r'^polls/(?P<poll_id>\d+)/$', views.polls),
	url(r'^candidates/(?P<name>[가-힣]+)/$', views.candidates),
]
