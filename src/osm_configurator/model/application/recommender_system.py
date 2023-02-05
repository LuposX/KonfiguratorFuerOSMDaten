from __future__ import annotations

from typing import TYPE_CHECKING

import pandas as pd

if TYPE_CHECKING:
    from typing import List, Final
    from pathlib import Path
    from pandas import Series


# the name of the data entry in the osm tag key file
CL_KEY: Final = "key"


class RecommenderSystem:

    """
    This class job is to provide recommendations to different classes.
    """

    def __init__(self):
        """
        Creates a new instance of the RecommenderSystem.
        """
        pass

    # TODO: remember the path_to the recommender file is saved in the data folder
    def recommend_key(self, input: str, path_to_recommender_file: Path) -> List[str]:
        """
        Creates recommendations based on user input

        Args:
            input (str): The input from which to generate suggestions.
            path_to_recommender_file (Path):

        Returns:
            Series: Returns a Series of strings containing the recommendations depending on the input.
        """
        # open the file
        key_df = pd.read_csv(path_to_recommender_file)

        # gets a series with true and false
        # an entry is true if the entry in the dataframe at that position contains the string
        found_matches: Series = key_df[CL_KEY].str.contains(input)

        return key_df.loc[found_matches]
