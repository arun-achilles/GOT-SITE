import got
import fresh_tomatoes
stark=got.Got("House Stark",
              "https://www.redwolf.in/image/catalog/artwork-Images/mens/house-stark-design-india-2.png",
              "https://www.youtube.com/watch?v=Wm0ikHOkGOY")
lannisters=got.Got("House Lannisters",
              "https://i.ytimg.com/vi/ZSoCnehpi78/maxresdefault.jpg",
              "https://www.youtube.com/watch?v=iYBpC3JeM0Y")
list=[stark,lannisters]
fresh_tomatoes.open_movies_page(list)

