from __future__ import annotations

from pathlib import Path
import os


class FileDeletion:
    """
    Responsible for deleting files.
    """

    def reset_folder(self, path: Path) -> bool:
        """
        Deletes all files in the given folder. If the folder does not exist it will create it.
        Args:
            path: The path to the folder
        Returns:
            bool: True, if the deletion was successful
        """
        # Create folder
        if not os.path.exists(path):
            os.makedirs(path)

        # Delete old files in folder
        delete_path = str(path) + '//'
        for file_name in os.listdir(delete_path):
            # construct full file path
            file = delete_path + file_name
            if os.path.isfile(file):
                os.remove(file)
        return True
