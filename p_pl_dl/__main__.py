import json
import os
from argparse import Namespace
from time import sleep

from core_helpers.logs import logger
from core_helpers.updates import check_updates
from core_helpers.utils import print_welcome
from rich import print
from rich.traceback import install

from p_pl_dl import scrappers as dExtractors
from p_pl_dl.cli import get_parsed_args
from p_pl_dl.consts import EXIT_FAILURE, GITHUB, LOG_FILE, PACKAGE
from p_pl_dl.consts import __desc__ as DESC
from p_pl_dl.consts import __version__ as VERSION
from p_pl_dl.downloader import (detect_websites, get_scrappers_list, load_urls,
                                process_url)
from p_pl_dl.scrappers import _common as dl_common
from p_pl_dl.utils import exit_session


def main() -> None:
    args: Namespace = get_parsed_args()
    install(show_locals=args.debug)
    logger.setup_logger(PACKAGE, LOG_FILE, args.debug, args.verbose)

    if GITHUB:
        check_updates(GITHUB, VERSION)

    print_welcome(PACKAGE, VERSION, DESC, GITHUB)

    if args.dest:
        try:
            os.chdir(args.dest)
        except FileNotFoundError as e:
            print(f"Could not change the working directory: {e}")
            exit_session(EXIT_FAILURE)

    print(f"Working download directory: {os.getcwd()}")

    sSourceCookies = args.cookies
    if sSourceCookies:
        print(f"Cookies source: {sSourceCookies}")
        if ".txt'" in sSourceCookies:
            dl_common.parseCookieFile(sSourceCookies)
        else:
            dl_common.parseCookies(sSourceCookies)
    else:
        print(f"No cookies provided!")

    sSourceUrls = args.input
    print(f"Using the following input source: {sSourceUrls}")

    nVideoLimit = int(args.limit) if args.limit else None
    print(f"Video limit per URL = {nVideoLimit}")

    # Load URLs from a file or command-line argument
    sLines: list[str] = load_urls(sSourceUrls, args.url)

    # Detect websites from URLs
    detected_sites: dict[str, str] = detect_websites(sLines)
    print("Detected websites:")
    print(json.dumps(detected_sites, indent=4))

    if args.only and args.only in get_scrappers_list():
        # Filter only the URLs that match the site in args.only
        detected_sites = dict(
            (k, v) for k, v in detected_sites.items() if v == args.only
        )

    for sUrl, sSite in detected_sites.items():
        if hasattr(dExtractors, sSite):
            module = getattr(dExtractors, sSite)
            process_url(sUrl, module, nVideoLimit)
        else:
            print(f"No extractor available for {sSite} - {sUrl}")
            sleep(0.5)


if __name__ == "__main__":
    main()
