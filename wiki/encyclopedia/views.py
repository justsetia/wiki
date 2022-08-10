
import random
from secrets import choice
from unicodedata import name
from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
import markdown2

from encyclopedia.forms import entriesform


from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request, title):
    entry = util.get_entry(title)
    entry = markdown2.markdown(entry)
    return render(request, 'encyclopedia/title.html', {'entry': entry})


def search(request):
    title = request.GET.get('q')
    title = title.upper()
    entries = util.list_entries()
    for name in entries:
        name = name.upper()
        if title in name:
            title = name
            break

    entry = util.get_entry(title)

    if entry is not None:
        return redirect('title', title)

    else:
        return render(request, 'encyclopedia/index.html', {'res': "The entry doesn't exist "
                                                           })


def smart_search(request, char):
    show = []

    entry = util.list_entries()
    for name in entry:
        if name[0].upper() == char.upper():
            print('yes')
            show.append(name)

    if show == []:
        return render(request, 'encyclopedia/index.html', {'res': 'There is no entry'})
    else:
        return render(request, 'encyclopedia/index.html', {'show': show})


def create(request):
    if request.method == 'GET':
        form = entriesform()
        return render(request, 'encyclopedia/create.html', {'form': form})

    elif request.method == 'POST':
        form = entriesform(request.POST)
        if form.is_valid():
            return redirect('title', form.cleaned_data['name'])

        return render(request, 'encyclopedia/create.html', {'form': form})
       # return render(request, 'encyclopedia/index.html')


def edit(request, title):
    if request.method == 'POST':
        print(request.POST)
        util.save_entry(title, request.POST['about'])
        return redirect('title', title)

    else:
        form = util.get_entry(title)
        return render(request, 'encyclopedia/edit.html', {'form': form, 'title': title})


def delete(request, title):
    util.delete_entry(title)
    return redirect('index')


def chance(request):
    list_name = util.list_entries()

    choose = random.choice(list_name)

    return redirect('title', choose)
