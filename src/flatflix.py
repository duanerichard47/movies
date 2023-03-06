class Movie:
    def __init__(self, title):
        self.title = title
        
        self.reviews =[]
        self.viewers =[]

    def get_title(self):
        return self.title

    def get_reviews(self):
        array =[]
        for review in self.reviews:
            array.append(review)
        return array
    

    def get_viewers(self):
        array =[]
        for view in self.reviews:
            array.append(view.viewer)
        return array
 

    def average_rating(self):
        tot =0
        for rate in self.reviews:
            tot=+ rate.rating  
        return tot/len(self.reviews)

    def highest_review(self):
        highest =self.reviews[0]
        for review in self.reviews:
          if highest.rating < review.rating:
                 highest = review
        return highest


class Viewer:
    def __init__(self, username):
        self.username = username
        self.reviews =[]
        self.movie =[]

    def get_username(self):
        return self.username
    #
    def get_reviews(self):
        # array = []
        # for review in self.reviews:
        #     array.append(review.viewer) returning list of viewers not reviews
        # return array
        return self.reviews
    #


    def get_movies(self):
        array = []
        for review in self.reviews:
            array.append(review.movie)
        return array


        #
    def has_reviewed(self, movie):
        # if movie in self.reviews:  method can not drill down to find movie in instance
        #     return True
        if movie in self.get_movies():
            return True
       
        #

    def rate_movie(self, movie, rating):
        new_review = Review(self, movie, rating)
        self.reviews.append(new_review)
        return len(self.reviews)



class Review:
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating
        

    def get_rating(self):
        return self.rating

    def get_viewer(self):
        return self.viewer

    def get_movie(self):
        return self.movie



