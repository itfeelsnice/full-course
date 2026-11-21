
let btn2 = document.querySelector("#btn2");
let btn3 = document.querySelector("#btn3");
let set1 = document.querySelector("#set1");

fetch("/check_cookie1").then(get1 => get1.text()).then(data1 =>{
    if (data1 === "set_cookie1"){
        set1.classList.add("add1");
        console.log("there is a cookie")
    }else if(data1 === "it_dosent_exist1"){
        console.log("there is no cookie")
    }
});

btn2.addEventListener("click", () =>{

    set1.classList.add("add1");

    fetch("/get_btn1", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            button_id1: "btn22"
        })
    });
});

btn3.addEventListener("click", () =>{
    set1.classList.add("add1");
});
