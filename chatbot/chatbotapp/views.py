import openai
import json
# from django.template import Context
from django.shortcuts import render
 

openai.api_key = "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"

def chatbot(request):
    if request.method == 'POST':
        prompt = request.POST['query']
        prompt=str(prompt)
        result=openai.Image.create(
        prompt=prompt,
           n=2, size="1024x1024")
        url=result.data[0].url
        Context={
            'query':prompt,
                  'resp': url
              }

        return render(request, "index.html",Context)
    Context={
          'query':"",
                  'resp': "https://tinypic.host/images/2023/02/28/gen.png"
              }
    return render(request, "index.html",Context)
