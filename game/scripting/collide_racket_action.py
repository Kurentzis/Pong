from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideRacketAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        stats = cast.get_first_actor(STATS_GROUP)
        ball = cast.get_first_actor(BALL_GROUP)
        racket1 = cast.get_first_actor(RACKET_GROUP)
        racket2 = cast.get_last_actor(RACKET_GROUP)

        ball_body = ball.get_body()
        racket_body = racket1.get_body()
        racket_body2 = racket2.get_body()

        if self._physics_service.has_collided(ball_body, racket_body):
            ball.bounce_y()
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)
            stats.add_points(10)
            



        if self._physics_service.has_collided(ball_body, racket_body2):
            ball.bounce_y()
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)
            stats.add_points(10)