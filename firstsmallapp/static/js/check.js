const email=document.getElementById("email")
const password=document.getElementById('password')
const form=document.getElementById('from')
const password_2=document.getElementById('password2')


form.addEventListener("submit",(e)=>{
    let message=[]
    console.log("message")
    if (email.value===""&&password.value===""){
    message.push(1)
    }
    if (email.value==""){
        message.push(2)
    }
    if (password.value==""){
        message.push(3)
    }
    console.log(message)
    for (let r=0;r<message.length;r++) {
        if (message[r] == 1) {
            let s = document.getElementById("errormail")
            s.classList.add("alert", "alert-danger")
            s.innerText = "vous avez rien entrer!"
        }
        //console.log(message.includes(1))
        if (!message.includes(1)){
            if (message[r] == 2) {
                let s = document.getElementById("errormail")
                s.classList.add("alert", "alert-danger")
                s.innerText = "vous avez oubliez votre email"
            } else {
                let s = document.getElementById("errormail")
                s.classList.remove("alert", "alert-danger")
                s.innerText = ""
            }
        if (message[r] == 3 ) {
            console.log("ok")
            let s = document.getElementById("errorpass")
            s.classList.add("alert", "alert-danger")
            s.innerText = "vous avez oubliez votre mots de pass"
        } else {
            let s = document.getElementById("errorpass")
            s.classList.remove("alert", "alert-danger")
            s.innerText = ""
        }
        if (message[r] == 4 ) {
            console.log("ok")
            let s = document.getElementById("errorpass")
            s.classList.add("alert", "alert-danger")
            s.innerText = ""
        } else {
            let s = document.getElementById("errorpass")
            s.classList.remove("alert", "alert-danger")
            s.innerText = ""
        }
    }

    }

    if (message.length!=0) {
        e.preventDefault()
    }

})