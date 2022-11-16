from datetime import date

from django.shortcuts import render

all_posts = [
    {
        "slug": "taylor",
        "image": "taylor.jpg",
        "author": "Samara",
        "date": date(2021, 7, 21),
        "title": "Anti-Hero",
        "excerpt": "Midnights: 'Anti-Hero' tops UK charts for third week in a row",
        "content": """
          The success of Midnights is so great that the singer managed to surpass a mark reached in 2017,
          when “Look What You Made Me Do” remained at the top of the list for two consecutive weeks. Despite
          the enormous popularity, Taylor Swift's project was displaced from the 1st place of the US charts,
          losing the top to Her Loss, Drake's new album and 21 Savage. The rap stars' collaborative album was
          released on November 4th.

          Despite not remaining at the top of the US charts, Taylor Swift remains one of the top names in the
          music industry. The singer became the number 1 artist on Spotify worldwide, that is, the blonde is the
          most listened to artist on the streaming platform. She achieved this feat, after becoming the singer with
          the most monthly listeners, with more than 79 million streams every month. It is worth remembering that,
          with the debut of Midnights, Taylor also became the most listened to artist in a single day on the platform,
          with more than 184 million reproductions
        """
    },
    {
        "slug": "the-weeknd",
        "image": "the-weeknd.jpg",
        "author": "Samara",
        "date": date(2022, 3, 10),
        "title": "Remove 'Trilogy' From The Streaming Service?",
        "excerpt": "The Weeknd considers pulling Trilogy (2012) from streaming services. The album is a compilation of his previously released mixtapes such as 'House Of Balloons', 'Thursday' and 'Echoes Of Silence'.",
        "content": """
          Abel Tesfaye, the artist's real name, asked his followers to listen to the works individually and recalled
          that the collection does not have the original mix of the projects.

          “If you want to hear the trilogy as it was meant to be heard… listen to House of Balloons, Thursday and Echoes
          of Silence individually. Not all samples are in the trilogy and the mix is ​​not the original mix”, wrote The Weeknd,
          who reinforced that “Trilogy” is not an album.
        """
    },
    {
        "slug": "ariana-grande",
        "image": "ariana-grande.jpg",
        "author": "Samara",
        "date": date(2020, 8, 5),
        "title": "Ariana Grande enters studio",
        "excerpt": "Ariana Grande is away from the music scene to shoot the movie “Wicked”, where she will play the character “Glinda“. However, there seems to be news regarding this as she has been spotted in the studio! ",
        "content": """
          This Monday (November 7th) she posted an update via Instagram “stories” in recording along with producers.

          In the image, she showed producers Greg Wells and Stephen Oremus. The former has recordings with Adele (One
          and Only), Taylor Swift (Beautiful Ghosts), among others. The other is specialized in musical shows including
          “Wicked” itself.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
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
    return render(request, "blog/all-posts.html", {
      "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
      "post": identified_post
    })
