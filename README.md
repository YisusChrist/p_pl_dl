 p_pl_dl - Porn Playlist Downloader

<p align="center">
    <a href="https://github.com/YisusChrist/p_pl_dl/issues">
        <img src="https://img.shields.io/github/issues/YisusChrist/p_pl_dl?color=171b20&label=Issues%20%20&logo=gnubash&labelColor=e05f65&logoColor=ffffff">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/YisusChrist/p_pl_dl/forks">
        <img src="https://img.shields.io/github/forks/YisusChrist/p_pl_dl?color=171b20&label=Forks%20%20&logo=git&labelColor=f1cf8a&logoColor=ffffff">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/YisusChrist/p_pl_dl/stargazers">
        <img src="https://img.shields.io/github/stars/YisusChrist/p_pl_dl?color=171b20&label=Stargazers&logo=octicon-star&labelColor=70a5eb">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/YisusChrist/p_pl_dl/actions">
        <img alt="Tests Passing" src="https://github.com/YisusChrist/p_pl_dl/actions/workflows/github-code-scanning/codeql/badge.svg">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/YisusChrist/p_pl_dl/pulls">
        <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/YisusChrist/p_pl_dl?color=0088ff">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://opensource.org/license/gpl-3-0">
        <img alt="License" src="https://img.shields.io/github/license/YisusChrist/p_pl_dl?color=0088ff">
    </a>
</p>

<br>

<p align="center">
    <a href="https://github.com/YisusChrist/p_pl_dl/issues/new?assignees=YisusChrist&labels=bug&projects=&template=bug_report.yml">Report Bug</a>
    ·
    <a href="https://github.com/YisusChrist/p_pl_dl/issues/new?assignees=YisusChrist&labels=feature&projects=&template=feature_request.yml">Request Feature</a>
    ·
    <a href="https://github.com/YisusChrist/p_pl_dl/issues/new?assignees=YisusChrist&labels=question&projects=&template=question.yml">Ask Question</a>
    ·
    <a href="https://github.com/YisusChrist/p_pl_dl/security/policy#reporting-a-vulnerability">Report security bug</a>
</p>

<br>

A porn playlist downloader using `yt-dlp` and `beautifulsoup`, along with some limited support for image albums.

<details>
<summary>Table of Contents</summary>

- [Requirements](#requirements)
- [Installation](#installation)
  - [From PyPI](#from-pypi)
  - [Manual installation](#manual-installation)
  - [Uninstall](#uninstall)
- [Usage](#usage)
  - [Basic Usage](#basic-usage)
  - [Input TXT w/ URLs](#input-txt-w-urls)
  - [Cookies](#cookies)
- [Contributors](#contributors)
  - [How do I contribute to p\_pl\_dl?](#how-do-i-contribute-to-p_pl_dl)
- [License](#license)

</details>

Currently supports:

- lewdthots (albums only)
- pornhub
- porntrex
- spankbang
- xhamster
- xvideos

---

## Requirements

Here's a breakdown of the packages needed and their versions:

- [beautifulsoup4](https://pypi.org/project/beautifulsoup4) >= 4.12.3
- [core-helpers](https://github.com/YisusChrist/core_helpers)
- [jsbeautifier](https://pypi.org/project/jsbeautifier) >= 1.15.1
- [poetry](https://pypi.org/project/poetry) >= 1.7.1 (_only for manual installation_)
- [requests](https://pypi.org/project/requests) >= 2.31.0
- [rich](https://pypi.org/project/rich) >= 13.7.1
- [yt-dlp](https://pypi.org/project/yt-dlp) >= 2022.10.4

> [!NOTE]
> The software has been developed and tested using Python `3.12.1`. The minimum required version to run the software is Python 3.6. Although the software may work with previous versions, it is not guaranteed.

## Installation

### From PyPI

`p_pl_dl` can be installed easily as a PyPI package. Just run the following command:

```bash
pip3 install p_pl_dl
```

> [!IMPORTANT]
> For best practices and to avoid potential conflicts with your global Python environment, it is strongly recommended to install this program within a virtual environment. Avoid using the --user option for global installations. We highly recommend using [pipx](https://pypi.org/project/pipx) for a safe and isolated installation experience. Therefore, the appropriate command to install `p_pl_dl` would be:
>
> ```bash
> pipx install p_pl_dl
> ```

The program can now be ran from a terminal with the `p_pl_dl` command.

### Manual installation

If you prefer to install the program manually, follow these steps:

> [!WARNING]
> This will install the version from the latest commit, not the latest release.

1. Download the latest version of [p_pl_dl](https://github.com/YisusChrist/p_pl_dl) from this repository:

   ```bash
   git clone https://github.com/YisusChrist/p_pl_dl
   cd p_pl_dl
   ```

2. Install the package:

   ```bash
   poetry install --only main
   ```

3. Run the program:

   ```bash
   poetry run p_pl_dl
   ```

### Uninstall

If you installed it from PyPI, you can use the following command:

```bash
pipx uninstall p_pl_dl
```

## Usage

> [!TIP]
> For more information about the usage of the program, run `p_pl_dl --help` or `p_pl_dl -h`.

![Usage](https://i.imgur.com/ZvMr431.png)

### Basic Usage

Call `p_pl_dl` using command prompt. Pass in a text file with URLs using `-i`. Optionally, provide cookies with `-c`, and specify the download destination with `-d`.

For cookies, you may pass in a single text file, or a folder path containing multiple cookie text files.

Videos from each site will be downloaded to `\sites\<site name>` within the current working directory.

Using a single cookie text file:

```sh
p_pl_dl -i "C:\MyFolder\urls.txt" -c "C:\MyCookieFolder\cookies.txt" -d "F:\DownloadDestination"
```

Using multiple cookie text files stored in a folder:

```sh
p_pl_dl -i "C:\MyFolder\urls.txt" -c "C:\MyCookieFolder\" -d "F:\DownloadDestination"
```

You may also restrict downloads to a specific site using `-o`. This may be useful if your `urls.txt` has lots of playlists/videos across many sites, but you need to scrape a specific one. Pass in the full name of the site as given in the list of supported sites above.

```sh
p_pl_dl -i "C:\MyFolder\urls.txt" -c "C:\MyCookieFolder\" -d "F:\DownloadDestination" -o "xhamster"
p_pl_dl -i "C:\MyFolder\urls.txt" -c "C:\MyCookieFolder\" -d "F:\DownloadDestination" -o "spankbang"
```

---

### Input TXT w/ URLs

The URL text file should have URLs separated by a line break. The URLs may be for individual videos or entire playlists.

Example:

```
https://www.xvideos.com/video35247781/
https://www.xhamster.com/videos/busty-blonde-girl-get-fucked-with-nice-lingerie-14429903
```

### Cookies

All cookie text files must have `# Netscape HTTP Cookie File` on its first line. If that line is not found, the file will not be recognized as a cookie file and ignored.

## Contributors

<a href="https://github.com/YisusChrist/p_pl_dl/graphs/contributors"><img src="https://contrib.rocks/image?repo=YisusChrist/p_pl_dl" /></a>

### How do I contribute to p_pl_dl?

Before you participate in our delightful community, please read the [code of conduct](https://github.com/YisusChrist/.github/blob/main/CODE_OF_CONDUCT.md).

I'm far from being an expert and suspect there are many ways to improve – if you have ideas on how to make the configuration easier to maintain (and faster), don't hesitate to fork and send pull requests!

We also need people to test out pull requests. So take a look through [the open issues](https://github.com/YisusChrist/p_pl_dl/issues) and help where you can.

See [Contributing](https://github.com/YisusChrist/.github/blob/main/CONTRIBUTING.md) for more details.

## License

`p_pl_dl` is released under the [GPL-3.0 License](https://opensource.org/license/gpl-3-0).
