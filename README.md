# TaterTrader

TaterTrader is a Python script that automatically follows the Tate brothers on Twitter and buys/sells tokens based on their tweets using the Bitmart API.
I was sent a tweet describing this, so I decided to build it pretty haphazardly for fun, kid tested, mother approved.

`Disclaimer`: This project is for educational and experimental purposes only. Make sure to thoroughly test and validate the strategy before using real funds. Additionally, comply with any legal and regulatory requirements in your jurisdiction. I am not responsible for any losses incurred while using this script.
## Features

- Follows the Tate brothers Twitter accounts specified by their user IDs
- Streams tweets from the Tate brothers in real-time
- Parses each tweet to check for token mentions starting with $
- Automatically places a buy order on Bitmart for the detected token

## Prerequisites

- Python 3.x
- Twitter Developer Account and API credentials
- Bitmart API credentials

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/BradMyrick/TaterTrader.git
   ```

2. Navigate to the project directory:
   ```
   cd TaterTrader
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Update the `main.py` file with your Twitter and Bitmart API credentials:
   - Replace `your_consumer_key`, `your_consumer_secret`, `your_access_token`, and `your_access_token_secret` with your Twitter API credentials.
   - Replace `your_bitmart_api_key`, `your_bitmart_secret_key`, and `your_bitmart_memo` with your Bitmart API credentials.

## Usage

To start the TaterTrader script, run the following command:

```
python main.py
```

The script will:
- Authenticate with the Twitter API
- Follow the specified Tate brothers Twitter accounts
- Start streaming tweets from the Tate brothers
- Parse each tweet for token mentions starting with $
- Automatically place a buy order on Bitmart for the detected token

## Disclaimer

Please note that automatically buying/selling tokens based on social media activity carries significant risks. This project is for educational and experimental purposes only. Make sure to thoroughly test and validate the strategy before using real funds. Additionally, comply with any legal and regulatory requirements in your jurisdiction.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).