from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "midnight.jpg",
        "author": "Samara",
        "date": date(2022, 11, 10),
        "title": "Midnights",
        "excerpt": "Midnights is the tenth studio album by American singer Taylor Swift, released on October 21, 2022 through Republic Records. Announced at the 2022 MTV Video Music Awards, the album marks Swift's first new work since her ninth studio album Evermore.",
        "content": """
            Taylor Swift released her tenth studio album this Friday (21st). "Midnights" has thirteen tracks, written and
            produced alongside Jack Antonoff and also a participation of Lana Del Rey in one of the songs. 
            
            Taylor Swift released her tenth studio album this Friday (21st). "Midnights" has thirteen tracks, written and
            produced alongside Jack Antonoff and also a participation of Lana Del Rey in one of the songs.
            
            Taylor Swift released her tenth studio album this Friday (21st). "Midnights" has thirteen tracks, written and
            produced alongside Jack Antonoff and also a participation of Lana Del Rey in one of the songs.     
        """
    }
    {
        "slug": "the-weeknd",
        "image": "coding.jpg",
        "author": "Samara",
        "date": date(2022, 3, 10),
        "title": "The Weeknd breaks own record and makes history with current tour",
        "excerpt": "According to new box office figures for the tour, revealed this week, The Weeknd has become the highest-grossing black artist at a single show in history.",
        "content": """
          It is worth mentioning that the title of black artist with the highest grossing in a single show in history
          has belonged to the singer since July, when he amassed an incredible $9.890 million after performing at MetLife
          Stadium in East Rutherford. With this performance in Los Angeles, the Canadian broke his own record and left
          his name in history!

          Despite having announced before hitting the road that he would visit different continents with the
          “AFTER HOURS TIL DAWN Tour”, including South America, no new tour dates have been revealed so far. There is a
          rumor that The Weeknd will come to Brazil for two shows in March next year, but the information has not been
          confirmed by his team or any producer.
        """
    },
    {
        "slug": "ariana-grande",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "Ariana Grande enters studio with Adele and Taylor Swift producers",
        "excerpt": "Ariana Grande is away from the music scene to record the film 'Wicked', where she will play the character "Glinda". However, it looks like there's news about it, as she's been seen in the studio!",
        "content": """
          O mais provável é que ela esteja gravando músicas para a trilha sonora de “Wicked”, visto o histórico dos
          produtores. Vale ressaltar que Ariana Grande deixou claro que está focada na produção, já que é um sonho de
          infância. Do que se trata de um novo álbum pop, deve demorar mais um pouco.
          
        """
    }
]

def get_date(post):
    return post['date']


# Create your views here.



def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
  return render(request, "blog/all-posts.html")

def post_detail(request, slug):
  return render(request, "blog/post-detail.html")