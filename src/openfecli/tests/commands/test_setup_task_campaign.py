import pathlib
import tarfile
from importlib import resources

import pytest
from click.testing import CliRunner

from openfecli.commands.setup_task_campaign import setup_task_campaign

from ..utils import assert_click_success


@pytest.fixture
def alchemical_network_mcl1_path(tmp_path: pathlib.Path) -> pathlib.Path:
    # The test data is distributed as a tarball, not an importable package.
    archive = resources.files("openfe.tests.data") / "warehouse_data.tar.gz"
    with archive.open("rb") as stream, tarfile.open(fileobj=stream, mode="r:gz") as tar:
        data = tar.extractfile("warehouse_data/alchemicalNetwork_mc1_small.json")
        assert data is not None
        path = tmp_path / "alchemicalNetwork_mc1_small.json"
        path.write_bytes(data.read())
    return path


def test_setup_task_campaign(alchemical_network_mcl1_path):
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            setup_task_campaign, ["--alchemical-network", str(alchemical_network_mcl1_path)]
        )
        assert_click_success(result)
        assert pathlib.Path("warehouse_alchemicalNetwork_mc1_small").is_dir()
        assert pathlib.Path("tasks_alchemicalNetwork_mc1_small.db").is_file()


def test_setup_task_campaign_custom_name(alchemical_network_mcl1_path):
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            setup_task_campaign,
            [
                "--alchemical-network",
                str(alchemical_network_mcl1_path),
                "--name",
                "my_special_campaign",
            ],
        )
        assert_click_success(result)
        assert pathlib.Path("warehouse_my_special_campaign").is_dir()
        assert pathlib.Path("tasks_my_special_campaign.db").is_file()
