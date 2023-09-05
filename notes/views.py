from django.shortcuts import get_object_or_404, render
from django.http import response, HttpRequest, HttpResponse
from .models import Note, Comment, User
from django.http import FileResponse, Http404
from django.views.generic import ListView
from .forms import NoteCreateForm
from django.shortcuts import redirect


def pdf_view(request):
    try:
        return FileResponse(open('D://Dev/Twilight-Bellas-Lullaby.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()


class IndexListView(ListView):
    model = Note
    ordering = 'id'
    paginate_by = 100

def about(request):
    template = 'about.html'
    notes =''
    context = {'notes': notes}
    return render(request, template, context)


def rules(request):
    template = 'rules.html'
    notes = ''
    context = {'notes': notes}
    return render(request, template)


def notes_detail(request, pk):
    template = 'notes_detail.html'
    notes =get_object_or_404(Note.objects.filter(pk=pk))
    context = {'notes': notes}
    return render(request, template, context)


def create_notes(request):
    form = NoteCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, 'notes.html', context)


def edit(request, pk):
    # Находим запрошенный объект для редактирования по первичному ключу
    # или возвращаем 404 ошибку, если такого объекта нет.
    instance = get_object_or_404(Note, pk=pk)
    # Связываем форму с найденным объектом: передаём его в аргумент instance.
    form = NoteCreateForm(request.POST or None, instance=instance)
    # Всё остальное без изменений.
    context = {'form': form}
    # Сохраняем данные, полученные из формы, и отправляем ответ:
    if form.is_valid():
        form.save()
    return render(request, 'notes.html', context)



