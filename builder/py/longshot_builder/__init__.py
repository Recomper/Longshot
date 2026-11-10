"""Longshot Builder, in Python: the same window as the WPF builder (builder/LongshotBuilder), run by python.org's own python.exe and
Qt's DLLs (both signed by their makers), with no executable of Longshot's own to download. It also does what the setup exe did
(builder/setup/setup.c): it reads a release's longshot-setup.txt, downloads the parts it names, checks each one's SHA-256 and
unpacks them into %LOCALAPPDATA%\\LongshotBuilder\\versions\\<tag>."""
APP_ID = "Recomper.Longshot.Builder"   # (Windows' AppUserModelID: the taskbar groups and shows the window as Longshot, not Python)
REPO = "Recomper/Longshot"
