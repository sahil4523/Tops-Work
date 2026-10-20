from insta_utils.likes import like_count
from insta_utils.comments import comment_count

likes = 100
comments = 20

likes = like_count(likes, 1)
comments = comment_count(comments, 2)

print("Total likes:", likes)
print("Total comments:", comments)