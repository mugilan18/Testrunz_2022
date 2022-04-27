import React, { useEffect, useState } from 'react'
import TextField from '@mui/material/TextField';
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
const Adduser = () => {
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
    setNameerror()
    setEmailerror()
    setRoleerror()
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
    else if (!email) {
      console.log("no email")
      setEmailerror("*Email required*")
    }
    else if (!role) {
      console.log("no role")
      setRoleerror("*Role required*")
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
            }),
          }).then(response => response.json())
            .then(data => {
              setOpen1(true);
              /// send email
              axios.post(process.env.REACT_APP_API + "/usermail", usermail)
                .then((res) => {
                  console.log(res.data)
                  if (res.data == "error") {
                    Swal.fire({
                      icon: 'error',
                      title: 'Oops...',
                      text: 'Check the Email or internet connection',

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
              setEmail("")
              setName("")
              setRole("")
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
  }

  // const createuser = (e) => {
  //   e.preventDefault();
  //   console.log(role)
  // }

  return (
    <div>
      <Grid container spacing={2} columns={16}>
        <Grid item xs={8}>
        </Grid>
        <Grid item xs={8}>

        </Grid>
      </Grid>
      <label>Name : </label>
      <TextField
        onChange={e => setName(e.target.value)}
        id="outlined-size-small"
        size="small"
        value={name}
      />
      <br />
      <p className='errormsg'>{nameerror}</p>
      <br />
      <label>email : </label>
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
      <br />
      <label>Role : </label>
      {/* ////////////////////////////////////////////////////////////////////////////////////////// */}
      {user.role==="superadmin"?
      <FormControl sx={{ m: 1, minWidth: 120 }} >
        <InputLabel id="demo-simple-select-disabled-label">Role</InputLabel>
        <Select
          labelId="demo-simple-select-disabled-label"
          id="demo-simple-select-disabled"
          value={role}
          label="Role"
          size="small"
          onChange={(e) => setRole(e.target.value)}
        >
          <MenuItem value={"admin"}>Admin</MenuItem>
          <MenuItem value={"teacher"}>Teacher</MenuItem>
          <MenuItem value={"student"}>Student</MenuItem>

        </Select>
       
      </FormControl>
      :null}
      {/* ///////////////////////////////////////////////////////////////////////////////////////////////////// */}


      {/* ////////////////////////////////////////////////////////////////////////////////////////// */}
      {user.role==="admin"?
      <FormControl sx={{ m: 1, minWidth: 120 }} >
        <InputLabel id="demo-simple-select-disabled-label">Role</InputLabel>
        <Select
          labelId="demo-simple-select-disabled-label"
          id="demo-simple-select-disabled"
          value={role}
          label="role"
          onChange={(e) => setRole(e.target.value)}
        >

          <MenuItem value={"teacher"}>Teacher</MenuItem>
          <MenuItem value={"student"}>Student</MenuItem>

        </Select>
        
      </FormControl>
      :null}
      {/* ///////////////////////////////////////////////////////////////////////////////////////////////////// */}


      {/* ////////////////////////////////////////////////////////////////////////////////////////// */}
      {user.role==="teacher"?
      <FormControl sx={{ m: 1, minWidth: 120 }} >
        <InputLabel id="demo-simple-select-disabled-label">Role</InputLabel>
        <Select
          labelId="demo-simple-select-disabled-label"
          id="demo-simple-select-disabled"
          value={role}
          label="Role"
          onChange={(e) => setRole(e.target.value)}
        >
          <MenuItem value={"student"}>Student</MenuItem>

        </Select>
   
      </FormControl>
      :null}
      {/* ///////////////////////////////////////////////////////////////////////////////////////////////////// */}

      <p className='errormsg'>{roleerror}</p>




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

export default Adduser