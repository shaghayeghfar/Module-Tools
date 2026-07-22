const fs = require("fs");

const args = process.argv.slice(2);

let onePerLine = false;
let showHidden = false;
let path = "."; // Current directory by default

// Check for flags
for (let i = 0; i < args.length; i++) {
  if (args[i] === "-1") {
    onePerLine = true;
  } else if (args[i] === "-a") {
    showHidden = true;
  } else {
    path = args[i];
  }
}

try {
  // Check if the path is a file
  if (fs.statSync(path).isFile()) {
    console.log(path);
  } else {
    let files = fs.readdirSync(path);

    // Print each file
    for (let i = 0; i < files.length; i++) {
      let file = files[i];

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
