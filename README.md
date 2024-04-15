```markdown
# Telegram Greeting and Farewell Bot

A simple Telegram bot written in Python using the Telegram Bot API to greet new users upon joining a group and bid farewell to users when they leave the group.

## Description

This bot is designed to greet new users with a customizable message when they join a Telegram group and bid farewell to users with a predefined message when they leave the group. It listens for status updates regarding new members joining or existing members leaving the group and responds accordingly.

## Usage

1. **Set Up Your Bot Token**: Replace `"token here"` in the `main()` function with your actual bot token obtained from the BotFather on Telegram.

2. **Customize Greeting and Farewell Messages**: You can customize the greeting and farewell messages by modifying the `bot_message` variable in the `greet_new_user()` and `goodbye()` functions.

3. **Run the Bot**: Once you have set up your bot token and customized the messages, run the script. The bot will start listening for updates and respond to new members joining or leaving the group.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/telegram-greeting-farewell-bot.git
   ```

2. Install the required dependencies:

   ```bash
   pip install python-telegram-bot
   ```

3. Run the bot script:

   ```bash
   python bot.py
   ```

## Dependencies

- python-telegram-bot: A Python wrapper for the Telegram Bot API.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
