
"""Registry for all remotely-stored CLI test data."""

import pooch

from openfe.data._registry import r2_entry

POOCH_CACHE = pooch.os_cache("openfe")

zenodo_cmet_data = r2_entry(
    "cmet_results.tar.gz",
    "56f58010f969ccf6a60d8d1203603929cbd308ea968ce673c3f00af89a11c900",
)
zenodo_rbfe_serial_data = r2_entry(
    "rbfe_results_serial_repeats.tar.gz",
    "f600015c94cd79fc9e8386871aabd51e4a1c2a591511a91f7745fcda98fdfe7f",
)
zenodo_rbfe_parallel_data = r2_entry(
    "rbfe_results_parallel_repeats.tar.gz",
    "945105ed5ce8e19c1de2729bc32a70905f2bc89e241a4a34ebdbe3b01fa68ed5",
)
zenodo_abfe_data = r2_entry(
    "abfe_results.zip",
    "5bd016beba82baff6d66ff30dfcef9cb1923e683fc72252a129ce3c6eb258d10",
)
zenodo_septop_data = r2_entry(
    "septop_results.zip",
    "76aa4130383a29f3b243e94e7a4ced2baf90b1a4834d9daf35aa32f76938cd55",
)

zenodo_data_registry = [
    zenodo_cmet_data,
    zenodo_rbfe_serial_data,
    zenodo_rbfe_parallel_data,
    zenodo_abfe_data,
    zenodo_septop_data,
]
