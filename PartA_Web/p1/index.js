let Price =0;
console.log("Hello")
function calculate() {
    let res = Price;
    console.log(Price)
    document.getElementById("ans").removeAttribute("hidden")
    document.getElementById("res").innerHTML = res;
    alert("Please pay "+res)
    
}
function addItem(){
    var price = document.getElementById("selectlevel1").value;
    var qty = document.getElementById("qty").value;
    Price+= (price*qty);
    console.log(Price);
}