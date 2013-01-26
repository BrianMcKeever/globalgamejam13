from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from globalgamejam13.game.views import *

urlpatterns = patterns('',
    url(r'^new/$', game_new, name = 'game_new'), 
    url(r'^list/$', game_list, name = 'game_list'), 
    url(r'^join/$', game_join, name = 'game_join'), 
    url(r'^set/bpm/$', game_set_bpm, name = 'game_set_bpm'), 
    url(r'^set/master/$', game_set_master_bpm, name = 'game_set_master_bpm'), 
    url(r'^(?P<game_id>\d+)/score/$', game_score, name = 'game_score'), 
)

