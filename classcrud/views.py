from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy
from django.views.generic.list import ListView  # 데이터 보여주기
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # 데이터 추가/수정/삭제
from .models import ClassBlog


class BlogView(ListView):  # html template : 블로그 리스트를 담은 html
    model = ClassBlog  # ClassBlog의 모델로 부터 만들어진 객체의 목록을 보고싶다!
    # template_name = 'classcrud/list.html'   # default 가 classblog_list.html 인걸 list.html로 바꿔서 쓰겠다.
    # context_object_name = 'blog_list'     # object_list를 blog_list로 구분


class BlogCreate(CreateView):  # form을 갖는 html : (소문자모델)_form.html
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')


class BlogDetail(DetailView):  # 상세페이지를 담은 html : (소문자모델)_detail.html
    model = ClassBlog
    # context_object_name = 'blogpost'  # object -> blogpost로 사용가능


class BlogUpdate(UpdateView):  # form을 갖는 html : (소문자모델)_form.html
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')


class BlogDelete(DeleteView):  # 이거 진짜 지울지 확인하는 html 필요 : (소문자모델)_confirm_delete.html
    model = ClassBlog
    success_url = reverse_lazy('list')
