
import pooch

POOCH_CACHE = pooch.os_cache("openfe")


def r2_entry(fname: str, sha256: str) -> dict[str, str]:
    """Create a Pooch registry entry for content-addressed R2 data."""
    return {
        "base_url": f"https://data.openfe.org/v1/{sha256}/",
        "fname": fname,
        "known_hash": f"sha256:{sha256}",
    }


zenodo_rfe_simulation_nc = r2_entry(
    "simulation.nc",
    "92361a0864d4359a75399470135f56642b72c605069a4c33dbc4be6f91f28b31",
)

zenodo_t4_lysozyme_traj = r2_entry(
    "t4_lysozyme_trajectory.zip",
    "e985d055db25b5468491e169948f641833a5fbb67a23dbb0a00b57fb7c0e59c8",
)
zenodo_industry_benchmark_systems = r2_entry(
    "industry_benchmark_systems.zip",
    "2bb5eee36e29b718b96bf6e9350e0b9957a592f6c289f77330cbb6f4311a07bd",
)
zenodo_resume_data = r2_entry(
    "multistate_checkpoints.zip",
    "1ff25e04513e1dff2917d163e6c9c90cde0c0b3a3738f7f596c7f28b86027696",
)
zenodo_md_resume_data = r2_entry(
    "checkpoint.xml",
    "ab5ec6405f200df8fd375971a8c87ec434f7a6166b9ff035df569853397a3359",
)
zenodo_septop_structural = r2_entry(
    "septop_structural_results.zip",
    "c30208eaf43b5aadc83368ba6319d35468d5311a7226d2a72a248881e1a38d6d",
)
zenodo_abfe_structural = r2_entry(
    "abfe_simulation_outputs.zip",
    "c8ffc8667d86fa4b3b83fcf6371e0046811f5f217980dd37a6ab9b1042a2fa69",
)

zenodo_data_registry: list[dict[str, str]] = [
    zenodo_rfe_simulation_nc,
    zenodo_t4_lysozyme_traj,
    zenodo_industry_benchmark_systems,
    zenodo_resume_data,
    zenodo_md_resume_data,
    zenodo_septop_structural,
    zenodo_abfe_structural,
]
