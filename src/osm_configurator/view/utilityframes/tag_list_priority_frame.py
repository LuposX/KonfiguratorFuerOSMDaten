from __future__ import annotations

from functools import partial

import customtkinter

from PIL import Image

import os

from definitions import PROJECT_DIR

import src.osm_configurator.model.project.configuration.category as category_i
import src.osm_configurator.model.project.configuration.default_value_entry as default_value_entry_i
import src.osm_configurator.view.popups.alert_pop_up as alert_pop_up_i

import src.osm_configurator.view.constants.frame_constants as frame_constants_i
import src.osm_configurator.view.constants.button_constants as button_constants_i

from src.osm_configurator.view.freezable import Freezable

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Final
    from src.osm_configurator.view.utilityframes.reduction_default_value_frame import ReductionDefaultValueFrame

# Finals
UP_ARROW_SIZE: Final = 10
DOWN_ARROW_SIZE: Final = 10
PAD_X: Final = 2
PAD_Y: Final = 2
ELEMENT_BORDER_DISTANCE: Final = 4

ENTRY_BUTTON_HEIGHT: Final = 44
ARROW_BUTTON_HEIGHT: Final = 20


class TagListPriorityFrame(customtkinter.CTkScrollableFrame, Freezable):
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

        # starts unfrozen
        self._frozen: bool = False

        self._last_pressed_entry_button: customtkinter.CTkButton | None = None

        self._selected_category: category_i.Category | None = None
        self._selected_entry: default_value_entry_i.DefaultValueEntry | None = None

        self._selected_button_id: int = 0

        self._entries: [default_value_entry_i.DefaultValueEntry] = []

        # The images used for moving entries up and down
        self._up_arrow_image: customtkinter.CTkImage = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(PROJECT_DIR, "data/view_icons/arrow_up.png")),
            dark_image=Image.open(os.path.join(PROJECT_DIR, "data/view_icons/arrow_up.png")),
            size=(UP_ARROW_SIZE, UP_ARROW_SIZE))

        self._down_arrow_image: customtkinter.CTkImage = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(PROJECT_DIR, "data/view_icons/arrow_down.png")),
            dark_image=Image.open(os.path.join(PROJECT_DIR, "data/view_icons/arrow_down.png")),
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
            entry (default_value_entry.DefaultValueEntry | None): A default value entry, that shall be loaded directly,
                can be None, to not load a specific entry directly

        Returns:
            bool: True if category was successfully loaded, else False
        """

        # no button has been pressed yet
        self._last_pressed_entry_button: customtkinter.CTkButton | None = None

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

            # Determine, what button corresponds to the entry
            e: default_value_entry_i.DefaultValueEntry
            entry_id: int = 0
            for e in self._entries:
                if e == self._selected_entry:
                    break
                entry_id += 1

            # Now disabling all "bad" arrow buttons, such as the 2 at the default value, the down on the 2nd entry,
            # and the up on the last entry
            self._disabling_bad_arrows()

            # Pretending the corresponding button was pressed
            self._entry_button_pressed(entry_id)

        # category is loaded
        return True

    def _disabling_bad_arrows(self):
        # Disables all arrow buttons, that's should not be press able
        # the 2 on the Default shall not be press-able
        # the up on the 2nd entry shall not be press-able
        # the down on the last shall not be press-able
        self._up_button_list[0].configure(state="disabled",
                                          fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DISABLED.value)
        self._down_button_list[0].configure(state="disabled",
                                            fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DISABLED.value)

        if len(self._up_button_list) > 1:
            self._up_button_list[1].configure(
                state="disabled",
                fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DISABLED.value
            )

        if len(self._down_button_list) > 1:
            self._down_button_list[len(self._down_button_list) - 1].configure(
                state="disabled",
                fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DISABLED.value
            )

    def _up_button_pressed(self, button_id: int):

        if self._selected_category.move_default_value_entry_up(self._entries[button_id]):
            # If it was successfully moved, we move it in the frame as well
            # Only the Entry Button needs to be moved, since up and down button are everywhere and only
            # correspond to the entries through their id, so change id of button, change partners

            # The Button above
            entry_button: customtkinter.CTkButton = self._entry_button_list[button_id - 1]
            # Swapping the buttons on the list
            self._entry_button_list[button_id - 1] = self._entry_button_list[button_id]
            self._entry_button_list[button_id] = entry_button

            # setting the command new, so they still ask for the right entry and don't send the wrong button_id to
            # the command, and make every button call wrong entries
            self._entry_button_list[button_id].configure(command=partial(self._entry_button_pressed, button_id))
            self._entry_button_list[button_id - 1].configure(command=partial(self._entry_button_pressed, button_id - 1))

            # Re-gridding all entry buttons
            self._regrid_entries()

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

            # setting the command new, so they still ask for the right entry and don't send the wrong button_id to
            # the command, and make every button call wrong entries
            self._entry_button_list[button_id].configure(command=partial(self._entry_button_pressed, button_id))
            self._entry_button_list[button_id + 1].configure(command=partial(self._entry_button_pressed, button_id + 1))

            # Re-gridding all entry buttons
            self._regrid_entries()

            # refreshing the entries
            self._entries: [default_value_entry_i.DefaultValueEntry] = self._selected_category.get_default_value_list()
        else:
            alert_pop_up_i.AlertPopUp("Could not move Entry Down!")

    def _regrid_entries(self):
        self._remove_all_entry_buttons()
        self._place_all_entry_buttons()

    def _remove_all_entry_buttons(self):
        button: customtkinter.CTkButton
        for button in self._entry_button_list:
            button.grid_remove()

    def _place_all_entry_buttons(self):
        button: customtkinter.CTkButton
        index: int = 0
        for button in self._entry_button_list:
            button.grid(row=index * 2, column=0, rowspan=2, columnspan=1, padx=PAD_X, pady=PAD_Y)
            index += 1

    def _entry_button_pressed(self, button_id: int):
        # First activating all buttons, so they don't end up all disabled
        button: customtkinter.CTkButton
        for button in self._entry_button_list:
            button.configure(state="normal", text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                             fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value)

        # Disabling the pressed button
        self._entry_button_list[button_id].configure(
            state="disabled",
            text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR_DISABLED.value,
            fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DISABLED.value
        )

        self._selected_button_id: int = button_id
        self._last_pressed_entry_button: customtkinter.CTkButton = self._entry_button_list[button_id]

        # telling parent what entry was pressed
        # since buttons and entries in the id, we can just use the button_id to find it
        self._parent.load_entry(self._entries[button_id])

    def _add_entry_to_list(self, entry: default_value_entry_i.DefaultValueEntry):
        entry_button: customtkinter.CTkButton = customtkinter.CTkButton(
            master=self,
            width=int(self._width * (
                    4 / 5) - ELEMENT_BORDER_DISTANCE),
            height=ENTRY_BUTTON_HEIGHT,
            corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
            border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
            fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
            hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
            border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
            text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
            text=entry.get_default_value_entry_tag(),
            command=partial(self._entry_button_pressed,
                            len(self._entry_button_list))
        )

        entry_button.grid(row=len(self._entry_button_list) * 2, column=0, rowspan=2, columnspan=1, padx=PAD_X,
                          pady=PAD_Y)

        up_button: customtkinter.CTkButton = customtkinter.CTkButton(
            master=self,
            width=int(self._width * (
                    1 / 5) - ELEMENT_BORDER_DISTANCE),
            height=ARROW_BUTTON_HEIGHT,
            corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
            border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
            fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
            hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
            border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
            text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
            text="",
            command=partial(self._up_button_pressed,
                            len(self._up_button_list)),
            image=self._up_arrow_image
        )

        up_button.grid(row=len(self._up_button_list) * 2, column=1, rowspan=1, columnspan=1, padx=PAD_X, pady=PAD_Y)

        down_button: customtkinter.CTkButton = customtkinter.CTkButton(
            master=self,
            width=int(self._width * (
                    1 / 5) - ELEMENT_BORDER_DISTANCE),
            height=ARROW_BUTTON_HEIGHT,
            corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
            border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
            fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
            hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
            border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
            text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
            text="",
            command=partial(self._down_button_pressed,
                            len(self._down_button_list)),
            image=self._down_arrow_image
        )

        down_button.grid(row=len(self._down_button_list) * 2 + 1, column=1, rowspan=1, columnspan=1, padx=PAD_X,
                         pady=PAD_Y)

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

    def freeze(self):
        """
        If this method is called, the frame will freeze by disabling all possible interactions with it.
        """
        if not self._frozen:
            entry_button: customtkinter.CTkButton
            for entry_button in self._entry_button_list:
                entry_button.configure(state="disabled")

            up_button: customtkinter.CTkButton
            for up_button in self._up_button_list:
                up_button.configure(state="disabled")

            down_button: customtkinter.CTkButton
            for down_button in self._down_button_list:
                down_button.configure(state="disabled")

            self._frozen: bool = True

    def unfreeze(self):
        """
        If this method is called, the frame returns into its previous intractable state.
        """
        if self._frozen:
            # First activating everything
            entry_button: customtkinter.CTkButton
            for entry_button in self._entry_button_list:
                entry_button.configure(state="normal")

            up_button: customtkinter.CTkButton
            for up_button in self._up_button_list:
                up_button.configure(state="normal")

            down_button: customtkinter.CTkButton
            for down_button in self._down_button_list:
                down_button.configure(state="normal")

            # Now disabling what shall stay disabled
            self._disabling_bad_arrows()

            self._last_pressed_entry_button.configure(
                state="disabled",
                text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR_DISABLED.value,
                fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DISABLED.value
            )

            self._frozen: bool = False
