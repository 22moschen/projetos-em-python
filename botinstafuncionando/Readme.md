# Instagram Comment Bot

This project is a Python script that automatically logs in to your Instagram account and posts comments on a specified post.

## Prerequisites

This script requires Python 3.6+ and a few Python packages which are listed in the `requirements.txt` file.

In order to run the script, you will also need to download the ChromeDriver executable (compatible with the version of Google Chrome installed on your computer) and place it in the same directory as the script.

## Installation

1. Clone this repository or download it as a ZIP file and extract it.

2. Open a terminal/command prompt and navigate to the directory where the script is located.

3. Install the required Python packages using pip:

pip install -r requirements.txt


4. Download the correct version of ChromeDriver from the official [website](https://sites.google.com/a/chromium.org/chromedriver/) and place it in the script directory.

## Usage

1. Open the `instagram_comment_bot.py` script in a text editor.

2. Replace `'username'` and `'password'` in the `main` function with your Instagram login credentials.

3. Adjust the `webdriver_service` variable in the `main` function to the correct path of your 'chromedriver' executable.

4. If you wish to comment on a different post, replace the `post_url` variable with the URL of your desired Instagram post.

5. You can also customize the comment text by changing the `comment` variable.

6. Save the changes and close the text editor.

7. In the terminal/command prompt, run the script:

python instagram_comment_bot.py


The script will log in to your Instagram account and start posting comments on the specified post.

## Important Note

Please keep in mind that Instagram updates its website from time to time. Consequently, some elements on the page may change, causing the script to not work as expected. 

If the script fails to find a specific element, the likely cause is that Instagram has updated the website and the elements' identifiers (XPATH, CSS selectors, etc.) have changed. 

To solve this issue, you can inspect the website (right-click on the web page, then click "Inspect") and identify the new identifiers for the updated elements. Then, replace the old identifiers in the script with the newly found ones.

Here's an example of how to locate an element's XPath:

```plaintext
1. Right-click on the web page and select "Inspect" to open Chrome Developer Tools.
2. In the Elements tab, you can see the HTML content of the page. 
3. Hover over the HTML elements in the Elements tab and Chrome will highlight the corresponding part of the web page. 
4. Once you find the element you're interested in, right-click on that element in the Elements tab and select "Copy" -> "Copy XPath". 
5. Replace the old XPath in the script with the one you've just copied.

Remember, the key to maintaining this script functional is to adjust it according to Instagram's updates.

## Note

Please use this script responsibly and respect Instagram's Community Guidelines. Also, keep in mind that extensive use of this script could lead to your account being rate-limited or banned by Instagram.

## Disclaimer

This project is for educational purposes only. The author is not responsible for any consequences resulting from the use of this script.
