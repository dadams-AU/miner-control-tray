---

# Miner Control Tray Application

A simple system tray application to control the Rigel Miner based on predefined schedules. Built with Python, this application provides a convenient interface for users to start, stop, or monitor their mining operations right from their desktop's system tray. This should work with any mining software.

## Features

- **Scheduled Operations**: The miner is set to start automatically at 8 PM and stop at 5 PM daily.
- **Manual Control**: Users can manually start or stop the miner from the system tray menu anytime.
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

3. Adjust any paths or settings in `_app.py` if necessary.

4. Run the application:

    ```bash
    python3 `app.py
    ```

## Usage

Once the application is running:

- Click on the system tray icon to see the options.
- Select "Start Miner" to manually start the mining process.
- Select "Stop Miner" to manually stop the mining process.
- Click "Exit" to close the tray application.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/dadams-AU/miner-control-tray/blob/main/LICENSE) file for details.

---
