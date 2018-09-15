This is an [info-beamer](https://info-beamer.com/) plugin displaying a simple text-based countdown.

# Dependencies

* [DejaVu fonts](https://packages.debian.org/stable/fonts-dejavu)
* [Python](https://www.python.org/) 3
* [gitdir](https://github.com/fenhl/gitdir)
* [info-beamer-text](https://github.com/fenhl/info-beamer-text)
* [timespec](https://github.com/fenhl/timespec)

# Usage

Run the `run.py` script and give it a timespec for the target date/time as arguments. See [the timespec documentation](https://github.com/fenhl/timespec#syntax) for details on how to write a timespec. The script will start info-beamer for you. The program will continue running even after the target date/time, but you can press <kbd>Ctrl</kbd>+<kbd>C</kbd> at any time to exit.
