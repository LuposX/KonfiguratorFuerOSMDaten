from __future__ import annotations

from typing import TYPE_CHECKING

import src.osm_configurator.model.application.recommender_system as recommender_system_i
from src_tests.definitions import PROJECT_MAIN_FOLDER
import src.osm_configurator.model.application.application_settings as application_settings_i

import os

if TYPE_CHECKING:
    from typing import List
    from src.osm_configurator.model.application.application_settings import ApplicationSettings


class TestRecommenderSystem:
    def test_recommender_system_correctly(self):
        # create a recommender system
        settings: ApplicationSettings = application_settings_i.ApplicationSettings()
        recommender_system_o = recommender_system_i.RecommenderSystem(settings)

        found_list_with_keys: List[str] = recommender_system_o.recommend_key("buil")

        assert "building" in found_list_with_keys
        assert "building:levels" in found_list_with_keys

        found_list_with_keys: List[str] = recommender_system_o.recommend_key("hi")

        assert "highway" in found_list_with_keys
        assert "historic" in found_list_with_keys
        assert "hiking" in found_list_with_keys
