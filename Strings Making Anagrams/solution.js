'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the makeAnagram function below.
function makeAnagram(a, b) {
    
    let aArr = a.split('');
    let bArr = b.split('');
    let aObject = {};
    let bObject = {};
    let countForAna = 0;

    for(let i=0;i<aArr.length;i++){
        if(aArr[i] in aObject){
            aObject[aArr[i]]=aObject[aArr[i]]+1;
        } else {
            aObject[aArr[i]] = 1;
        }
    }

    for(let i=0;i<bArr.length;i++){
        if(bArr[i] in bObject){
            bObject[bArr[i]] = bObject[bArr[i]]+1;
        } else {
            bObject[bArr[i]] = 1;
        }
    }
    console.log(aObject);
    console.log(bObject);

    for(let key in aObject){
        if(key in bObject){
            countForAna = countForAna + (Math.min(aObject[key],bObject[key]) * 2 );
        }
    }

    return (aArr.length+bArr.length) - countForAna;


}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const a = readLine();

    const b = readLine();

    const res = makeAnagram(a, b);

    ws.write(res + '\n');

    ws.end();
}
