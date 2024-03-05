
# Subtitle Translator

This script, crafted with care by Tharindu Madushan, leverages the powerful `googletrans` library to seamlessly translate subtitles from one language to another. It's designed to handle subtitle files (.srt), translating their content while preserving the original timing and formatting.

## Features

- **Automatic Translation**: Utilizes `googletrans` for effortless translation across languages supported by Google Translate.
- **Retries on Failure**: Built-in retry logic to handle temporary network issues or API limitations.
- **Progress Display**: Utilizes `tqdm` to show progress during translation, providing a visual indication of completion.
- **Flexible Language Selection**: Easily target translations to a specific language by modifying the destination language code.

## Requirements

To run this script, you'll need Python installed on your system along with the following libraries:
- `googletrans` for translation capabilities.
- `tqdm` for progress bar visualization.
- `re` for regular expression support, which is included with Python.

## Installation

First, ensure you have Python installed. Then, install the required packages using pip:

```bash
pip install googletrans==4.0.0-rc1 tqdm
```

> **Note**: The version of `googletrans` might change. Please check for the latest version compatible with this script.

## Usage

1. **Prepare Your Subtitle File**: Ensure your subtitle file is in the `.srt` format and encoded in UTF-8 to avoid any encoding issues.

2. **Set the Input and Output Paths**: Modify the `input_file_path` and `output_file_path` variables in the script to point to your source subtitle file and the desired output file location, respectively.

3. **Run the Script**: Execute the script with Python. Example:

```bash
python subtitle_translator.py
```

## How It Works

- The script initializes a `Translator` object from `googletrans`.
- It reads the source subtitle file line by line, identifying timestamps and text.
- Non-timestamp lines are translated using the `safe_translate` function, which retries failed translations up to a specified limit before giving up and leaving the text as-is.
- The translated text, along with unaltered timestamps, are written to the output file, preserving the original file's structure.

## Customization

- **Language Selection**: Change the `dest` parameter in the `safe_translate` function to translate to a different language (use ISO language codes, e.g., 'en' for English, 'si' for Sinhala).
- **Retry Logic**: Adjust the `retries` and `delay` parameters in the `safe_translate` function to change the retry behavior.

## Acknowledgments

Thanks to the developers of `googletrans` and `tqdm` for their fantastic libraries that made this script possible.

