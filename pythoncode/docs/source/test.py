from pathlib import Path
import os
import sys

current_dir = os.path.dirname(__file__)
target_dir = os.path.abspath(os.path.join(current_dir, "../../ConfiguratorOSMData"))
sys.path.insert(0, target_dir)

print(target_dir)

