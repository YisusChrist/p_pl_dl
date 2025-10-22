from argparse import Namespace

from core_helpers.cli import ArgparseColorThemes, setup_parser

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
    parser, g_required = setup_parser(
        PACKAGE,
        DESC,
        VERSION,
        ArgparseColorThemes.GREY_AREA,
    )

    # Required arguments
    g_required.add_argument(
        "-i", "--input", help="Input TXT file with URLs to process", type=str
    )
    g_required.add_argument("-u", "--url", help="URL to process", type=str)
    g_required.add_argument(
        "-c", "--cookies", help="Input TXT file with cookies", type=str
    )
    g_required.add_argument(
        "-ds", "--dest", help="Download destination path", default=".", type=str
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

    return parser.parse_args()
