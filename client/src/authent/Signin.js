import React, { useState } from 'react'
import "./signup.css"
import template from "./template.png"
import Button from '@mui/material/Button';
import { auth } from "./firebase";
import { useHistory, Link } from "react-router-dom";
import { useStateValue } from '../data/StateProvider';
import { actionTypes } from "../data/reducer"
import { useCookies } from "react-cookie";
import axios from "axios";
import Alert from '@mui/material/Alert';
import Snackbar from '@mui/material/Snackbar';
import Google1 from "./Google1"
const Signin = () => {

  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const [{ user }, dispatch] = useStateValue();
  const history = useHistory()
  const [open, setOpen] = React.useState(false);
  const [open1, setOpen1] = React.useState(false);
  const [statusmessage, setStatusmessage] = useState("")
  const vertical ="button"
  const horizontal = "center"
  const [cookies, setCookie, removeCookie] = useCookies(["userjwt"]);
  const [emailerror, setEmailerror] = useState(false)
  const [passworderror, setPassworderror] = useState(false)


  const handleClose = (event, reason) => {
    if (reason === 'clickaway') {
      return;
    }
    setOpen(false);
    setOpen1(false)
  };

 




  const authsignin = () => {
    setEmailerror(false)
    setPassworderror(false)
    if(!email){
      setEmailerror(true)
    }
    else if(!password){
      setPassworderror(true)
    }
    else{
      setEmailerror(false)
    auth.signInWithEmailAndPassword(email, password)
      .then((userCredential) => {
        console.log("successfully signin")
        fetch(`${process.env.REACT_APP_API}/login`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            email: email,
          }),
        })
          .then(response => response.json())
          .then(data => {
            console.log('Success:', data.jwttoken);
            setCookie('userjwt', data.jwttoken, { path: '/' });
            axios.post(`${process.env.REACT_APP_API}/validateuser`, {
              usertoken: data.jwttoken
            })
            .then((res) => {
              console.log("here")
              dispatch({
                type: actionTypes.SET_USER,
                user: res.data.user
             });
             console.log("hello user")
             history.push("/private");
             });

          })
          .catch((error) => {
            console.error('Error:', error);
          });

      })
      .catch((error) => {
        var errorCode = error.code;
        var errorMessage = error.message;
        console.log("Failure1", errorCode)
        console.log("Failure2", errorMessage)
        setStatusmessage(errorMessage)
        setOpen(true);
      });
  }
}



  return (
    <div>
      <section>
        <div className="container">
          <div className="user signinupBx">
            <div className="imgBx"><img src={template} alt="" /></div>
            <div className="formBx">
              <form >
                <h2>Sign In</h2>
                <input
                  style={{  borderStyle:emailerror?"solid" :"none",
                    borderColor:emailerror?"#f1c232":"none",
                    borderRadius:emailerror?"5px":"none",
                  }}
                  onChange={e => setEmail(e.target.value)}
                  type="email"
                  value={email}
                  placeholder="Email"
                />
                <input
                style={{  borderStyle:passworderror?"solid" :"none",
                borderColor:passworderror?"#f1c232":"none",
                borderRadius:emailerror?"5px":"none",

              }}
                  onChange={e => setPassword(e.target.value)}
                  type="password"
                  placeholder="Password"
                  value={password}
                />
                
                <Button  variant="contained"  style={{background:"#3F51B"}} onClick={authsignin}>Submit</Button>
            
                <br/>
                <div className='divider'><strong className="or">or</strong> </div>
                <Google1/>
                <p className="signinup">
                  Don't have an account ?
                  <Link to="/signup" className="card-link" > Sign Up.</Link>
                </p>
                <br/>
                <br/>
                <p className="forget">
                <Link to="/forgot_password" className="card-link" > *Forgot Password ?</Link>
                </p>
                </form>
                </div>

              
          
          </div>
        </div>
        <Snackbar open={open} autoHideDuration={3000} onClose={handleClose} anchorOrigin={{ vertical, horizontal }}>
          <Alert onClose={handleClose} severity="error" sx={{ width: '100%' }}>
            {statusmessage}
          </Alert>
        </Snackbar>

        <Snackbar open={open1} autoHideDuration={3000} onClose={handleClose} anchorOrigin={{ vertical, horizontal }}>
          <Alert onClose={handleClose} severity="success" sx={{ width: '100%' }}>
            SignIn Successful!
          </Alert>
        </Snackbar>
      </section>

    </div>
  )
}

export default Signin






