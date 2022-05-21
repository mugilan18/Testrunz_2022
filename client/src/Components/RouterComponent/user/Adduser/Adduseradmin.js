import React, { useEffect, useState } from 'react'
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import { Button } from '@mui/material';
import Grid from '@mui/material/Grid';
import Alert from '@mui/material/Alert';
import Snackbar from '@mui/material/Snackbar';
import { auth } from '../../../../authent/firebase';
import axios from 'axios';
import Swal from 'sweetalert2'
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormHelperText from '@mui/material/FormHelperText';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import { useStateValue } from '../../../../data/StateProvider';
const Adduseradmin = () => {
  const [email, setEmail] = useState("")
  const [role, setRole] = useState("")
  const [roleerror, setRoleerror] = useState()
  const [{ user }, dispatch] = useStateValue();
  const [emailerror, setEmailerror] = useState()
  const [name, setName] = useState("")
  const [nameerror, setNameerror] = useState()
  const [open, setOpen] = React.useState(false);
  const [open1, setOpen1] = React.useState(false);
  const [password, setPassword] = useState("")
  const [statusmessage, setStatusmessage] = useState("")
  const [lab, setLab] = useState("")
  const vertical = "button"
  const horizontal = "center"



  const handleClose = (event, reason) => {
    if (reason === 'clickaway') {
      return;
    }
    setOpen(false);
    setOpen1(false)
  };

  useEffect(() => {
    function randomStr(len) {
      var arr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
      var ans = '';
      for (var i = len; i > 0; i--) {
        ans +=
          arr[Math.floor(Math.random() * arr.length)];
      }
      return ans;
    }
    setPassword(randomStr(8))
console.log(user)
  }, [])

  const createuser = (e) => {
    e.preventDefault();
    // setNameerror()
    // setEmailerror()
    setRoleerror()
    console.log(name)
    console.log(email)
    console.log(user.collegeName)
    console.log(user.department)
    console.log("lab",lab)
    console.log(role)
    console.log("this is password", password)
    let usermail = {
      name: name,
      email: email,
      password: password
    }
    if (!name) {
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
    else if (!role) {
      console.log("no role")
      setRoleerror("*Role required*")
    }
    else if (!lab) {
      alert("add lab")
    }
    else {
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
              name: name,
              role:role,
              collegeName:user.collegeName,
              department:user.department,
              labtype:lab
            }),
          }).then(response => response.json())
            .then(data => {
              setOpen1(true);
              console.log("created",data)
              Swal.fire(
                'User Created',
                'User has been Created successfully',
                'success'
              )

              /// send email
              axios.post(process.env.REACT_APP_API + "/usermail", usermail)
                .then((res) => {
                  console.log(res.data)
                  if (res.data == "error") {
                    Swal.fire({
                      icon: 'error',
                      title: 'Oops...',
                      text: 'Created with invalid email',

                    })
                  }
                  else {
                    console.log("mail sent successfully.");


                    Swal.fire(
                      'User Created',
                      'User has been Created and password is sent through mail',
                      'success'
                    )


                  }
                })
              //////////////
              setEmail()
              setName()
              setRole()
              setLab()
            })
            .catch((error) => {
              console.error('Error:', error);
              Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'User not registered contact testrunz developer',
              })
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
          Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Authentication failed',
          })
        });
    }
  }

  return (
    <div>
      
     <div>
      <label>Name:&nbsp;&nbsp;</label>
      <TextField
        id="outlined-size-small"
        size="small"
        value={name}
        onChange={(e) => {setName(e.target.value)
          if(/[`!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~1234567890]/.test(e.target.value)){
            setNameerror("*No Special Character Allowed*")
          }
          else {
            setNameerror()
          }
        } }
      />
      <p className='errormsg'>{nameerror}</p>
      </div>
      <br/>
     
      <div>
      <label>Email:&nbsp;&nbsp;</label>
      <TextField
        onChange={e => {
          setEmail(e.target.value)
          if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(e.target.value)) {
            setEmailerror()
          }
          else {
            setEmailerror("*Invalid Email account*")
          }
        }}
        id="outlined-size-small"
        size="small"
        value={email}
      />
      <br />
      <p className='errormsg'>{emailerror}</p>
      </div>
      <br/>

     <div>
      <label>College:&nbsp;&nbsp; </label>
      <TextField
        disabled
        id="outlined-size-small"
        size="small"
        value={user.collegeName}
      />
      </div>
      <br/>

  <div>
<label>Department:&nbsp;&nbsp;</label>
      <TextField
        disabled
        id="outlined-size-small"
        size="small"
        value={user.department}
      />

</div>
<br/>




<div>
<label>Role:&nbsp;&nbsp;</label>
      <FormControl sx={{ m: 1, minWidth: 120 }} >
      
        <Select
          // labelId="demo-simple-select-disabled-label"
          // id="demo-simple-select-disabled"
          value={role}
          onChange={(e) => setRole(e.target.value)}
          size="small"
        >
          <MenuItem value={"teacher"}>Teacher</MenuItem>
          <MenuItem value={"student"}>Student</MenuItem>

        </Select>
       
      </FormControl>
      </div >
      <p className='errormsg'>{roleerror}</p>
      <br/>



<div>

{
  user.labtype ? 
<>

     <label>Lab:</label>
      <Autocomplete
      // disablePortal
      // id="combo-box-demo"
      value={lab}
      size="small"
      onChange={(event, newValue) => {
      
        setLab(newValue)
      }}
      options={(user.labtype).map((option) => option)}
      sx={{ width: 300 }}
      renderInput={(params) => <TextField {...params}  />}
    />
</>
: null}
 

    
      </div>
      <br/>



      <Button variant='contained' style={{ backgroundColor: "#F1C232", color: "black" }} onClick={createuser}>Create user</Button>
      <Snackbar open={open} autoHideDuration={3000} onClose={handleClose} anchorOrigin={{ vertical, horizontal }}>
        <Alert onClose={handleClose} severity="error" sx={{ width: '100%' }}>
          {statusmessage}
        </Alert>
      </Snackbar>

      <Snackbar open={open1} autoHideDuration={3000} onClose={handleClose} anchorOrigin={{ vertical, horizontal }}>
        <Alert onClose={handleClose} severity="success" sx={{ width: '100%' }}>
          user created Successfully !
        </Alert>
      </Snackbar>
    </div>
  )
}

export default Adduseradmin;