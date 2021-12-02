from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Bookmark
from django.urls import reverse_lazy

# Create your views here.
class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6

class BookmarkCreateView(CreateView):   # 제너릭 뷰인 크리에이트 뷰를 상속 받아 생성
    model = Bookmark                    # 어떤 모델의 입력을 받을 지 생성
    fields = ['site_name', 'url']       # 어떤 필드들을 입력 받을 지 설정하는 부분
    success_url = reverse_lazy('bookmark:list')  # 북마크 추가를 완료하고 목록페이지로 이동
    template_name_suffix = '_create'    # 사용할 템플릿의 접미사만 변경하는 설정 값

    # 기본으로 설정된 템플들은 모델명 _xxx 형태로, CreateView와 UpdateView는 "_form"이 접미사임
    # 이런 기본 접미사가 아닌 bookmark_create.html 라는 이름의 템플릿 파일을 사용하도록 설정하는 것

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:list')