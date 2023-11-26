#!usr/bin/env node
const Int = parseInt(process.argv[2]);
if (Number.isNaN(Int))
{
    console.log("Not a number");
}
else
{
    console.log("My number: " + Int);
}
