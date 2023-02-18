from __future__ import annotations

from functools import partial

import customtkinter

from PIL import Image

import src.osm_configurator.model.project.configuration.category as category_i
import src.osm_configurator.model.project.configuration.default_value_entry as default_value_entry_i
import src.osm_configurator.view.popups.alert_pop_up as alert_pop_up_i

import src.osm_configurator.view.constants.frame_constants as frame_constants_i
import src.osm_configurator.view.constants.button_constants as button_constants_i

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from typing import Final
    from src.osm_configurator.view.utilityframes.reduction_default_value_frame import ReductionDefaultValueFrame

# Finals
UP_ARROW_SIZE: Final = 10
DOWN_ARROW_SIZE: Final = 10
PADX: Final = 2
PADY: Final = 2
ELEMENT_BORDER_DISTANCE: Final = 4

ENTRY_BUTTON_HEIGHT: Final = 44
ARROW_BUTTON_HEIGHT: Final = 20


class TagListPriorityFrame(customtkinter.CTkScrollableFrame):
    """
    This frame shows all the default values of a category, listed in priority.
    The higher an entry is, the lower its priority is.
    There will always be one not deletable DEFAULT-entry at the top of the list, always having the lowest priority,
    that also can't be moved.
    """

    def __init__(self, parent: ReductionDefaultValueFrame, width: int, height: int):
        """
        This method will create a TagListPriorityFrame, showing a list of default value entries from the given category,
        ordered in, low on top, to high on bottom priorities.

        Args:
            parent (ReductionDefaultValueFrame): The parent frame of this frame
            width (int): The width of this frame
            height (int): The height of this frame
        """
        super().__init__(master=parent,
                         width=width,
                         height=height,
                         corner_radius=frame_constants_i.FrameConstants.FRAME_CORNER_RADIUS.value,
                         fg_color=frame_constants_i.FrameConstants.SUB_FRAME_FG_COLOR.value)

        # Setting private Attributes
        self._parent: ReductionDefaultValueFrame = parent
        self._width: int = width
        self._height: int = height

        self._selected_category: category_i.Category = None
        self._selected_entry: default_value_entry_i.DefaultValueEntry = None

        self._selected_button_id: int = 0

        self._entries: [default_value_entry_i.DefaultValueEntry] = []

        # The images used for moving entries up and down
        self._up_arrow_image = customtkinter.CTkImage(light_image=Image.open("HERE PATH!!!!"),
                                                      dark_image=Image.open("HERE PATH!!!!"),
                                                      size=(UP_ARROW_SIZE, UP_ARROW_SIZE))

        self._down_arrow_image = customtkinter.CTkImage(light_image=Image.open("HERE PATH!!!!"),
                                                        dark_image=Image.open("HERE PATH!!!!"),
                                                        size=(DOWN_ARROW_SIZE, DOWN_ARROW_SIZE))

        # The different List for all the Buttons
        self._entry_button_list: [customtkinter.CTkButton] = []
        self._up_button_list: [customtkinter.CTkButton] = []
        self._down_button_list: [customtkinter.CTkButton] = []

        # Making the grid
        # Only the Columns are defined, since on rows will be stacked upon
        self.grid_columnconfigure(0, weight=4)
        self.grid_columnconfigure(1, weight=1)

    def load_category(self, category: category_i.Category | None,
                      entry: default_value_entry_i.DefaultValueEntry | None) -> bool:
        """
        Loads in all the default value entries of the given category into the frame, so their priority can be edited.

        Args:
            category (category.Category): The category the default value entries will be loaded from and edited upon
            entry (default_value_entry.DefaultValueEntry | None): A default value entry, that shall be loaded directly, can be None, to not load a specific entry directly

        Returns:
            bool: True if category was successfully loaded, else False
        """
        # First deleting everything on the Frame
        entry_button: customtkinter.CTkButton
        for entry_button in self._entry_button_list:
            entry_button.destroy()
        self._entry_button_list: [customtkinter.CTkButton] = []

        up_button: customtkinter.CTkButton
        for up_button in self._up_button_list:
            up_button.destroy()
        self._up_button_list: [customtkinter.CTkButton] = []

        down_button: customtkinter.CTkButton
        for down_button in self._down_button_list:
            down_button.destroy()
        self._down_button_list: [customtkinter.CTkButton] = []

        # Now setting up for new entries, if the selected category si none, then just the frame was emptied
        if category is not None:
            # This list will always have at least one entry! (The DEFAULT-Entry!)
            self._selected_category: category_i.Category = category
            self._entries: [default_value_entry_i.DefaultValueEntry] = self._selected_category.get_default_value_list()

            new_entry: default_value_entry_i.DefaultValueEntry
            for new_entry in self._entries:
                self._add_entry_to_list(new_entry)

            # If there is a specific entry given, it will be loaded directly, otherwise, the first entry is loaded
            if entry is not None:
                self._selected_entry: default_value_entry_i.DefaultValueEntry = entry
            else:
                self._selected_entry: default_value_entry_i.DefaultValueEntry = self._entries[0]

            # Determing, what button corrosponds to the entry
            e: default_value_entry_i.DefaultValueEntry
            entry_id: int = 0
            for e in self._entries:
                if e == self._selected_entry:
                    break
                entry_id += 1

            # Now disabling all "bad" arrow buttons, such as the 2 atn the default value, the down on the 2nd entry,
            # and the up on the last entry
            self._up_button_list[0].configure(state="disabled",
                                              fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DISABLED.value)
            self._down_button_list[0].configure(state="disabled",
                                                fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DISABLED.value)

            if len(self._up_button_list) > 1:
                self._up_button_list[len(self._up_button_list) - 1].configure(state="disabled",
                                                                              fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DISABLED.value)

            if len(self._down_button_list) > 1:
                self._down_button_list[len(self._down_button_list) - 1].configure(state="disabled",
                                                                                  fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DISABLED.value)

            # Pretending the corrosponding button was pressed
            self._entry_button_pressed(entry_id)

        # category is loaded
        return True

    def _up_button_pressed(self, button_id: int):

        if self._selected_category.move_default_value_entry_up(self._entries[button_id]):
            # If it was successfully moved, we move it in the frame aswell
            # Only the Entry Button needs to be moved, since up and down buttosn are everywhere and only
            # corrospond to the entries through their id, so change id of button, change partners

            # The Button above
            entry_button: customtkinter.CTkButton = self._entry_button_list[button_id - 1]
            # Swapping the buttons on the list
            self._entry_button_list[button_id - 1] = self._entry_button_list[button_id]
            self._entry_button_list[button_id] = entry_button
            # Swapping the buttons on the Frame
            # (they are swapped in list so just give them their new position, that is the position in the List)
            self._entry_button_list[button_id].grid(row=button_id, column=0, rowspan=2, columnspan=1, padx=PADX,
                                                    pady=PADY)
            self._entry_button_list[button_id - 1].grid(row=button_id - 1, column=0, rowspan=2, columnspan=1, padx=PADX,
                                                        pady=PADY)

            # refreshing the entries
            self._entries: [default_value_entry_i.DefaultValueEntry] = self._selected_category.get_default_value_list()
        else:
            alert_pop_up_i.AlertPopUp("Could not move Entry Up!")

    def _down_button_pressed(self, button_id: int):

        if self._selected_category.move_default_value_entry_down(self._entries[button_id]):
            # Move them first on the List
            # The Button below
            entry_button: customtkinter.CTkButton = self._entry_button_list[button_id + 1]
            # Swapping on list
            self._entry_button_list[button_id + 1] = self._entry_button_list[button_id]
            self._entry_button_list[button_id] = entry_button
            # Swapping buttons on Frame
            # (they are swapped in list so just give them their new position, that is the position in the List)
            self._entry_button_list[button_id].grid(row=button_id, column=0, rowspan=2, columnspan=1, padx=PADX,
                                                    pady=PADY)
            self._entry_button_list[button_id - 1].grid(row=button_id + 1, column=0, rowspan=2, columnspan=1, padx=PADX,
                                                        pady=PADY)

            # refreshing the entries
            self._entries: [default_value_entry_i.DefaultValueEntry] = self._selected_category.get_default_value_list()
        else:
            alert_pop_up_i.AlertPopUp("Could not move Entry Down!")

    def _entry_button_pressed(self, button_id: int):
        # First activating all buttons, so they don't end up all disabled
        button: customtkinter.CTkButton
        for button in self._entry_button_list:
            button.configure(state="normal", text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                             fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value)

        # Disabling the pressed button
        self._entry_button_list[button_id].configure(state="disabled",
                                                     text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR_DISABLED.value,
                                                     fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DISABLED.value)
        self._selected_button_id: int = button_id

        # telling parent what entry was pressed
        # since buttons and entries alling in theri id, we can just use the button_id to find it
        self._parent.load_entry(self._entries[button_id])

    def _add_entry_to_list(self, entry: default_value_entry_i.DefaultValueEntry):
        entry_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self,
                                                                        width=int(self._width * (
                                                                                4 / 5) - ELEMENT_BORDER_DISTANCE),
                                                                        height=ENTRY_BUTTON_HEIGHT,
                                                                        corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                                                        border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                                                        fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DELETE.value,
                                                                        hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR_DELETE.value,
                                                                        border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                                                        text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR_DELETE.value,
                                                                        text=entry.get_default_value_entry_tag(),
                                                                        command=partial(self._entry_button_pressed,
                                                                                        len(self._entry_button_list)))
        entry_button.grid(row=len(self._entry_button_list) * 2, column=0, rowspan=2, columnspan=1, padx=PADX, pady=PADY)

        up_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self,
                                                                     width=int(self._width * (
                                                                             1 / 5) - ELEMENT_BORDER_DISTANCE),
                                                                     height=ARROW_BUTTON_HEIGHT,
                                                                     corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                                                     border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                                                     fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DELETE.value,
                                                                     hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR_DELETE.value,
                                                                     border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                                                     text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR_DELETE.value,
                                                                     text=entry.get_default_value_entry_tag(),
                                                                     command=partial(self._up_button_pressed,
                                                                                     len(self._up_button_list)))
        up_button.grid(row=len(self._entry_button_list), column=1, rowspan=1, columnspan=1, padx=PADX, pady=PADY)

        down_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self,
                                                                       width=int(self._width * (
                                                                               1 / 5) - ELEMENT_BORDER_DISTANCE),
                                                                       height=ARROW_BUTTON_HEIGHT,
                                                                       corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                                                       border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                                                       fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DELETE.value,
                                                                       hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR_DELETE.value,
                                                                       border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                                                       text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR_DELETE.value,
                                                                       text=entry.get_default_value_entry_tag(),
                                                                       command=partial(self._down_button_pressed,
                                                                                       len(self._down_button_list)))
        down_button.grid(row=len(self._entry_button_list) + 1, column=1, rowspan=1, columnspan=1, padx=PADX, pady=PADY)

        self._entry_button_list.append(entry_button)
        self._up_button_list.append(up_button)
        self._down_button_list.append(down_button)

    def update_button(self, text: str) -> bool:
        """
        Method to update the text of the tag button, that is currently selected

        Args:
            text (str): The text that shall be seen on the currently selected button

        Returns:
            bool: True if text was changed successfully, False else
        """

        self._entry_button_list[self._selected_button_id].configure(text=text)
        return True
