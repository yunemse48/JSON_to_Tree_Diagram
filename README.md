# Tree Diagram Generator

## Project Description

This project is a Python-based tool for generating tree diagrams from structured JSON data. It uses NetworkX and Matplotlib for creating and visualising the tree structures, making it suitable for analysing and presenting hierarchical data.

## Features

- Generate tree diagrams from JSON data.
- Customisable layout and presentation.
- Support for visualising complex hierarchical structures.

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Dependencies

Install the required Python packages:

The `requirements.txt` file includes the following packages:

- networkx
- matplotlib

### Graphviz Installation

For advanced graph layouts with `pygraphviz`, install Graphviz:

- **Windows**: Download and install from [Graphviz's website](https://graphviz.org/download/).
  - Installation via `conda` is highly recommended on Windows! 
- **MacOS**: Use Homebrew with `brew install graphviz`.
- **Linux (Ubuntu/Debian)**: Use `sudo apt install graphviz`.

## Usage

To generate a tree diagram:

1. Prepare your JSON data representing the hierarchical structure.
2. Run the script with the JSON data.
3. The script will generate and display the tree diagram.

### Sample Screenshots
**Single Branch** (properties off)
![Figure_1](https://github.com/yunemse48/JSON_to_Tree_Diagram/assets/60715607/e4fa7905-1348-44bf-992f-d7b2105c4dfe)

**Multiple Branch** (properties on)
![Figure_2](https://github.com/yunemse48/JSON_to_Tree_Diagram/assets/60715607/384486cf-2207-4a8f-8878-621a769c640e)

## Customization

You can customise the tree diagram by modifying the script. The script allows for adjustments in the layout, node properties, and more.

## Contributing

Contributions to this project are welcome! Feel free to fork the repository and submit pull requests.

## License

This project is open source and available under the [MIT License](LICENSE).
