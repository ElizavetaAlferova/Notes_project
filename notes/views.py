from django.shortcuts import get_object_or_404, render
from django.http import response, HttpRequest, HttpResponse
from .models import Note
from django.http import FileResponse, Http404
from django.views.generic import ListView
from .forms import NoteCreateForm
from django.shortcuts import redirect
from django.db.models import Q
from django.views.decorators.clickjacking import xframe_options_exempt

def pdf_view(request, pk):
    try:
        return FileResponse(open('D://Dev/notes_project/notes_project/media/'+ str(Note.objects.get(pk=pk).pdf), 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404



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

@xframe_options_exempt
def notes_detail(request, pk):
    template = 'notes_detail.html'
    notes =get_object_or_404(Note.objects.filter(pk=pk))
    context = {'notes': notes}
    return render(request, template, context)


def create_notes(request):
    form = NoteCreateForm(
        request.POST or None,
        files = request.FILES or None)
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
    form = NoteCreateForm(request.POST or None,
                          instance=instance,
                          files=request.FILES or None)
    # Всё остальное без изменений.
    context = {'form': form}
    # Сохраняем данные, полученные из формы, и отправляем ответ:
    if form.is_valid():
        form.save()
    return render(request, 'notes.html', context)


def delete(request, pk):
    instance = get_object_or_404(Note, pk=pk)
    form = NoteCreateForm(instance=instance)
    context = {'form': form}
    if request.method == 'POST':
        instance.delete()
        return redirect('/')
    return render(request, 'notes.html', context)


def search(request):
    template = 'search.html'
    notes =''
    context = {'notes': notes}
    return render(request, template, context)


def search_answer(request):
    template = 'search_answer.html'
    query = request.GET.get('q')
    notes = Note.objects.filter(Q(title__icontains=query) | Q(composer__icontains=query))
    context = {'notes': notes}
    return render(request, template, context)


