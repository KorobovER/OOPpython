from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import AdvUser, Posts
from django.views.generic import CreateView
from .forms import RegisterUserForm, PostsForm
from django.views.generic.base import TemplateView
from django.views.generic import DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import FilterForm
from django.db.models import Q


def index(request):
    bbs = Posts.objects.filter(status='Выполнено').order_by('-created_at')[:4]
    count = Posts.objects.filter(status='Принято в работу').count()
    context = {'bb': bbs, 'count': count}
    return render(request, 'main/index.html', context)


def other_page(request, page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))


class BBLoginView(LoginView):
    template_name = 'main/login.html'


@login_required
def profile(request):
    post_all = Posts.objects.all()
    if request.user.is_staff:
        posts = Posts.objects.filter()
    else:
        posts = Posts.objects.filter(author=request.user.pk)
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        q = Q(status__icontains=keyword)
        posts = posts.filter(q)
    else:
        keyword = ''
    form = FilterForm(initial={'keyword': keyword})
    context = {'posts': posts, 'form': form}
    return render(request, 'main/profile.html', context)


class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'main/logout.html'


class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'main/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:register_done')


class RegisterDoneView(TemplateView):
    template_name = 'main/register_done.html'


@login_required
def profile_posts_add(request):
    if request.method == 'POST':
        form = PostsForm(request.POST, request.FILES)
        if form.is_valid():
            posts = form.save()
            return redirect('main:profile')
    else:
        form = PostsForm(initial={'author': request.user.pk})
    context = {'form': form}
    return render(request, 'main/posts_add.html', context)


class profile_posts_delete(SuccessMessageMixin, DeleteView):
    model = Posts
    template_name = 'main/posts_delete.html'
    success_url = '/accounts/profile/'
    success_message = "Объявление удалено"
