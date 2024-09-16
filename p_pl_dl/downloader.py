import os

from rich import print

from p_pl_dl.consts import EXIT_FAILURE
from p_pl_dl.utils import exit_session


def get_scrappers_list() -> list[str]:
    """
    Get a list of all available scrappers.

    Returns:
        A list of all available scrappers.
    """
    # Get the list of modules in the scrappers directory
    scrappers: list[str] = [
        os.path.splitext(s)[0]
        for s in os.listdir(os.path.join(os.path.dirname(__file__), "scrappers"))
        if not s.startswith("_")
    ]

    return scrappers


def detect_websites(urls) -> dict:
    scrappers: list[str] = get_scrappers_list()
    return {url: site for url in urls for site in scrappers if site in url}


def load_urls(source_file, url_argument) -> list[str]:
    if not source_file and not url_argument:
        print("No input source provided. Exiting...")
        exit_session(EXIT_FAILURE)

    if source_file:
        try:
            with open(source_file) as fSourceUrls:
                url_list: list[str] = [line.strip() for line in fSourceUrls.readlines()]
        except (FileNotFoundError, PermissionError, OSError) as e:
            print(f"Could not open the source file: {e}")
            exit_session(EXIT_FAILURE)
        return list(set(url_list))
    elif url_argument:
        return [url_argument]
    else:
        return []


def process_url(url, module, video_limit) -> None:
    # Cookies should already be parsed and available when going through main
    module.run(url, sCookieSource=None, nVideoLimit=video_limit)
