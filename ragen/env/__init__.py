from .frozen_lake.config import FrozenLakeEnvConfig
from .frozen_lake.env import FrozenLakeEnv
from .sokoban.config import SokobanEnvConfig
from .sokoban.env import SokobanEnv


REGISTERED_ENVS = {
    "frozen_lake": FrozenLakeEnv,
    "sokoban": SokobanEnv,
}

REGISTERED_ENV_CONFIGS = {
    "frozen_lake": FrozenLakeEnvConfig,
    "sokoban": SokobanEnvConfig,
}

try:
    from .webshop.config import WebShopEnvConfig
    from .webshop.env import WebShopEnv
except ImportError:
    pass
else:
    REGISTERED_ENVS["webshop"] = WebShopEnv
    REGISTERED_ENV_CONFIGS["webshop"] = WebShopEnvConfig
