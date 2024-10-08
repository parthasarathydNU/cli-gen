# AST Generator CLI

AST Generator is a command-line tool that generates Abstract Syntax Trees (ASTs) for JavaScript files in a specified directory. It processes all JavaScript files recursively in the given directory and provides a sample output of the generated ASTs.

## Features

- Recursively processes all JavaScript files in a given directory
- Generates ASTs using @babel/parser
- Provides a sample output of the first three ASTs
- Reports the total number of JavaScript files processed

## Installation

1. Ensure you have Node.js installed on your system (version 12 or higher recommended).

2. Clone this repository or download the source code:
   ```
   git clone git@github.com:parthasarathydNU/cli-gen.git
   cd ast-generator-cli/jsCodeExplorer
   ```

3. Install the dependencies:
   ```
   npm install
   ```

4. Make the CLI globally available:
   ```
   npm link
   ```

## Usage

After installation, you can use the AST Generator CLI from anywhere in your terminal:

```
ast-generator <directory_path>
```

Replace `<directory_path>` with the absolute path to the directory containing JavaScript files you want to analyze.

Example:
```
ast-generator /path/to/your/project
```

## Output

The tool will provide the following output:

- Confirmation that AST generation has started
- Sample AST output for up to three JavaScript files (first 500 characters of each AST)
- Total number of JavaScript files processed
- Error messages if any issues occur during processing

To understand the output generated refer to [Understanding the Output](./UnderstandingAstOutput.md)

## Dependencies

- @babel/parser: For generating ASTs from JavaScript code
- fs.promises: For asynchronous file operations
- path: For handling file paths

## Contributing

Contributions to the AST Generator CLI are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Troubleshooting

If you encounter any issues:

1. Ensure you have the latest version of Node.js installed.
2. Check that you have the necessary permissions to read the directory you're analyzing.
3. If you get a "command not found" error, try running `npm link` again in the project directory.

For any other issues, please open an issue on the GitHub repository.

## Future Enhancements

- Add support for TypeScript files
- Implement options for different output formats (e.g., JSON, YAML)
- Add filtering options to process only specific file types or patterns
