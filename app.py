import os
import sys
import webview


class Api:
    def __init__(self):
        self._window = None

    def set_window(self, window):
        self._window = window

    def minimize(self):
        if self._window is not None:
            try:
                self._window.minimize()
            except Exception:
                pass

    def toggle_fullscreen(self):
        if self._window is not None:
            try:
                self._window.toggle_fullscreen()
            except Exception:
                pass


def get_index_path() -> str:
    """Return absolute path to index.html next to this script or inside a PyInstaller bundle."""
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        base_dir = sys._MEIPASS  # type: ignore[attr-defined]
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, "index.html")


def main() -> None:
    index_path = get_index_path()
    if not os.path.exists(index_path):
        raise FileNotFoundError(f"Файл index.html не найден: {index_path}")

    url = "file:///" + index_path.replace("\\", "/")
    api = Api()
    window = webview.create_window(
        title="AiTrats",
        url=url,
        width=960,
        height=760,
        min_size=(520, 520),
        resizable=True,
        background_color="#0f172a",
        js_api=api,
    )
    api.set_window(window)
    webview.start()


if __name__ == "__main__":
    main()
