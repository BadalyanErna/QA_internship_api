from pytest import fixture
from config import Config


def read_config(parser):
    parser.addoption(
        "--env",
        action="store",
        default="local")


@fixture(scope="session")
def env(request):
    return request.config.getaddoption("--env")


@fixture(scope="session")
def app_config(env):
    conf = Config(env)
    return conf
