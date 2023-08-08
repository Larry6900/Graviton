""" from pyudemy import Udemy

# Authenticate with your client ID and client secret
udemy = Udemy("TmyXWS16rtIEO6WhPS2i7vPzQSPpeJBpxzIR2paw", "cphOjrGbDH7jKhMVAFYual7p0XTM0xp2QZKK1RuBxQFojhAkaeY7J7qG8Q05WhEZYWgWE3ccCl7PE9mOG8Ygon5mx033GS9qBiCg5o8x7tPrZY638NJ8R6KHT4HASALS")

# Search for JavaScript courses
courses = udemy.courses(search='javascript')
course = courses['results'][0]
# Print the course titlestitle = course['title']
# Get the course title, URL, and thumbnail
title = course['title']
url = course['url']
thumbnail = course['image_480x270']
url = f"https://www.udemy.com{url}"
print(f"Title: {title}")
print(f"URL: {url}")
print(f"Thumbnail: {thumbnail}") """
""" roadmap = []
for i in range(31):
    step = input(f"Enter step {i}: ")
    roadmap.append(step)
print (roadmap) """
pathway = input("Enter Pathway: ")
if pathway[0] == "H": #For c# prompt
        data = ['How to install Visual Studio.', 'How to create a new C# project.', 'How to write a simple C# program.', 'How to use variables in C#.', 'How to use loops in C#.', 'How to use functions in C#.', 'How to use classes in C#.', 'How to use interfaces in C#.', 'How to use generics in C#.', 'How to use asynchronous programming in C#.', 'How to use dependency injection in C#.', 'How to use unit testing in C#.', 'How to deploy a C# application.', 'How to use the .NET Framework.', 'How to use the .NET Core Framework.', 'How to use ASP.NET.', 'How to use Entity Framework.', 'How to use LINQ.', 'How to use XML.', 'How to use JSON.', 'How to use web services.', 'How to use APIs.', 'How to use databases.', 'How to use security.', 'How to use debugging.', 'How to use profiling.', 'How to use version control.', 'How to work with teams.', 'How to contribute to open source projects.', 'How to get a job as a C# developer.', 'How to continue learning C#.']
elif pathway[0] == "h": #How to learn origami 
        data =['How to find a good origami paper.', 'How to fold a basic crease.', 'How to fold a square into a triangle.', 'How to fold a waterbomb base.', 'How to fold a crane.', 'How to fold a frog.', 'How to fold a boat.', 'How to fold a house.', 'How to fold a flower.', 'How to fold a heart.', 'How to fold a more complex model.', 'How to fold a modular origami model.', 'How to fold an origami sculpture.', 'How to fold an origami tessellation.', 'How to fold an origami garment.', 'How to fold an origami animal.', 'How to fold an origami plant.', 'How to fold an origami object.', 'How to fold an origami food.', 'How to fold an origami costume.', 'How to learn more about origami.', 'How to find origami tutorials.', 'How to join an origami club.', 'How to attend an origami workshop.', 'How to read origami books.', 'How to watch origami videos.', 'How to participate in origami competitions.', 'How to share your origami creations.', 'How to teach origami to others.', 'How to become an origami artist.']

print(data)