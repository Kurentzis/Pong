from constants import *
from game.casting.cast import Cast
from game.directing.scene_manager import SceneManager
from game.scripting.action_callback import ActionCallback
from game.scripting.script import Script


class Director(ActionCallback):
    """A person who directs the game."""

    def __init__(self, video_service):
        self._video_service = video_service
        self._cast = Cast()
        self._script = Script()
        self._scene_manager = SceneManager()
        
    def on_next(self, scene):
        self._scene_manager.prepare_scene(scene, self._cast, self._script)
        
    def start_game(self):
        """Starts the game. Runs the main game loop."""
        self.on_next(NEW_GAME)
        self._execute_actions(INITIALIZE)
        self._execute_actions(LOAD)
        while self._video_service.is_window_open():
            self._execute_actions(INPUT)
            self._execute_actions(UPDATE)
            self._execute_actions(OUTPUT)
        self._execute_actions(UNLOAD)
        self._execute_actions(RELEASE)
        
    def _execute_actions(self, group):
        actions = self._script.get_actions(group)    
        for action in actions:
            action.execute(self._cast, self._script, self)          