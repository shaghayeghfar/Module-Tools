const fs = require("fs");

// Get arguments after "node wc.js"
const args = process.argv.slice(2);

let countLines = false;
let countWords = false;
let countBytes = false;

let files = [];

// Read arguments
for (let arg of args) {
  if (arg === "-l") {
    countLines = true;
  } else if (arg === "-w") {
    countWords = true;
  } else if (arg === "-c") {
    countBytes = true;
  } else {
    files.push(arg);
  }
}

// If no flags are given, wc shows all three
if (!countLines && !countWords && !countBytes) {
  countLines = true;
  countWords = true;
  countBytes = true;
}

// Function to count one file
function countFile(fileName) {
  const content = fs.readFileSync(fileName, "utf8");

  let lines = content.split("\n").length - 1;

  let words = content
    .trim()
    .split(/\s+/)
    .filter((word) => word.length > 0).length;

  let bytes = Buffer.byteLength(content);

  let result = "";

  if (countLines) {
    result += lines + " ";
  }

  if (countWords) {
    result += words + " ";
  }

  if (countBytes) {
    result += bytes + " ";
  }

  result += fileName;

  console.log(result);
}

// Run wc for every file

for (let file of files) {
  countFile(file);
}
