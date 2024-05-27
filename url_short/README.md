# URL Shortener

This project provides a simple Python script to shorten URLs using the `pyshorteners` library. It allows users to input a URL, which is then shortened using the TinyURL service.

## Features

- **URL Shortening**: Converts long URLs into shorter, more manageable links.
- **User Input**: Accepts URLs directly from the user input.
- **Simple and Fast**: Provides a quick and easy way to shorten URLs using TinyURL.

## Requirements

Before you run the script, make sure you have the following Python packages installed:

- `pyshorteners`
- `pyperclip` (optional, for clipboard support)
- `requests`

You can install these dependencies using `pip`:

```bash
pip install pyshorteners
pip install pyperclip
pip install requests
```

## How to Use

1. **Clone the Repository**: Clone this repository to your local machine using:
   ```bash
   git clone https://github.com/Riya-2603/url-shortener.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd url-shortener
   ```

3. **Run the Script**:
   ```bash
   python shorten_url.py
   ```

4. **Input URL**: When prompted, enter the URL you want to shorten.

5. **Get Shortened URL**: The script will output the shortened URL.


1. **Importing pyshorteners**: The script imports the `pyshorteners` library which is used to shorten URLs.
   ```python
   import pyshorteners
   ```

2. **Shorten URL Function**: Defines a function `shorten_url` that takes a URL as input and returns a shortened URL using TinyURL.
   ```python
   def shorten_url(url):
       s = pyshorteners.Shortener()
       shortened_url = s.tinyurl.short(url)
       return shortened_url
   ```

3. **User Input**: Prompts the user to enter a URL.
   ```python
   url = input("Enter the URL: ")
   ```

4. **Get Shortened URL**: Calls the `shorten_url` function with the user-provided URL and prints the shortened URL.
   ```python
   shortened_url = shorten_url(url)
   print("Shortened URL:", shortened_url)
   ```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements

- [PyShorteners](https://github.com/ellisonleao/pyshorteners) for providing the URL shortening functionality.
