


class MovieModel(db.Model, CRUDMixin):

    movie_name = db.Column(db.String(255))
    average_score = db.Column(db.Float)
    short_comment = db.Column(db.String(255))


