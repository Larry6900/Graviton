from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from time import sleep
import json
import googleapiclient.discovery
from bardapi import Bard
import os
from tempfile import TemporaryFile
from pyudemy import Udemy
from youtubesearchpython import VideosSearch

def scrapeSite(path):
    steps = []
    # Replace XXXX with the values you get from __Secure-1PSID
    os.environ['_BARD_API_KEY'] = "YQhxb9EdlRGMKGLoiNKEenNZrXZCXWOBM8Q_SqQfuNj-Uqj94RlyEL6bKfbxmzX6wNhmow."
    # Set your input text
    input_text = f'Generate a list to learn {path}. Each list item should start with a number. There should be at more 20 list items. Do not create sub lists under each list item, instead add them to the main list. Each list item should be less than 6 words and should start with the word "how to learn". include the word {path} in each list item. Each step should include a quantative skill that can be developed.Do not mention hours required for each list item'
    # Send an API request and get a respons
    bard_output = Bard().get_answer(input_text)['content']
    bard_output = bard_output.replace("*", "")
    bard_output = bard_output.replace("Step", "")
    bard_output = bard_output.replace("`", "")
    fp = TemporaryFile('w+t')
    fp.write(bard_output)
    fp.seek(0)
    for lines in fp:
        lines = lines.strip()
        if lines and lines[0].isdigit():
            steps.append(lines)
    print(steps)
    return steps

def trim_string(s: str, max_words: int) -> str:
    words = s.split()
    if len(words) > max_words:
        return ' '.join(words[:max_words]) + '...'
    else:
        return s

# Example usage
def searchyt(prompt, data):
    youtubeurl = []
    youtubetitle = []
    youtubethumbnail = []
    for item in data:
        query = f'{item} reagrding {prompt} in english'
        videosSearch = VideosSearch(query, limit=1)
        result = videosSearch.result()
        video = result['result'][0]
        video_id = video['id']
        video_title = video['title']
        video_title = trim_string(video_title,5)
        video_thumbnail = video['thumbnails'][0]['url']
        youtubeurl.append(f"https://youtu.be/{video_id}")
        youtubetitle.append(video_title)
        youtubethumbnail.append(video_thumbnail)
    return youtubeurl,youtubetitle,youtubethumbnail

def searchudemy(prompt,data):
    udemyurl = []
    udemytitle = []
    udemythumbnail = []
    for item in data:
        # Authenticate with your client ID and client secret
        udemy = Udemy("TmyXWS16rtIEO6WhPS2i7vPzQSPpeJBpxzIR2paw", "cphOjrGbDH7jKhMVAFYual7p0XTM0xp2QZKK1RuBxQFojhAkaeY7J7qG8Q05WhEZYWgWE3ccCl7PE9mOG8Ygon5mx033GS9qBiCg5o8x7tPrZY638NJ8R6KHT4HASALS")

        # Search for JavaScript courses
        courses = udemy.courses(search=item + prompt)
        course = courses['results'][0]
        # Print the course titlestitle = course['title']
        # Get the course title, URL, and thumbnail
        title = course['title']
        title = trim_string(title,5)
        url = course['url']
        thumbnail = course['image_480x270']
        url = "https://www.udemy.com"+ url
        udemyurl.append(url)
        udemytitle.append(title)
        udemythumbnail.append(thumbnail)
    return udemyurl,udemythumbnail,udemytitle

def about(request):
    return render(request,'about.html')

def home(request):
    return render(request, 'index.html')

def generate(request):
    return render(request, 'generate.html')

def result(request):
    loopnum=0
    data = []
    yttitle  = []
    ytthumbnail = [] 
    yturl = []
    udurl = []
    udtitle = []
    udthumbnail = []
    
    if request.method == 'POST':
        prompt = request.POST['pathway']
        youtube = request.POST.get('youtube')
        udemy = request.POST.get('udemy')
    
    # Uses the user's prompt to generate the roadmap
    data = scrapeSite(prompt)
    """ if prompt[0] == "C": #For c# prompt
        data = ['How to install Visual Studio.', 'How to create a new C# project.', 'How to write a simple C# program.', 'How to use variables in C#.', 'How to use loops in C#.', 'How to use functions in C#.', 'How to use classes in C#.', 'How to use interfaces in C#.', 'How to use generics in C#.', 'How to use asynchronous programming in C#.', 'How to use dependency injection in C#.', 'How to use unit testing in C#.', 'How to deploy a C# application.', 'How to use the .NET Framework eith C#.', 'How to use the .NET Core Framework with C#.', 'How to use ASP.NET with C#.', 'How to use Entity Framework with C#.', 'How to use LINQ with C#.', 'How to use XML with C#.', 'How to use JSON with C#.', 'How to use web services with C#.', 'How to use APIs with C#.', 'How to use databases with C#.', 'Code Securtiy with C#.', 'How To Debug C# code', 'How to use profiling in C#.', 'How to use version control.', 'How to work with teams.', 'How to contribute to open source projects.', 'How to get a job as a C# developer.', 'How to continue learning C#.']
    elif prompt[0] == "O": #How to learn origami 
        data =['How to find a good origami paper.', 'How to fold a basic crease.', 'How to fold a square into a triangle.', 'How to fold a waterbomb base.', 'How to fold a crane.', 'How to fold a frog.', 'How to fold a boat.', 'How to fold a house.', 'How to fold a flower.', 'How to fold a heart.', 'How to fold a more complex model.', 'How to fold a modular origami model.', 'How to fold an origami sculpture.', 'How to fold an origami tessellation.', 'How to fold an origami garment.', 'How to fold an origami animal.', 'How to fold an origami plant.', 'How to fold an origami object.', 'How to fold an origami food.', 'How to fold an origami costume.', 'How to learn more about origami.', 'How to find origami tutorials.', 'How to join an origami club.', 'How to attend an origami workshop.', 'How to read origami books.', 'How to watch origami videos.', 'How to participate in origami competitions.', 'How to share your origami creations.', 'How to teach origami to others.', 'How to become an origami artist.']
     """
    if youtube == "youtubego":
        yturl,yttitle, ytthumbnail = searchyt(prompt, data)
    
    if udemy == "udemygo":
         udurl,udtitle,udthumbnail = searchudemy(prompt,data)
    
    ud_data= zip(udurl,udtitle,udthumbnail)
    yt_data= zip(yturl,yttitle,ytthumbnail)
    roadmap_data = zip(data)
    loopnum = len(data)
    context = {
        'ud_data': ud_data,
        'yt_data': yt_data,
        'steps':roadmap_data,
        'title': prompt,
    }
    return render(request, 'result.html', context)

def stuff(request):
    return render(request, 'result.html')