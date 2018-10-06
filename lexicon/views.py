from django.shortcuts import render
from lexicon.models import WordList, Polarity
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    # file = open('C:/Users/imran/Dropbox/Bengali VADER/bengaliSentiment/lexicon/new_lexicon.txt', encoding='utf-8-sig')
    # list = [l for l in file]
    # for l in list:
    #     w = WordList(word=l)
    #     w.save()
    if request.method == 'POST':
        valence = request.POST.getlist('polarity')
        word_id = request.POST.getlist('word_id')
        # print(valence, word_id)
        for v, w in zip(valence, word_id):
            a = WordList.objects.get(pk=w)
            s = Polarity(valence=v, word_id=a)
            s.save()
            
    words = WordList.objects.raw('SELECT * FROM lexicon_wordlist ORDER BY RAND()')
    paginator = Paginator(words, 10)

    page = request.GET.get('page')
    word_list = paginator.get_page(page)
    # print(word_list.word)
    return render(request, 'home.html', {
        'word_list': word_list,
    })