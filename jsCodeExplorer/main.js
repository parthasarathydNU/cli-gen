#!/usr/bin/env node

const { walkDir, readFile } = require('./fileUtils');
const { generateAst } = require('./parsingUtils');

async function generateAstsForDirectory(directoryPath) {
    const asts = {};

    for await (const filePath of walkDir(directoryPath)) {
        const fileContents = await readFile(filePath);
        if (fileContents) {
            const ast = generateAst(fileContents);
            if (ast) {
                asts[filePath] = JSON.stringify(ast);
            }
        }
    }

    return asts;
}

async function main() {
    // Get the directory path from command line arguments
    const directoryPath = process.argv[2];

    if (!directoryPath) {
        console.error('Error: Please provide a directory path.');
        console.log('Usage: node main.js <directory_path>');
        process.exit(1);
    }

    try {
        console.log(`Generating ASTs for directory: ${directoryPath}`);
        const generatedAsts = await generateAstsForDirectory(directoryPath);
        
        console.log('AST generation complete. Printing sample results:');
        const astEntries = Object.entries(generatedAsts);
        if (astEntries.length === 0) {
            console.log('No JavaScript files found in the specified directory.');
        } else {
            astEntries.slice(0, 3).forEach(([filePath, astDump]) => {
                console.log(`AST for ${filePath}:`);
                console.log(astDump.substring(0, 500));  // Print first 500 characters of each AST
                console.log('\n' + '='.repeat(50) + '\n');
            });
            console.log(`Total JavaScript files processed: ${astEntries.length}`);
        }
    } catch (error) {
        console.error('An error occurred:', error);
        process.exit(1);
    }
}

main();
