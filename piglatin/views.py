from django.http import HttpResponse
from django.shortcuts import render
from . import piglatin
from indic_transliteration import sanscript,detect # pip install indic_transliteration



def home(request):
	return render(request,"home.html")

def translate(request):
	originaltext=request.GET["originaltext"]
	#piglatinText=piglatin.convert_sentence(originaltext.lower())
	piglatinText = sanscript.transliterate(originaltext, sanscript.HK  , sanscript.DEVANAGARI)

	return render(request,"translate.html",{'original':originaltext,'translation':piglatinText})

def about(request):
	return render(request,"about.html")
