import os
import sys
import webview


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
        raise FileNotFoundError(f"Не найден файл интерфейса: {index_path}")

    url = "file:///" + index_path.replace("\\", "/")
    webview.create_window(
        title="AiTrats",
        url=url,
        width=960,
        height=760,
        min_size=(520, 520),
        resizable=True,
        background_color="#0f172a",
    )
    webview.start()


if __name__ == "__main__":
    main()
