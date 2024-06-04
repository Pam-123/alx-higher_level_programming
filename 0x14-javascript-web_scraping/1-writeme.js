#!/usr/bin/env node

const fs = require('fs');

// Get the file path and string to write from the arguments
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Write the string to the file in utf-8 encoding
fs.writeFile(filePath, stringToWrite, 'utf8', (err) => {
    if (err) {
        // If an error occurred during writing, print the error object
        console.log(err);
        return;
    }
    // Optional: Print a success message
    console.log(`Successfully wrote to ${filePath}`);
});
