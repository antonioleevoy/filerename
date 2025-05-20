
# filerename

**filerename** is a simple Python script for batch-renaming files in a specified directory. It helps streamline the process of organizing files by allowing pattern-based name changes, prefix/suffix addition, and more.

## Features

- Rename multiple files in bulk
- Add or remove prefixes and suffixes
- Replace parts of filenames using custom rules
- Command-line interface for easy use

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/antonioleevoy/filerename.git
   cd filerename
   ```

2. (Optional) Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

### Usage

1. Run the script:

   ```bash
   python filerename.py
   ```

2. Follow the prompts to:
   - Enter the path to the directory containing the files
   - Define the renaming logic (e.g., add prefix, suffix, or replace text)

> **Note**: Always review the output or test in a sample directory to prevent unwanted renaming.

## Example

Original files:
```
image1.jpg
image2.jpg
```

Using a prefix "holiday_":

```
holiday_image1.jpg
holiday_image2.jpg
```

## License

This project is licensed under the MIT License.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
