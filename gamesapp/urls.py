from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^game/(?P<game_id>[^/]+)$', views.game_view),
    url(r'^api/games/$', views.games),
    url(r'^api/games/(?P<game_id>[^/]+)/$', views.game),
    url(r'^api/highscores/$', views.highscores),
    url(r'^api/highscores/(?P<game_id>[^/]+)/$', views.highscore_game),
    url(r'^api/highscores/(?P<game_id>[^/]+)/(?P<user_id>[^/]+)/$', views.highscore_game_user),
    url(r'^api/highscore/(?P<id>[^/]+)/$', views.highscore_id),
    url(r'^api/user/register/$', views.register_user),
    url(r'^api/user/login/$', views.login_user),
    url(r'^api/user/logout/$', views.logout_user),
]
