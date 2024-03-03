import tomli

def load_config(config_loc: str = "./config/config.toml"):
    with open(config_loc, "rb") as f:
        config = tomli.load(f)
    return config