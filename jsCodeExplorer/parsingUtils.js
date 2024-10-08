const parser = require('@babel/parser');

function generateAst(fileContents) {
    try {
        return parser.parse(fileContents, {
            sourceType: 'unambiguous',
            plugins: ['jsx', 'typescript', 'decorators-legacy']
        });
    } catch (error) {
        console.error('Error parsing file:', error);
        return null;
    }
}

module.exports = { generateAst };
