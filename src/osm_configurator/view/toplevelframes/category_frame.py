from __future__ import annotations

import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.category_controller_interface
import src.osm_configurator.view.constants.frame_constants as frame_constants_i
import src.osm_configurator.view.constants.scrollbar_constants as scrollbar_constants_i
import src.osm_configurator.view.constants.label_constants as label_constants_i

import customtkinter

from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Final
    from src.osm_configurator.view.states.state_manager import StateManager
    from src.osm_configurator.control.category_controller_interface import ICategoryController

# Final Variables
ELEMENT_BORDER_DISTANCE: Final = 10


class CategoryFrame(TopLevelFrame):
    """
    This frame lets the user create, delete and edit categories.
    It shows the name of a category, as well as their black- and white-List.
    Categories also can be turned on and off with Checkboxes.
    There will also be key-recommendations be shown for the black- and white-List.
    """

    def __init__(self, state_manager: StateManager, category_controller: ICategoryController):
        """
        This method creates an CategoryFrame so the user can create, delete and edit categories.

        Args:
            state_manager (state_manager.StateManager): The StateManager the frame will call, when it wants to change to another state.
            category_controller (category_controller.CategoryController): Respective controller
        """
        # Starting with no master
        # Also setting other settings
        super().__init__(master=None,
                         width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value,
                         height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value,
                         corner_radius=frame_constants_i.FrameConstants.FRAME_CORNER_RADIUS.value,
                         fg_color=frame_constants_i.FrameConstants.MIDDLE_FRAME_FG_COLOR.value)

        # Private Attributes
        self._state_manager = state_manager
        self._category_controller = category_controller

        # Making the grid
        # The grid is a 3x3 grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # The grid is made up by smaller frames
        # CategoryMenu
        category_menu_frame = customtkinter.CTkFrame(master=self,
                                                     width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value,
                                                     height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value/3,
                                                     corner_radius=frame_constants_i.FrameConstants.FRAME_CORNER_RADIUS.value,
                                                     fg_color=frame_constants_i.FrameConstants.MIDDLE_FRAME_FG_COLOR.value)
        category_menu_frame.grid(row=0, column=0, rowspan=1, columnspan=3)
        # This frame also has a grid
        # It is a 2x2 grid, where the second column row is heavier weightet
        category_menu_frame.grid_columnconfigure(0, weight=1)
        category_menu_frame.grid_columnconfigure(1, weight=4)
        category_menu_frame.grid_rowconfigure(0, weight=1)
        category_menu_frame.grid_rowconfigure(1, weight=1)
        # Making the Labels for the Frame
        choose_categories_label = customtkinter.CTkLabel(master=category_menu_frame,
                                                         width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value/5,
                                                         height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value/6 - ELEMENT_BORDER_DISTANCE,
                                                         corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                                         fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                                         text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                                         anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                                         padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADX.value,
                                                         pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADY.value,
                                                         text="Choose Categories")
        choose_categories_label.grid(row=0, column=0, rowspan=1, columnspan=1)

        # CategoryNameLabel
        category_name_label = customtkinter.CTkLabel(master=category_menu_frame,
                                                         width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value/5,
                                                         height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value/6 - ELEMENT_BORDER_DISTANCE,
                                                         corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                                         fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                                         text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                                         anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                                         padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADX.value,
                                                         pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADY.value,
                                                         text="Category Name")
        category_name_label.grid(row=1, column=0, rowspan=1, columnspan=1)

        #Making the



        # WhiteListFrame
        white_list_frame = customtkinter.CTkFrame(master=self,
                                                  width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value/3,
                                                     height=(frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value/3)*2,
                                                     corner_radius=frame_constants_i.FrameConstants.FRAME_CORNER_RADIUS.value,
                                                     fg_color=frame_constants_i.FrameConstants.MIDDLE_FRAME_FG_COLOR.value)
        # For the WhiteListFrame Frame is no grid needed, it only has one element in it



        # BlackListFrame
        black_list_frame = customtkinter.CTkFrame(master=self,
                                                     width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value/3,
                                                     height=(frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value/3)*2,
                                                     corner_radius=frame_constants_i.FrameConstants.FRAME_CORNER_RADIUS.value,
                                                     fg_color=frame_constants_i.FrameConstants.MIDDLE_FRAME_FG_COLOR.value)
        # The BlackListFrame, also needs no grid for only one element



        # RecommenderFrame
        # This is a scrollable Frame
        recommender_frame = customtkinter.CTkScrollableFrame(master=self,
                                                             width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value/3,
                                                             height=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value/3,
                                                             corner_radius=scrollbar_constants_i.ScrollbarConstants.SCROLLBAR_CORNER_RADIUS.value,
                                                             fg_color=scrollbar_constants_i.ScrollbarConstants.SCROLLBAR_FG_COLOR.value)
        # RecommenderFrame doesn't need a grid, it will have its buttons be stacked upon



        # CreateDeleteFrame
        create_delete_frame = customtkinter.CTkFrame(master=self,
                                                     width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value/3,
                                                     height=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value/3,
                                                     corner_radius=frame_constants_i.FrameConstants.FRAME_CORNER_RADIUS.value,
                                                     fg_color=frame_constants_i.FrameConstants.MIDDLE_FRAME_FG_COLOR.value)
        # THid Frame has a small, 1x2 grid
        create_delete_frame.grid_columnconfigure(0, weight=1)
        create_delete_frame.grid_rowconfigure(0, weight=1)
        create_delete_frame.grid_rowconfigure(1, weight=1)

    def activate(self):
        pass
