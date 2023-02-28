import openai
import json
# from django.template import Context
from django.shortcuts import render
 

openai.api_key = "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"

def chatbot(request):
    openai.api_key = "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"
    model_engine = "davinci"
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
