from abc import ABC
from src.osm_configurator.model.application.application_interface import ApplicationInterface


class RecommenderSystem:

    def __init__(self):
        """
        Creates a new instance of the RecommenderSystem.
        """
        pass

    def recommend(self, input):
        """
        Creates recommendations based on user input

        Args:
            input (str): The input from which to generate suggestions.

        Returns:
            List<String>: Returns a list of strings containing the recommendations depending on the input.
        """
        pass

