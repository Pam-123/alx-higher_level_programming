#!/usr/bin/env node

const fs = require('fs');

// Get the file path from the first argument
const filePath = process.argv[2];

// Read the file content in utf-8 encoding
fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        // If an error occurred during reading, print the error object
        console.log(err);
        return;
    }
    // Print the content of the file
    console.log(data);
});
