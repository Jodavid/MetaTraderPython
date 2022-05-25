import os

import yaml


def _read_yaml_configuration_file(config_path: str) -> dict:
    with open(config_path, "r", encoding="utf8") as config_file:
        configs = yaml.load(config_file, Loader=yaml.loader.SafeLoader)

    return configs


ENV = os.getenv("ENV_MLOPS", "dev").lower()  # prod, dev or stage
STAGE_MAP = {"prod": "production", "dev": "development", "stage": "staging"}
assert ENV in STAGE_MAP

# Configuration file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.normpath(__file__)))
CONFIG_PATH = os.path.join(BASE_DIR, f"config_{ENV}.yaml")
CONFIG_YAML = _read_yaml_configuration_file(CONFIG_PATH)

# TimeFrame
TIMEFRAME = CONFIG_YAML.get("timeframe", {})
TIMEFRAME_TEMP = TIMEFRAME.get("timeframe_temp", "")