/*
The function Change String(str) needs to modify the string passed using the
following rules:
• Replace every letter in the string with the letter that follows it in alphabetical order (ie.
Z becomes a, l becomes m).
• Take every vowel in this new string (a, e, i, o, u) and Capitalize it.
• Return this modified string. 
*/

//65-90 97-123
function changeString(str){
    return str.replace(/[a-zA-Z]/g,function(c){
        let s = c.charCodeAt(0) === 90 ? 97 : c.charCodeAt(0) === 123? 65 : c.charCodeAt(0) + 1;
        return String.fromCharCode(s);
    }).replace(/[aeiou]/g,function(match){
        return match.toUpperCase();
    })
}
function changestring(){
    let str = document.getElementById("id").value;
    let conv = changeString(str)
    document.getElementById("ans").innerHTML = conv;

}
console.log(changeString("Hello"))

/*
return str.replace(/[a-zA-z]/g,function(c){
    let s = c.charCodeAt(0) === 90 ? 97 : c.charCodeAt(0) === 123?65:c.charCodeAt(0)+1;
    return String.fromCharCode(s);
}).replace(/[aeiou]/g,function(match){
    return match.toUpperCase();
})
}
*/