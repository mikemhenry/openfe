import pooch

from ._registry import zenodo_data_registry


def retrieve_registry_data(zenodo_registry: list[dict], path: str) -> None:
    """Helper function for pulling all test data up-front.

    Parameters
    ----------
    path : str
        path to store the data - usually a pooch.os_cache instance.

    """

    def _infer_processor(fname: str):
        if fname.endswith("tar.gz"):
            return pooch.Untar()
        elif fname.endswith("zip"):
            return pooch.Unzip()
        else:
            return None

    # TODO: parallelize this?
    for d in zenodo_registry:
        pooch.retrieve(
            url=f'{d["base_url"].rstrip("/")}/{d["fname"]}',
            known_hash=d["known_hash"],
            fname=d["fname"],
            processor=_infer_processor(d["fname"]),
            progressbar=True,
            path=path,
        )
