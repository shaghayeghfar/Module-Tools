const fs = require("fs");

const args = process.argv.slice(2);

let numberAllLines = false;
let numberNonBlankLines = false;
let startIndex = 0;
let lineNumber = 1;

// Check for flags
if (args[0] === "-n") {
  numberAllLines = true;
  startIndex = 1;
} else if (args[0] === "-b") {
  numberNonBlankLines = true;
  startIndex = 1;
}

// Read each file
for (let i = startIndex; i < args.length; i++) {
  let fileName = args[i];

  try {
    let content = fs.readFileSync(fileName, "utf8");

    let lines = content.split("\n");

    for (let j = 0; j < lines.length; j++) {
      let line = lines[j];

      if (numberAllLines) {
        console.log(lineNumber + " " + line);
        lineNumber++;
      } else if (numberNonBlankLines) {
        if (line.trim() === "") {
          console.log(line);
        } else {
          console.log(lineNumber + " " + line);
          lineNumber++;
        }
      } else {
        console.log(line);
      }
    }
  } catch (error) {
    console.log("Cannot read file: " + fileName);
  }
}
