from __future__ import annotations

import os
import numpy as np
import pandas as pd
from pathlib import Path

import src.osm_configurator.model.application.application_settings_default_enum as application_settings_enum

from definitions import PROJECT_DIR

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Final
    from pandas import Series
    from src.osm_configurator.model.application.application_settings import ApplicationSettings

# the name of the data entry in the osm tag key file
CL_KEY: Final = "key"
MOST_USED_TAGS_TABLE_PATH: Final = "data/most_used_keys.csv"


class RecommenderSystem:
    """
    This class job is to provide recommendations to different classes.
    """

    def __init__(self, application_settings_manager: ApplicationSettings):
        """
        Creates a new instance of the RecommenderSystem.
        """
        self._settings = application_settings_manager

    def recommend_key(self, input_key_str: str) -> List[str]:
        """
        Creates recommendations based on user input

        Args:
            input_key_str (str): The input from which to generate suggestions.


        Returns:
            List[str]: Returns a List of strings containing the recommendations depending on the input.
                If file was not found return None.
        """
        number_of_keys_to_recommend: int = int(self._settings .get_setting(
            application_settings_enum.ApplicationSettingsDefault.NUMBER_OF_RECOMMENDATIONS))

        path_to_recommender_file: Path = Path(os.path.join(PROJECT_DIR, MOST_USED_TAGS_TABLE_PATH))
        try:
            # open the file
            key_df = pd.read_csv(path_to_recommender_file)
        except Exception:
            return []

        # gets a series with true and false
        # an entry is true if the entry in the dataframe at that position contains the string
        found_matches: Series = key_df[CL_KEY].str.contains(input_key_str)

        # Replaces all NaN values with False.
        found_matches.replace(np.NaN, False, inplace=True)
        return key_df.loc[found_matches][CL_KEY].tolist()[:number_of_keys_to_recommend]
