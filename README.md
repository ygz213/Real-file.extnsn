![](app/icons/icon.ico)

---

# Real-file.extnsn

This is just a GUI that detects your file's real extension using the filetype module.

## Requirements

- Python 3.5 and above
- [filetype](https://github.com/h2non/filetype.py) module for scanning

## Installation

1. Download source code from [Releases](https://github.com/ygz213/Real-file.extnsn/releases) page.
2. Open terminal and type `pip install filetype`
3. Run `main.py` for English or `main_turkish.py` for Turkish.

### Information if MIT License link is not working

That bug is caused by Python. To fix, you should make a minor change on `webbrowser.py` (It is on `{PYTHON_PATH}/lib/webbrowser.py`. Steps:

1. Find `except (FileNotFoundError, subprocess.CalledProcessError):` in the code
2. Change it as `except (FileNotFoundError, subprocess.CalledProcessError, PermissionError) :`
3. Problem is now fixed. This is pre-added on next versions of Python.

Source: <https://bugs.python.org/issue41005>

## Supported extensions

See <https://github.com/h2non/filetype.py#supported-types>.

---

## Thanks to

- Authors of [filetype](https://github.com/h2non/filetype.py) module
- Freepik for [magnifying glass](https://www.flaticon.com/free-icon/magnifier_71403) on the logo   (Icon made by [Freepik](https://www.freepik.com/) from www.flaticon.com)
- [formycity](https://www.veryicon.com/icons/miscellaneous/unicons/file-blank-4.html) for blank file on the logo
