const fs = require("fs");

const args = process.argv.slice(2);

let onePerLine = false;
let showHidden = false;
let paths = [];

// Check for flags
for (let i = 0; i < args.length; i++) {
  if (args[i] === "-1") {
    onePerLine = true;
  } else if (args[i] === "-a") {
    showHidden = true;
  } else {
    paths.push(args[i]);
  }
}

// Use current directory if no path is given
if (paths.length === 0) {
  paths.push(".");
}

for (let i = 0; i < paths.length; i++) {
  let path = paths[i];

  try {
    // Check if the path is a file
    if (fs.statSync(path).isFile()) {
      console.log(path);
    } else {
      let files = fs.readdirSync(path);

      // Sort files like ls command
      files.sort();

      // Print each file
      for (let j = 0; j < files.length; j++) {
        let file = files[j];

        // Skip hidden files unless -a is used
        if (!showHidden && file.startsWith(".")) {
          continue;
        }

        if (onePerLine) {
          console.log(file);
        } else {
          process.stdout.write(file + " ");
        }
      }

      if (!onePerLine) {
        console.log();
      }
    }
  } catch (error) {
    console.log("Cannot access: " + path);
  }
}
