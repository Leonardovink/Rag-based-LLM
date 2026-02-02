from django.shortcuts import render

# Create your views here.
from .question import QuestionForm

def ask_question(request):
    answer = None

    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data["question"]
            # placeholder answer for now
            answer = f"You asked: {question}"
    else:
        form = QuestionForm()

    return render(request, "qa/ask.html", {
        "form": form,
        "answer": answer
    })
