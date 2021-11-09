const email=document.getElementById("exampleInputEmail1")
const password=document.getElementById("exampleInputPassword1")
const form =document.getElementById("formme")
//document.getElementById("error").innerText("sdadsa")
console.log(email)
//if (email){
 //  let x=1
//}
console.log(form)
form.addEventListener("submit",(e) =>{
   // document.getElementById("error").innerHTML="dsadsa"
    let message=[]
    console.log(email)
    if (email.value==""){
        message.push(1)
    }
    if (password.value==""){
        message.push(2)
    }
    console.log(message)


    for (let i=0;i<message.length;i++){
        if (message[i]==1){
           let s= document.getElementById("errormail")
            s.classList.add("alert","alert-danger")
            s.innerText="vous avez oubliez votre email"
        }
        if (message[i]==2){
            let s= document.getElementById("errorpass");
            s.classList.add("alert","alert-danger")
            s.innerText="vous avez oubliez votre mots de pass"
            //document.getElementById("error").innerText(<div className="alert alert-danger">
          //      <strong>Danger!</strong> no password
          //  </div>)
        }
    }
if (message.length!=0) {
        e.preventDefault()
    }
})