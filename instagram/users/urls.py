from django.urls import path
from . import views

# from instagram.users.views import (
#     user_list_view,
#     user_redirect_view,
#     user_update_view,
#     user_detail_view,
# )

app_name = "users"
urlpatterns = [
    path("explore/", view=views.ExploreUsers.as_view(), name="explore_users"),
    path("<int:id>/follow/", view=views.FollowUser.as_view(), name="follow_users"),
    path("<int:id>/unfollow/", view=views.UnFollowUser.as_view(), name="un_follow_users"),
    path("<username>/followers/", view=views.UserFollowers.as_view(), name="user_followers"),
    path("<username>/following/", view=views.UserFollowing.as_view(), name="user_following"),
    path("search/", view=views.Search.as_view(), name="search"),
    path("<username>/", view=views.UserProfile.as_view(), name="user_profile"),
    path("<username>/password/", view=views.ChangePassword.as_view(), name="change_password"),
    path("login/facebook/", view=views.FacebookLogin.as_view(), name="fb_login"),
]
