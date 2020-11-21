from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogView.as_view(), name='list'),
    path('newblog/', views.BlogCreate.as_view(), name='new'),
    path('detail/<int:pk>', views.BlogDetail.as_view(), name='detail'),
    path('update/<int:pk>', views.BlogUpdate.as_view(), name='change'),
    path('delete/<int:pk>', views.BlogDelete.as_view(), name='del'),
]

# .as_view() => Class에 해당하는 메서드
# views.py를 클래스로 정의(Generic view를 사용)했으면 path의 두번째 인자를
# 클래스로 할 수 없으니깐 , 상속받은 것의 메서드인 as_view를 인자로 넘겨준다.
# => 클래스이름.as_view()
