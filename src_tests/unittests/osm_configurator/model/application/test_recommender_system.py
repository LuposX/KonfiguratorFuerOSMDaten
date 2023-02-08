from __future__ import annotations

from typing import TYPE_CHECKING

import src.osm_configurator.model.application.recommender_system as recommender_system_i
from src_tests.definitions import PROJECT_MAIN_FOLDER

import os

if TYPE_CHECKING:
    from typing import List


class TestRecommenderSystem:
    def test_recommender_system_correctly(self):
        # create a recommender system
        recommender_system_o = recommender_system_i.RecommenderSystem()

        found_list_with_keys: List[str] = recommender_system_o.recommend_key("buil", os.path.join(PROJECT_MAIN_FOLDER, "data/all_osm_keys.csv"))

        assert "building" in found_list_with_keys
        assert "building:levels" in found_list_with_keys
        assert "building:min_level" in found_list_with_keys

        found_list_with_keys: List[str] = recommender_system_o.recommend_key("hi", os.path.join(PROJECT_MAIN_FOLDER,
                                                                                                  "data/all_osm_keys.csv"))

        assert "highway" in found_list_with_keys
        assert "historic" in found_list_with_keys
        assert "hiking" in found_list_with_keys

    def test_recommender_system_wrong_path(self):
        # create a recommender system
        recommender_system_o = recommender_system_i.RecommenderSystem()

        assert recommender_system_o.recommend_key("buil", os.path.join(PROJECT_MAIN_FOLDER, "data/aladadl_osmdada_keys.csv")) == None


