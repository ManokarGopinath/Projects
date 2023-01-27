from django.shortcuts import render, redirect
from django.http import HttpResponse
import torch
import json
from .models import Paracheck, Grammercheck, Spellcheck, Filespellcheck
from .forms import ParaForm, GrammerForm, SpellForm, FilespellForm
from gingerit.gingerit import GingerIt
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
from sentence_splitter import SentenceSplitter, split_text_into_sentences

model_name = 'tuner007/pegasus_paraphrase'
torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)
# Create your views here.
def get_response(input_text,num_return_sequences):
      batch = tokenizer.prepare_seq2seq_batch([input_text],truncation=True,padding='longest',max_length=60, return_tensors="pt").to(torch_device)
      translated = model.generate(**batch,max_length=60,num_beams=10, num_return_sequences=num_return_sequences, temperature=1.5)
      tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
      return tgt_text

def index(request):
   return HttpResponse('hello world!')

def grammerform(request):
    if request.method == 'POST':
        form = GrammerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            documents = Grammercheck.objects.all()
            for obj in documents:
                Grammertext = obj.title
            splitter = SentenceSplitter(language='en')
            sentence_list = splitter.split(Grammertext)
            sentence_list

            paraphrase = []
            for i in sentence_list:
              a = get_response(i,1)
              paraphrase.append(a)

              paraphrase

            paraphrase2 = [' '.join(x) for x in paraphrase]
            paraphrase2

            paraphrase3 = [' '.join(x for x in paraphrase2) ]
            paraphrased_text = str(paraphrase3).strip('[]').strip("'")
            paraphrased_text
            with open("./media/json/sample.json", "w") as outfile:
                json.dump(paraphrased_text, outfile)
            # Opening JSON file
            f = open('./media/json/sample.json')
            data = json.load(f)
            rewrtingtext = data
            f.close()
            # parser = GingerIt()
            # output = parser.parse(data)
            # with open("./media/json/data.json", "w") as outfile:
            #     json.dump(output, outfile)
            # # Opening JSON file
            # f = open('./media/json/data.json')
            # data = json.load(f)
            # # list
            # print(data['result'])
            # finaltext = data['result']
            # f.close()
            return render(request, 'para.html', {'rewrtingtext':rewrtingtext, 'grammertext': Grammertext})
            
    else:
        form = ParaForm()
        #documents = Grammercheck.objects.all().order_by('-id')
    return render(request, 'para.html', {
        'form': form,
    })

def paraform(request):
    if request.method == 'POST':
        form = ParaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            documents = Paracheck.objects.all()
            for obj in documents:
                title = obj.description
                fdocument = obj.document.url
            # print(fdocument)
            myfile = open('.'+fdocument,"rt")
            contents = myfile.read()
            myfile.close()
            print(contents)
            paratext = contents
            splitter = SentenceSplitter(language='en')
            sentence_list = splitter.split(paratext)
            sentence_list

            paraphrase = []
            for i in sentence_list:
              a = get_response(i,1)
              paraphrase.append(a)

              paraphrase

            paraphrase2 = [' '.join(x) for x in paraphrase]
            paraphrase2

            paraphrase3 = [' '.join(x for x in paraphrase2) ]
            paraphrased_text = str(paraphrase3).strip('[]').strip("'")
            paraphrased_text
            with open("./media/json/test.json", "w") as outfile:
                json.dump(paraphrased_text, outfile)
            # Opening JSON file
            f = open('./media/json/test.json')
            data = json.load(f)
            originaltext = data
            f.close()
            return render(request, 'checker.html', {'originaltext':originaltext, 'paratext': paratext})
            
    else:
        form = ParaForm()
        #documents = Grammercheck.objects.all().order_by('-id')
    return render(request, 'checker.html', {
        'form': form,
    })

def spellform(request):
    if request.method == 'POST':
        form = SpellForm(request.POST, request.FILES)
        if form.is_valid():
            #func_obj = form
            #func_obj.sourceFile = form.cleaned_data['sourceFile']
            form.save()
            #print(form.Document.document)
            #form.save()
            documents = Spellcheck.objects.all()
            for obj in documents:
                spelltext = obj.description
                #info = obj.info
            #print(rank)
            #print(baseurls)
            #print(grammertext)
            parser = GingerIt()
            output = parser.parse(spelltext)
            with open("./media/json/data1.json", "w") as outfile:
                json.dump(output, outfile)
            # Opening JSON file
            f = open('./media/json/data1.json')
            data = json.load(f)
            # list
            print(data['result'])
            giventext = data['result']
            f.close()
            return render(request, 'spell.html', {'giventext':giventext, 'spelltext': spelltext})
    else:
        form = SpellForm()
        #documents = Grammercheck.objects.all().order_by('-id')
    return render(request, 'spell.html', {
        'form': form,
    })

def filespellform(request):
    if request.method == 'POST':
        form = FilespellForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            documents = Filespellcheck.objects.all()
            for obj in documents:
                title = obj.description
                fdocument = obj.document.url
            print(fdocument)
            #myfile = open("sample.txt", "rt")
            myfile = open('.'+fdocument,"rt")
            contents = myfile.read()
            myfile.close()
            print(contents)
            text = contents
            parser = GingerIt()
            parser.parse(text)
            output = parser.parse(contents)
            with open("./media/json/grammar.json", "w") as outfile:
                 json.dump(output, outfile)
            f = open('./media/json/grammar.json')
            data = json.load(f)
            # list
            print(data['result'])
            rewrtingtext = data['result']
            f.close() 
        return render(request, 'filespell.html', {
        'form': form, 'rewrtingtext': rewrtingtext, 'grammertext': contents,
    })

    else:
        fileform = FilespellForm()
        #documents = Grammercheck.objects.all().order_by('-id')
        return render(request, 'filespell.html', {
        'form': fileform, 
    })
