from prod_project.config_schemas.config_schema import Config
from prod_project.utils.config_utils import get_config


@get_config(config_path="../configs", config_name="config")
def entrypoint(config: Config) -> None:
    print(config)


if __name__ == "__main__":
    entrypoint()  # type: ignore
