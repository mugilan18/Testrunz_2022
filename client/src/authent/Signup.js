import React, { useState } from 'react'
import { auth } from "./firebase";
import { useHistory, Link } from "react-router-dom";
import "./signup.css"
import template from "./template.png"
import Button from '@mui/material/Button';
import Alert from '@mui/material/Alert';
import Snackbar from '@mui/material/Snackbar';

const Signup = () => {
  const [email, setEmail] = useState("")
  const [emailerror, setEmailerror] = useState()
  const [password, setPassword] = useState("")
  const [passworderror, setPassworderror] = useState()
  const [confirmpassword, setConfirmpassword] = useState("")
  const [confirmpassworderror, setConfirmpassworderror] = useState()
  const [mismatch, setMismatch] = useState()
  const [name, setName] = useState("")
  const [nameerror, setNameerror] = useState()
  const history = useHistory()
  const [open, setOpen] = React.useState(false);
  const [open1, setOpen1] = React.useState(false);
  const [statusmessage, setStatusmessage] = useState("")
  const vertical ="button"
  const horizontal = "center"



  const handleClose = (event, reason) => {
    if (reason === 'clickaway') {
      return;
    }
    setOpen(false);
    setOpen1(false)
  };





  const authsignup = (e) => {
    e.preventDefault()
  console.log(email,name, password,confirmpassword)
  
    // setEmailerror()
    // setNameerror()
    setPassworderror()
    setConfirmpassworderror()
  if (!name ) {
      console.log("no name")
      setNameerror("*Name required*")
    }
    else if(nameerror){
      console.log(nameerror)
    }
    else if(emailerror){
      console.log(emailerror)
    }
  else if (!email) {
    console.log("no email")
    setEmailerror("*Email required*")
  } 
  else if (!password) {
    console.log("no password")
    setPassworderror("*Password required*")
  }
 
  else if (!confirmpassword) {
    console.log("no cpassword")
    setConfirmpassworderror("*Confirm password required*")
  }
  else {

     if (password === confirmpassword) {

      auth.createUserWithEmailAndPassword(email, password)
        .then((userCredential) => {

          console.log("successfully Registered", userCredential)

          fetch(`${process.env.REACT_APP_API}/register`, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              email: email,
              name: name
            }),
          }).then(response => response.json())
            .then(data => {
              setOpen1(true);

              window.setTimeout(() => {
                history.push('/signin')
              }, 3000)
            })
            .catch((error) => {
              console.error('Error:', error);
              setStatusmessage("Database not created")
              setOpen(true);
            });
        })
        .catch((error) => {
          var errorCode = error.code;
          var errorMessage = error.message;
          console.log("Failure1", errorMessage)
          console.log("Failure2", errorCode)
          setStatusmessage(errorMessage)
          setOpen(true);
        });
    }
    else {
      setStatusmessage("password is not same")
      setOpen(true);
      setMismatch("Check Confirm passord")
    }

  }
 
 

    
   
  }
  return (
    <div>

      <section>
        <div className="container">
          <div className="user signinupBx">
            <div className="formBx">
              <form >
                <h2>Create an account</h2>

                <input
                  onChange={(e) => {setName(e.target.value)
                    if(/[`!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~1234567890]/.test(e.target.value)){
                      setNameerror("*No Special Character Allowed*")
                    }
                    else {
                      setNameerror()
                    }
                  } }
                  type="text"
                  placeholder="Username"
                  value={name}
                  required
                />
                <p className='errormsg'>{nameerror}</p>

                <input
                  onChange={e => {
                    setEmail(e.target.value)
                    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(e.target.value)) {
                      setEmailerror()
                    }
                    else {
                      setEmailerror("*Invalid Email account*")
                    }
                  }}
                  type="email"
                  placeholder="Email Address"
                  value={email}
                  required
                />
                <p className='errormsg'>{emailerror}</p>
                <input
                  onChange={e => setPassword(e.target.value)}
                  type="password"
                  placeholder="Create Password"
                  value={password}
                  required
                />
                <p className='errormsg'>{passworderror}</p>
                <input
                  onChange={e => setConfirmpassword(e.target.value)}
                  type="password"
                  placeholder="Confirm Password"
                  value={confirmpassword}
                  required
                />
                <p className='errormsg'>{confirmpassworderror}</p>
                <p className='errormsg'>{mismatch}</p>
                
                <Button  variant="contained" style={{background:"#3F51B"}}  onClick={authsignup}>Submit</Button>
                <p className="signinup">
                  Already have an account ?
                  <Link to="/signin" className="card-link" > Sign in.</Link>
                </p>
              </form>
            </div>
            <div className="imgBx"><img src={template} alt="" /></div>
          </div>
          <Snackbar open={open} autoHideDuration={3000} onClose={handleClose} anchorOrigin={{ vertical, horizontal }}>
            <Alert onClose={handleClose} severity="error" sx={{ width: '100%' }}>
              {statusmessage}
            </Alert>
          </Snackbar>

          <Snackbar open={open1} autoHideDuration={3000} onClose={handleClose} anchorOrigin={{ vertical, horizontal }}>
            <Alert onClose={handleClose} severity="success" sx={{ width: '100%' }}>
              signup Successful!
            </Alert>
          </Snackbar>

        </div>
      </section>


    </div>
  )
}

export default Signup



