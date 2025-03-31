# PyQt5 Media Player

This is a comprehensive media player application developed using PyQt5,
providing a rich user interface for playing audio and video files.

## Overview

The application is structured into a main window class (`Window`) that manages the user interface and media playback. It utilizes PyQt5's multimedia modules for playing audio and video, and standard widgets for creating the user interface. A custom model (`PlaylistModel`) is used to manage the playlist data.

## Features

* **Versatile File Support:** Plays a wide range of media formats (mp4, webm, mp3, wav, etc.).
* **Dynamic Playlist:** Allows users to create, manage, and interact with a playlist.
* **Complete Playback Controls:** Offers standard controls like play/pause, stop, previous, next, skip forward/backward.
* **Precise Volume Management:** Includes a volume slider and mute functionality.
* **Accurate Time Seeking:** Enables users to navigate through media using a time slider.
* **Adjustable Playback Speed:** Supports various playback speeds (0.25x to 3x).
* **Flexible Aspect Ratio:** Toggles between keeping and ignoring the media's aspect ratio.
* **Multiple Playback Modes:** Supports loop, item loop, shuffle, and sequential playback.
* **Intuitive Keyboard Shortcuts:** Provides keyboard shortcuts for quick control.
* **Sleek Dark Theme:** Features a dark theme for enhanced visual experience.
* **Integrated Playlist View:** Displays the playlist within the application.
* **Playlist Item Removal:** Allows users to remove items from the playlist.

## Project Structure

* **`main.py`:**
    * Contains the core logic of the media player.
    * Defines the `Window` class, which is the main application window.
    * Includes the `PlaylistModel` class, a custom model for the playlist.
    * Provides the `hhmmss()` function for time formatting.
    * Implements the `main()` function to initialize and run the application.
* **`icon_resource.py` (Optional):**
    * Contains the icon resources used in the application.
    * If not present, the application may use default icons.

## Code Explanation

1.  **Imports and Setup:**
    * Imports necessary PyQt5 modules for GUI, multimedia, and widgets.
    * Imports the optional `icon_resource` module.

2.  **`Window` Class:**
    * **`__init__(self)`:**
        * Initializes the main window, sets its size, title, and icon.
        * Calls `ui_init()` to set up the user interface.
    * **`ui_init(self)`:**
        * Creates the menu bar with an "Open File" action.
        * Sets up the `QMediaPlayer`, `QMediaPlaylist`, and `QGraphicsVideoItem` for media playback.
        * Creates the `QListView` and `PlaylistModel` for the playlist.
        * Creates time progress labels and a time slider.
        * Creates control buttons and a volume slider.
        * Arranges the widgets using layouts (`QVBoxLayout`, `QHBoxLayout`, `QGroupBox`, `QStackedWidget`).
        * Connects signals from widgets to their corresponding functions.
    * **Event Handlers:**
        * `resizeEvent()`: Resizes the video display.
        * `open_file()`: Opens media files and adds them to the playlist.
        * `ply()`: Plays the selected playlist item.
        * `remove()`: Removes the selected playlist item.
        * `playlist_selection_changed()`: Handles playlist item selection.
        * `playlist_position_changed()`: Updates the playlist view position.
        * `plistview()`: Toggles the playlist view.
        * `aspRatio()`: Changes the video aspect ratio.
        * `playback_speed()`: Adjusts the playback speed.
        * `playback_mode()`: Changes the playback mode.
        * `play_video()`: Plays or pauses the media.
        * `mediastate_changed()`: Updates the play/pause button icon.
        * `position_changed()`: Updates the time slider and current time label.
        * `duration_changed()`: Updates the time slider range and total time label.
        * `set_position()`: Sets the media playback position.
        * `backward()`/`forward()`: Skips the media backward/forward.
        * `mute_fn()`: Mutes/unmutes the media.
        * `keyPressEvent()`: Handles keyboard shortcuts.

3.  **`PlaylistModel` Class:**
    * Inherits from `QAbstractListModel`.
    * Manages the playlist data for the `QListView`.
    * `data()`: returns the filename of the media for display.
    * `rowCount()`: returns the number of items in the playlist.

4.  **`hhmmss(ms)` Function:**
    * Converts milliseconds to hh:mm:ss format.

5.  **`main()` Function:**
    * Creates a `QApplication` instance.
    * Sets the application style and dark theme palette.
    * Creates a `Window` instance and displays it.
    * Starts the application event loop.

## How It Works

1.  **Initialization:** The `main()` function initializes the application,
    sets up the dark theme, and creates the main window (`Window`).
2.  **UI Setup:** The `ui_init()` method creates the user interface,
    including the menu bar, media player objects, playlist view,
    time controls, and playback controls.
3.  **File Opening:** The "Open File" action triggers the `open_file()` function,
    which opens a file dialog, adds selected files to the playlist, and starts playback.
4.  **Playback:** The `QMediaPlayer` object handles media playback,
    and its signals are connected to update the UI (time slider, play/pause button, etc.).
5.  **Playlist Management:** The `PlaylistModel` manages the playlist data,
    and the `QListView` displays the playlist.
6.  **User Interaction:** The user interacts with the UI (buttons, sliders, etc.),
    and the corresponding event handlers update the media player and UI.
7.  **Event Loop:** The application event loop handles user input and updates the UI.

## Installation

1.  **Install PyQt5:**
    ```bash
    pip install PyQt5
    ```
2.  **(Optional) Install icon resources:**
    Ensure `icon_resource.py` is in the same directory.
3.  **Run the application:**
    ```bash
    python main.py
    ```

