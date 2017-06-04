from django.shortcuts import redirect
from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import EntryForm
from .models import Entry

def frontpage(request):
    entries_all = Entry.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    paginator = Paginator(entries_all,5)
    page = request.GET.get('page')
    try:
        entries = paginator.page(page)
    except PageNotAnInteger:
        entries = paginator.page(1)
    except EmptyPage:
        entries = paginator.page(paginator.num_pages)
    return render_to_response('blog/frontpage.html',{'entries':entries})

def frontpage_redirect(request):
    return redirect('frontpage')

#def entry_detail(request, pk):
#    entry = get_object_or_404(Entry, pk=pk)
#    return render(request,'blog/entry_detail.html',{'entry':entry})



@login_required
def entry_form(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = request.user
            entry.pub_date = timezone.now()
            entry.save()
            return redirect('entry_detail', pk=entry.pk)
    else:
        form = EntryForm()
    return render(request,'blog/entry_edit.html',{'form':form})

#