from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib import messages
from django.core.mail import send_mail
from django.http import Http404, HttpResponse, HttpResponseForbidden
from django.template.loader import get_template
from django.template import Context
from forms import *
from models import *
from score_functions import *
import globalgamejam13.settings as settings

def game_join(request):
    if request.method == 'POST': 
        form = JoinGameForm(request.POST) 
        if form.is_valid(): 
            try:
                game = Game.objects.get(
                    host__name = form.cleaned_data['host_name'],
                    password = form.cleaned_data['password']
                )
            except:
                return HttpResponse("invalid game_id")
            if game.password == form.cleaned_data['password']:
                try:
                    player = Player()
                    player.name = form.cleaned_data['player_name']
                    player.game = game
                    player.save()
                except:
                    return HttpResponse("duplicate player")
                return HttpResponse()
            else:
                return HttpResponse("wrong password")
    else:
        form = JoinGameForm() 

    return render_to_response('form.html', 
            {"form" : form}, context_instance=RequestContext(request)
    )

def game_list(request):
    games = Game.objects.filter(round = 0)
    return render_to_response('game_list.html', {
        "games": games
        }, context_instance=RequestContext(request),
        mimetype = 'text/plain'
    )

def game_new(request):
    if request.method == 'POST': 
        form = NewGameForm(request.POST) 
        if form.is_valid(): 
            player = Player()
            player.name = form.cleaned_data['player_name']
            player.save()
            game = Game()
            game.host = player
            game.password = form.cleaned_data['password']
            game.save()

            player.game = game
            player.save()
            return HttpResponse(game.id, mimetype = "text/plain")
    else:
        form = NewGameForm() 

    return render_to_response('form.html', 
            {"form" : form}, context_instance=RequestContext(request)
    )

def game_round(request):
    if request.method == 'POST': 
        form = RoundForm(request.POST) 
        if form.is_valid(): 
            try:
                game = Game.objects.get(id = form.cleaned_data['game_id'])
            except:
                return HttpResponse("invalid game_id")

            if game.round == settings.NUMBER_ROUNDS:
                final_score(players, game)
            else:
                game.round += 1
                game.save()
            return HttpResponse()
    else:
        form = RoundForm() 

    return render_to_response('form.html', 
            {"form" : form}, context_instance=RequestContext(request)
    )

def game_set_bpm(request):
    if request.method == 'POST': 
        form = SetBPMForm(request.POST) 
        if form.is_valid(): 
            try:
                game = Game.objects.get(id = form.cleaned_data['game_id'])
            except:
                return HttpResponse("invalid game_id")
            try:
                player = game.players.get(name = form.cleaned_data['player_name'])
            except:
                return HttpResponse("invalid player")
            if game.round == 0:
                return HttpResponse("round not started")
            pbpm = getattr(player, "round_%s_bpm"%game.round)
            #if pbpm == None:
                
            setattr(player, "round_%s_bpm"%game.round, form.cleaned_data['bpm'])
            player.save()
            players = game.players.all()

            for player in players:
                if getattr(player, "round_%s_bpm"%game.round) == None:
                    break
            else:
                if game.round == settings.NUMBER_ROUNDS:
                    final_score(players, game)
                else:
                    round_score(players, game)
                    game.round += 1
                    game.save()
            return HttpResponse()
    else:
        form = SetBPMForm() 

    return render_to_response('form.html', 
            {"form" : form}, context_instance=RequestContext(request)
    )
    
def game_set_master_bpm(request):
    if request.method == 'POST': 
        form = SetMasterBPMForm(request.POST) 
        if form.is_valid(): 
            try:
                game = Game.objects.get(id = form.cleaned_data['game_id'])
            except:
                return HttpResponse("invalid game_id")
            game.master_bpm = form.cleaned_data['bpm']
            game.save()
            return HttpResponse()
    else:
        form = SetMasterBPMForm() 

    return render_to_response('form.html', 
            {"form" : form}, context_instance=RequestContext(request)
    )

def game_score(request, game_id):
    try:
        game = Game.objects.get(id = game_id)
    except:
        return HttpResponse("invalid game_id")
    players = game.players.all().order_by("-score")
    return render_to_response('game_scores.html', {
        "players": players
        }, context_instance=RequestContext(request),
        mimetype = 'text/plain'
    )
