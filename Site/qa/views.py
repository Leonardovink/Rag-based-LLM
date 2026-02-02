from django.shortcuts import render
from django.http import JsonResponse
from .rag import query_rag


def ask_page(request):
    return render(request, "qa/ask.html")

def rag_chat(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)

    question = request.POST.get("question")
    if not question:
        return JsonResponse({"error": "No question provided"}, status=400)

    answer, sources = query_rag(question)

    return JsonResponse({
        "answer": answer,
        "sources": sources,
    })