---

# Miner Control Tray Application

A simple system tray application to control the T-Rex Miner based on predefined schedules. Built with Python, this application provides a convenient interface for users to start, stop, or monitor their mining operations right from their desktop's system tray.

## Features

- **Scheduled Operations**: The miner is set to start automatically at 8 PM and stop at 5 PM daily.
- **Manual Control**: Users can manually start or stop the miner anytime from the system tray menu.
- **Notifications**: Provides feedback to users when they try to start the miner outside the scheduled hours.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/dadams-AU/miner-control-tray.git
    cd miner-control-tray
    ```

2. Install the required Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

3. Adjust any paths or settings in `xna_app.py` if necessary.

4. Run the application:

    ```bash
    python3 xna_app.py
    ```

## Usage

Once the application is running:

- Click on the system tray icon to see the options.
- Select "Start Miner" to manually start the mining process.
- Select "Stop Miner" to manually stop the mining process.
- Click "Exit" to close the tray application.

## Credits

- Application developed and conceptualized by ChatGPT from OpenAI.
- Special thanks to [@dadams-AU](https://github.com/dadams-AU) for collaborating on refining the requirements and features.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---
