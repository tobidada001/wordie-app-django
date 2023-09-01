from django.shortcuts import render, redirect
from pprint import pprint as pp
from django.http import HttpResponse
from . import syn_ant_loop
import requests as req
from django.contrib import messages
# Create your views here.

def index(request):
    word_to_check = None
    college = []
    thesaurus = []
    context = {}
    sound_or_pronounce = None
    audio = ''
    pron = ''

    
    if 'check' in request.GET:

        word_to_check = request.GET.get('check', None)

        if not word_to_check:
            messages.error(request, 'You didn\'t enter any word!')
            return redirect('/')
        
        try:
            college = req.get('https://dictionaryapi.com/api/v3/references/collegiate/json/'+word_to_check+'?key=0f55e041-8e0c-47e8-bcb5-0c7cfd05cb35').json()
            
            thesaurus = req.get('https://dictionaryapi.com/api/v3/references/ithesaurus/json/'+word_to_check+'?key=869bafc3-8999-493d-a211-50975dfaef66').json()
            print('Yes, yes,')
            for i in range(len(college)):
                try:
                    audio = college[i]['hwi']['prs'][0]['sound']['audio']
                    pron = college[i]['hwi']['prs'][0]['mw']
                    if audio and pron:
                        break
                except KeyError:
                    continue
                except BaseException:
                    return redirect('/')
            
            context = {
                'synonyms': syn_ant_loop.get_syns(thesaurus), 
                'antonyms': syn_ant_loop.get_ants(thesaurus),
                'meanings': syn_ant_loop.get_meanings(college),
                'examples': syn_ant_loop.get_examples(thesaurus),
                'word': college[0]['hwi']['hw'],
                'pronunciation': pron,
                'audio_link': 'https://media.merriam-webster.com/audio/prons/en/us/mp3'+syn_ant_loop.get_audio(audio)+audio+'.mp3'}
        except BaseException :
            messages.error(request, 'An error has occured. Please try again.')
            return redirect('/')

    return render(request, 'index.html', context)