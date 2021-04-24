from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm



from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Event
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, JsonResponse


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """

    form = AuthenticationForm(data=request.POST or None)

    return render(request, 'registration/login.html', {
        'form': form
    })


@login_required
def event(request):

    events = Event.objects.filter(author__username=request.user.username)
    print(events)
    return render(request, 'event.html', {'events': events})



class MyAuthForm(AuthenticationForm):
    error_messages = {
        'invalid_login': _(
            "Вы ввели неверные данные. "

        ),
        'inactive': _("This account is inactive."),
    }

class MyLoginView(LoginView):
    authentication_form = MyAuthForm





class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = '__all__'
    # fields = ['summary', 'date', ]
    success_url = reverse_lazy('event')



    def form_valid(self, form):

        # Добавить зарегистрированного пользователя как автора event
        form.instance.author = self.request.user
        # Вызвать поведение проверки формы суперкласса
        return super(EventCreate, self).form_valid(form)

class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ['done']
    success_url = reverse_lazy('event')


class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('event')


@csrf_exempt
def event_done(request, pk):
    # ToDo something
    # Step 1 Get object from model
    # Step 2 Update object
    print(pk)
    obj = Event.objects.get(pk=pk)

    print(obj.done)
    obj.done = True
    obj.save()
    obj.refresh_from_db()
    print(obj.done)
    return JsonResponse({"result": "ok"}, status=200)


@csrf_exempt
def event_undone(request, pk):
    # ToDo something
    # Step 1 Get object from model
    # Step 2 Update object
    # print(pk)
    obj = Event.objects.get(pk=pk)

    # print(obj.done)
    obj.done = False
    obj.save()
    obj.refresh_from_db()
    # print(obj.done)
    return JsonResponse({"result": "ok"}, status=200)
