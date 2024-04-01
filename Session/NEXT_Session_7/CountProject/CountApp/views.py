from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request, 'count.html')

def result(request):
    text=request.POST['text']
    wordLen = len(text.split(" "))
    text_nospace=len(text.replace(" ", ""))
    total_len=len(text)
    return render(request, 'result.html', {'wordLen':wordLen, 'text': text, 'total_len': total_len, 'text_nospace':text_nospace})