from __future__ import annotations

from pathlib import Path
import os


class FileDeletion:
    """
    Responsible for deleting files.
    """

    @classmethod
    def reset_folder(cls, path: Path) -> bool:
        """
        Deletes all files in the given folder. If the folder does not exist it will create it.
        Args:
            path: The path to the folder
        Returns:
            bool: True, if the deletion was successful
        """
        # Create folder
        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except PermissionError:
                return False
        # Delete old files in folder
        delete_path = str(path) + '//'
        for file_name in os.listdir(delete_path):
            # construct full file path
            file = delete_path + file_name
            if os.path.isfile(file):
                try:
                    os.remove(file)
                except PermissionError:
                    return False
        return True
