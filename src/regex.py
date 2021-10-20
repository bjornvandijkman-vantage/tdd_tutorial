import re
import pandas as pd

df = pd.DataFrame(
    {
        "text": ["5 euro", "7 euro", "", "15 euro"],
        "row_number": [1, 2, 3, 4],
    }
)


def extract_money(text):
    """Extract monetary value from string by looking for
    a pattern of a digit, followed by 'euro'.
    e.g. 5 euro --> 5

    Args:
        text (str): Text containing monetary value

    Returns:
        float: The extracted value
    """

    if text:
        extracted_money = re.search(r"(\d) euro", text).group(1)
        return float(extracted_money)
    else:
        return None


df["money"] = df["text"].apply(lambda x: extract_money(x))
print(df)
