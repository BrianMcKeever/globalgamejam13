from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from globalgamejam13.game.views import *

urlpatterns = patterns('',
    url(r'^new$', game_new), 
    url(r'^new/$', game_new), 
    url(r'^list/$', game_list), 
    url(r'^join$', game_join), 
    url(r'^join/$', game_join), 
    url(r'^round$', game_round), 
    url(r'^round/$', game_round), 
    url(r'^set/bpm$', game_set_bpm), 
    url(r'^set/bpm/$', game_set_bpm), 
    url(r'^set/master$', game_set_master_bpm), 
    url(r'^set/master/$', game_set_master_bpm), 
    url(r'^(?P<game_id>\d+)/score/$', game_score, name = 'game_score'), 
)

