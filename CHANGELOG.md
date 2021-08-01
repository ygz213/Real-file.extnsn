# R-F.E v4

- Fixed [broken MIT License link](https://github.com/ygz213/Real-file.extnsn/issues/8)
- Added [scanning capability to input box](https://github.com/ygz213/Real-file.extnsn/issues/7) when enter is pressed
- Moved "Could not find this file's extension" notification in the code to don't wrong inform when `AttributeError` is occurred by another reason

# R-F.E v3.5

- Added "Select file" button
- Changes on code
- Design changes

# R-F.E v3.4

- Fixed [wrong version information on Turkish](https://github.com/ygz213/Real-file.extnsn/issues/5)
- Fixed [different designs on English and Turkish version](https://github.com/ygz213/Real-file.extnsn/issues/6)

# R-F.E v3.3

- Added `OSError` handling when typed file path is invalid
- Deleted `options.py` because couldn't create a checked checkbutton if `options.txt`'s line 1 is `theme: True`
    - Lost [dark theme](https://github.com/ygz213/Real-file.extnsn/issues/2)
    - Might come back in the future
- Deleted `scanafile.py` because it's nonsense to a button to open another window to scanning on empty window (moved to main window)
- Design changes

# R-F.E v3.2

- Fixed [version information](https://github.com/ygz213/Real-file.extnsn/issues/4)

# R-F.E v3.1

- Added [dark theme](https://github.com/ygz213/Real-file.extnsn/issues/2)

# R-F.E v3

- Added "Options" interface (with `options.py`)
- Added scanning capability to "Scan a file" interface
- Changes on code

## BETA - Version 2

- Fixed [icon issue](https://github.com/ygz213/Real-file.extnsn/issues/1) on Linux (but couldn't test for some reasons)
- Added English version
- Added "Scan a file" interface (with `scanafile.py`)
- Rewrote `main.py`

## ALPHA - Version 1

- Added menu interface for Turkish
