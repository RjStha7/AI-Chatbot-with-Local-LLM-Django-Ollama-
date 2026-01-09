from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .ai_service import ask_ai

def chat_page(request):
    return render(request, "chat.html")

@csrf_exempt
def chat_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")
        ai_response = ask_ai(user_message)
        return JsonResponse({"response": ai_response})
    return JsonResponse({"error": "POST only"})