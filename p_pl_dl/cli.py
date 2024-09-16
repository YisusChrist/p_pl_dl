from argparse import ArgumentParser, Namespace

from rich_argparse_plus import RichHelpFormatterPlus

from p_pl_dl.consts import PACKAGE
from p_pl_dl.consts import __desc__ as DESC
from p_pl_dl.consts import __version__ as VERSION
from p_pl_dl.downloader import get_scrappers_list


def get_parsed_args() -> Namespace:
    """
    Parse and return command-line arguments.

    Returns:
        The parsed arguments as an argparse.Namespace object.
    """
    RichHelpFormatterPlus.choose_theme("grey_area")

    parser = ArgumentParser(
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
        version=f"[argparse.prog]{PACKAGE}[/] version [i]{VERSION}[/]",
    )

    return parser.parse_args()
