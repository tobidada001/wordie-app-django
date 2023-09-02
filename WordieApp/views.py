from django.shortcuts import render, redirect
import requests as req
from django.contrib import messages
from itertools import chain
# Create your views here.

def index(request):
    word_to_check = None
    context = {}
    
    if 'check' in request.GET:
        word_to_check = request.GET.get('check', None)

        if not word_to_check:
            messages.error(request, 'You didn\'t enter any word!')
            return redirect('/')
        
        try:
            data = req.get('https://api.dictionaryapi.dev/api/v2/entries/en/'+word_to_check).json()
            
            synonyms, word_meanings, antonyms, examples = [], [], [], []
            pron_sound = None
            pron = None
           

            for i in data:
                for sound in i['phonetics']:
                    if sound['audio']:
                        pron_sound = sound.get('audio')
                        pron = sound.get('text')
                        break
                
                for meanings in i['meanings']:
                    synonyms.append(meanings['synonyms'])
                    antonyms.append(meanings['antonyms'])
                    

                    for definition in meanings['definitions']:
                        word_meanings.append(definition['definition'])
                        synonyms.append(definition['synonyms'])
                        antonyms.append(definition['antonyms'])
                        examples.append(definition.get('example'))

            context = {
                'synonyms': chain.from_iterable(synonyms),  'antonyms': chain.from_iterable(antonyms),  'meanings': word_meanings,
                'examples': examples,  'word': data[0]['word'], 'pronunciation': pron, 'audio_link': pron_sound,
                }
           
            
        except:
            messages.error(request, 'Word not found. Please check the spelling and try again.')
            return redirect('/')

    return render(request, 'index.html', context)