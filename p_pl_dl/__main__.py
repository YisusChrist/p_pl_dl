import argparse
import json
import os
import sys
from time import sleep

from rich import print
from rich.traceback import install
from rich_argparse_plus import RichHelpFormatterPlus

from . import scrappers as dExtractors
from .consts import *
from .logs import logger
from .scrappers import _common as dl_common


def get_scrappers_list() -> list:
    """
    Get a list of all available scrappers.

    Returns:
        A list of all available scrappers.
    """
    # Get the list of modules in the scrappers directory
    scrappers = [
        os.path.splitext(s)[0]
        for s in os.listdir(os.path.join(os.path.dirname(__file__), "scrappers"))
        if not s.startswith("_")
    ]

    return scrappers


def detect_websites(urls) -> dict:
    scrappers = get_scrappers_list()
    return {url: site for url in urls for site in scrappers if site in url}


def load_urls(source_file, url_argument):
    if not source_file and not url_argument:
        print("No input source provided. Exiting...")
        exit_session(EXIT_FAILURE)
        
    if source_file:
        try:
            with open(source_file) as fSourceUrls:
                url_list = [line.strip() for line in fSourceUrls.readlines()]
                return list(set(url_list))
        except (FileNotFoundError, PermissionError, OSError) as e:
            print(f"Could not open the source file: {e}")
            exit_session(EXIT_FAILURE)
    elif url_argument:
        return [url_argument]


def process_url(url, module, video_limit):
    try:
        # Cookies should already be parsed and available when going through main
        module.run(url, sCookieSource=None, nVideoLimit=video_limit)
    except Exception as e:
        print(f"[yellow]Error processing {module}[/]: {e}")


def get_parsed_args() -> argparse.Namespace:
    """
    Parse and return command-line arguments.

    Returns:
        The parsed arguments as an argparse.Namespace object.
    """
    RichHelpFormatterPlus.choose_theme("grey_area")

    parser = argparse.ArgumentParser(
        description=DESC,  # Program description
        formatter_class=RichHelpFormatterPlus,  # Disable line wrapping
        allow_abbrev=False,  # Disable abbreviations
        add_help=False,  # Disable default help
    )

    # Required arguments
    g_required = parser.add_argument_group("Required Arguments")
    g_required.add_argument(
        "-i", "--input", help="Input TXT file with URLs to process", type=str
    )
    g_required.add_argument("-u", "--url", help="URL to process", type=str)
    g_required.add_argument(
        "-c", "--cookies", help="Input TXT file with cookies", type=str
    )
    g_required.add_argument(
        "-d", "--dest", help="Download destination path", default=".", type=str
    )
    g_required.add_argument(
        "-o",
        "--only",
        help="Only run a specific site",
        choices=get_scrappers_list(),
        type=str.lower,
    )
    g_required.add_argument(
        "-l", "--limit", help="Limit the number of videos", type=int
    )

    # Optional arguments
    g_misc = parser.add_argument_group("Miscellaneous Options")
    # Help
    g_misc.add_argument(
        "-h", "--help", action="help", help="Show this help message and exit."
    )
    # Verbose
    g_misc.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action="store_true",
        default=False,
        help="Show log messages on screen. Default is False.",
    )
    # Debug
    g_misc.add_argument(
        "-D",
        "--debug",
        dest="debug",
        action="store_true",
        default=False,
        help="Activate debug logs. Default is False.",
    )
    g_misc.add_argument(
        "-V",
        "--version",
        action="version",
        help="Show version number and exit.",
        version=f"[argparse.prog]{NAME}[/] version [i]{VERSION}[/]",
    )

    return parser.parse_args()


def exit_session(exit_value: int) -> None:
    """
    Exit the program with the given exit value.

    Args:
        exit_value (int): The POSIX exit value to exit with.
    """
    logger.info("End of session")
    # Check if the exit_value is a valid POSIX exit value
    if not 0 <= exit_value <= 255:
        exit_value = EXIT_FAILURE

    if exit_value == EXIT_FAILURE:
        print(
            "[red]There were errors during the execution of the script. "
            f"Check the logs at {LOG_PATH} for more information.[/red]"
        )

    # Exit the program with the given exit value
    sys.exit(exit_value)


def main():
    args = get_parsed_args()
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
    sLines = load_urls(sSourceUrls, args.url)

    # Detect websites from URLs
    detected_sites = detect_websites(sLines)
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
    # Enable rich error formatting in debug mode
    install(show_locals=DEBUG)
    if DEBUG:
        print("[yellow]Debug mode is enabled[/]")
    if PROFILE:
        import cProfile

        print("[yellow]Profiling is enabled[/]")
        cProfile.run("main()")
    else:
        main()
