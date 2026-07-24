const fs = require("fs");

const args = process.argv.slice(2);

let numberAllLines = false;
let numberNonBlankLines = false;
let startIndex = 0;
let lineNumber = 1;

// Check for flags
for (let i = 0; i < args.length; i++) {
  if (args[i] === "-n") {
    numberAllLines = true;
    startIndex++;
  } else if (args[i] === "-b") {
    numberNonBlankLines = true;
    startIndex++;
  } else {
    break;
  }
}

// Read each file
for (let i = startIndex; i < args.length; i++) {
  let fileName = args[i];

  try {
    let content = fs.readFileSync(fileName, "utf8");

    // Remove the extra empty line if the file ends with "\n"
    let lines = content.endsWith("\n")
      ? content.slice(0, -1).split("\n")
      : content.split("\n");

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
