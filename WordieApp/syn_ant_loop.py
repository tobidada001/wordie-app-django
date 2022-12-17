import re
from pprint import pprint as pp
def get_syns(other_data):
    
    synonymn = []
    
    for i in other_data:
        try:

            if i['meta']['syns']:
                for j in i['meta']['syns']:
                    
                    for syn in j:
                        if len(synonymn) < 10:
                            synonymn.append(syn)
            else:
                continue
        except TypeError:
            continue
    return synonymn


def get_ants(other_data):
    antonymn = []

    for i in other_data:
        try:
            if i['meta']['ants']:
                for j in i['meta']['ants']:
                
                    for ant in j: 
                        if len(antonymn) < 10:
                            antonymn.append(ant)
            else:
                continue
        except TypeError:
            continue
    return antonymn

def get_meanings(other_data):
    meanings = []

    for i in other_data:
        try:

            for j in i['shortdef']:
                
                if len(meanings) < 12:
                    meanings.append(j)
        except TypeError:
            continue            
    return meanings

def get_examples(other_data):
    examples = []
    #pp(other_data[1]['def'][0]['sseq'][0][0][1]['dt'][1][1])
    for i in other_data:
        try:
            for j in i['def'][0]['sseq'][0][0][1]['dt'][1][1]: 
                if len(examples) < 15:
                    examples.append(j) 
        except TypeError:
            return []            
    return examples

def get_audio(audio):
    link = ''
    
    if re.search('^bix', audio):
        link = '/bix/'
    elif re.search('^gg', audio):
        link = '/gg/'
    elif re.search('^[a-zA-Z]', audio):
        link = '/'+audio[0]+'/'
    else:
        link = '/number/'

    return link
    