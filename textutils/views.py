# created by me
import string
from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     return HttpResponse("<h1>Hello</h1>")


def about(request):
    return render(request, "about.html")


# def index(request):
#     s = "Hello"
#     html1 = '''<button><a href="http://127.0.0.1:8000/capitalize/">capitalize</a></button>'''
#     html2 = '''<button><a href="http://127.0.0.1:8000/length/">length</a></button>'''
#     html3 = '''<button><a href="http://127.0.0.1:8000/trim/">trim</a></button>'''
#     html4 = '''<button><a href="http://127.0.0.1:8000/stylize/">stylize</a></button>'''
#     html5 = '''<button><a href="http://127.0.0.1:8000/removepunc/">removepunc</a></button>'''
#     final = s + html1 + html2 + html3 + htmlt4 + html5
#     return HttpResponse(final)

# def index(request):
#     return render(request, 'temp.html')


def index(request):
    return render(request, "index.html")


def capitalize(s):
    return s.upper()


def trim(s):
    return s.strip()


def removepunc(s):
    res = ""
    for i in range(len(s)):
        if s[i] in string.punctuation:
            continue
        else:
            res = res + s[i]
    return res


def remove_extra_lines(s):
    res = ""
    for i in range(len(s)):
        if s[i] != "\n" and s[i] != "\r":
            res = res + s[i]
        else:
            continue
    return res


def resp(s):
    res = ""
    s = trim(s)
    for i in range(len(s) - 1):
        if not (s[i] == " " and s[i + 1] == " "):
            res = res + s[i]
        else:
            continue
    if s[len(s) - 1] != " ":
        res = res + s[len(s) - 1]
    return res


def analyze(request):
    text = request.POST.get("input", "default")
    print(text)
    rp_val = True if (request.POST.get("removepunc", "off")) == "on" else False
    cp_val = True if (request.POST.get("capitalize", "off")) == "on" else False
    trim_val = True if (request.POST.get("trim", "off")) == "on" else False
    rel_val = True if (request.POST.get("rel", "off")) == "on" else False
    resp_val = True if (request.POST.get("resp", "off")) == "on" else False
    res = text
    if rp_val:
        res = removepunc(res)
    if cp_val:
        res = capitalize(res)
    if trim_val:
        res = trim(res)
    if rel_val:
        res = remove_extra_lines(res)
    if resp_val:
        res = resp(res)
    dict = {"text": res, "len": len(res)}
    return render(request, "analyze.html", dict)
