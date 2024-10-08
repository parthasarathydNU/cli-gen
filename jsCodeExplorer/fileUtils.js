const fs = require('fs').promises;
const path = require('path');

async function* walkDir(dir) {

    const files = await fs.readdir(dir);

    for (const file of files) {

        const filePath = path.join(dir, file);

		if(filePath.includes("node_modules")){
			continue;
		}

        const stat = await fs.stat(filePath);

        if (stat.isDirectory()) {

            yield* walkDir(filePath);

        } else if (path.extname(file) === '.js' || path.extname(file) === '.jsx' || path.extname(file) === '.ts' || path.extname(file) === '.tsx') {

            yield filePath;

        }
    }

}

async function readFile(filePath) {
	const filePromise = fs.readFile(filePath);

	try{
		return filePromise
		.then(
			result => {
				return result.toString();
			}
		).catch((error) => {
			console.info(`Error in readFile function ${error}`);
			throw new Error(`Error in readFile function ${error}`);
		})

	} catch ( error ){
		throw new Error(`Error caught in try catch readFile ${error}`)
	}
}

async function writeToFile(filePath, content){

	try{
		return fs.writeFile(filePath, JSON.stringify(content)).then(() => {
			return `\nASTs written to ${filePath} successfully\n`;
		});
	} catch (error) {
		throw new Error(`Error writing asts to file ${filePath}`);
	}

}

module.exports = {readFile, walkDir, writeToFile}
