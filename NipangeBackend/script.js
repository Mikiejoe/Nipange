async function getusers() {
    const res = await fetch("http://127.0.0.1:8000/api/users/getuser/40d8bffe/");
    const users = await res.json();
    console.log(users)
}

const email = document.getElementById('email')
const pass = document.getElementById('pass')
const phone = document.getElementById('phone')
const fname = document.getElementById('fname')
const lname = document.getElementById('lname')
const uname = document.getElementById('uname')
const sbtn = document.getElementById('sbtn')
const lbtn = document.getElementById('lbtn')
form = document.getElementById('form')
message = document.getElementById('message')

// sbtn.addEventListener('click', (e) => {
//     e.preventDefault();
//     var fdata = {
//         username: uname.value,
//         firstname: fname.value,
//         lastname: lname.value,
//         password: pass.value,
//         phone: phone.value,
//         email: email.value

//     }
//     postdata("http://localhost:8000/api/users/create_user/", fdata).then((data)=> {
//         console.log(data)
//         message.innerText = data["message"];
//     });
// })

async function postdata(url, data) {
    const res = await fetch(url, {
        method: "POST",
        mode: "cors",
        cache: "no-cache",
        headers: { "content-type": "application/json" },
        body: JSON.stringify(data)
    })
    return res.json();
}

lbtn.addEventListener("click", (e) => {
  e.preventDefault();
  var fdata = {
    password: pass.value,
    email: email.value,
  };
  postdata("http://localhost:8000/api/users/login/", fdata).then(
    (data) => {
      console.log(data);
      message.innerText = data["message"];
    }
  );
});


