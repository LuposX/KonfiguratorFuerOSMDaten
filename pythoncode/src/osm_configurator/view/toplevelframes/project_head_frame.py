from src.osm_configurator.view.states.state_manager import StateManager
from src.osm_configurator.control.control_interface import IControl
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class ProjectHeadFrame(TopLevelFrame):
    """
    This Frame shows the Header-PipeLine of the Application, when a Project os open.
    From there the User can:
    - Exit back to the MainMenu
    - Save the Project
    - Go to the Settings
    - Change between different Frames to edit Configurations
    - Use the Exports

    This Frame is always on the Top of the Window, below it will be presented a Frame to edit some part of the Project
    and below that Frame will be a FootFrame.
    Exceptions are the MainMenu and the Creation of a new Project, those won't have this Header on top of them.
    """

    def __init__(self, state_manager, control):
        """
        This Method Creates a ProjectHeadFrame, that lets the User Navigate the PipleLine directly and exit back to the
        MainMenu, as well giving the option to open the Options, saving the Project or letting the User use the
        Exports.

        Args:
            state_manager (StateManager): The StateManager the Frame will call, when it wants to change to
            another State.
            control (IControl): The Control the Frame will call, to get access to the Model.
        """
        super().__init__(state_manager, control)
        pass
