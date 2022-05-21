import React, { useEffect, useState } from 'react';
import TextField from "@mui/material/TextField";

import Autocomplete from '@mui/material/Autocomplete';
import MenuItem from '@mui/material/MenuItem';
import FormHelperText from '@mui/material/FormHelperText';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import Grid from '@mui/material/Grid';
import List from '@mui/material/List';
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import ListItemIcon from '@mui/material/ListItemIcon';
import Checkbox from '@mui/material/Checkbox';
import Button from '@mui/material/Button';
import Divider from '@mui/material/Divider';

import { auth } from '../../../../authent/firebase';
import axios from 'axios';
import Swal from 'sweetalert2'

import ApiUrl from '../../../../ServerApi';


import CheckBoxOutlineBlankIcon from '@mui/icons-material/CheckBoxOutlineBlank';
import CheckBoxIcon from '@mui/icons-material/CheckBox';

const icon = <CheckBoxOutlineBlankIcon fontSize="small" />;
const checkedIcon = <CheckBoxIcon fontSize="small" />;

function not(a, b) {
  return a.filter((value) => b.indexOf(value) === -1);
}

function intersection(a, b) {
  return a.filter((value) => b.indexOf(value) !== -1);
}

function union(a, b) {
  return [...a, ...not(b, a)];
}

function Addusersuperadmin() {
  const [options1, setOptions1] = useState();
  const [options2, setOptions2] = useState();
  const [options3, setOptions3] = useState();

  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [role, setRole] = useState("");
  const [emailerror, setEmailerror] = useState()
  const [nameerror, setNameerror] = useState()

  const [checked, setChecked] = React.useState([]);
  const [left, setLeft] = React.useState();
  const [right, setRight] = React.useState([]);
  const [password, setPassword] = useState("")
  const leftChecked = intersection(checked, left);
  const rightChecked = intersection(checked, right);
  const [department, setDepartment] = useState("");
  const [college, setCollege] = useState("");
  useEffect(() => {
    fetch(`${ApiUrl}/moreInfo/all/college`)
      .then(response => response.json())
      .then(data => {
        console.log(data)
        setOptions1(data.ids)


      });

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
  }, [])






  const fetchlab = (aa) => {
    console.log("heheheeh", aa)
    setDepartment(aa)
    setRight([])
    setLeft()
    fetch(`${ApiUrl}/moreInfo/labs`, {
      method: "POST",

      body: JSON.stringify({
        department: aa
      }),
      headers: {
        "Content-type": "application/json; charset=UTF-8"
      }
    })
      .then(response => response.json())
      .then(json => {

        // setOptions2(json.ids)
        setLeft(json.ids)
        console.log(json)

      }
      );
  }

  const fetchdepartment = (aa) => {

    setCollege(aa)
    setDepartment()
  
    fetch(`${ApiUrl}/moreInfo/department`, {
      method: "POST",

      body: JSON.stringify({
        college: aa
      }),
      headers: {
        "Content-type": "application/json; charset=UTF-8"
      }
    })
      .then(response => response.json())
      .then(json => {

        setOptions2(json.ids)

        console.log(json)
      }
      );
  }



  const createuser = (e) => {
    // e.preventDefault();
    // setNameerror()
    // setEmailerror()
    // setRoleerror()
    console.log(name)
    console.log(email)
    console.log(role)
    console.log("right",right)
    console.log(college)
    console.log(department)
    console.log("this is password", password)

    if (!name) {
      alert("no name")
      // setNameerror("*Name required*")
    }
    else if(nameerror){
      console.log("check name") 
      }
    else if (!email) {
      alert("no email")
      // setEmailerror("*Email required*")
    }
    else if(emailerror){
    console.log("check mail id") 
    }
    else if (!role) {
      alert("no role")
      // setRoleerror("*Role required*")
    }
    else if (!college) {
      alert("no college")
      // setEmailerror("*Email required*")
    }
    else if (!department) {
      alert("no department")
      // setRoleerror("*Role required*")
    }
    else if (!right.length) {
      alert("no lab")
      // setNameerror("*Name required*")
    }
    
    
    else {
      let usermail = {
        name: name,
        email: email,
        password: password
      }
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
              role: role,
              labtype: right,
              collegeName: college,
              department: department,
            }),
          }).then(response => response.json())
            .then(data => {
              // setOpen1(true);
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
              setCollege()
              setDepartment()
              setRight()
              // setLab()
            })
            .catch((error) => {
              console.error('Error:', error);
              // setStatusmessage("Database not created")
              // setOpen(true);
              Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'User not registered contact testrunz developer',
              })
            });
        })
        .catch((error) => {
          var errorCode = error.code;
          var errorMessage = error.message;
          console.log("Failure1", errorMessage)
          console.log("Failure2", errorCode)
          Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Authentication failed',
          })
          // setStatusmessage(errorMessage)
          // setOpen(true);
        });
    }
  }



  return (
    <div >
{/* <Grid
  container
  direction="column"
  justifyContent="space-around"

  alignItems="stretch"
> */}
<div>
      <label> Name :&nbsp;&nbsp; </label>
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
      <label>Email :&nbsp;&nbsp; </label>
      <TextField
        onChange={e => {
          setEmail(e.target.value)
          if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(e.target.value)) {
            setEmailerror()
          }
          else {
            setEmailerror("*Invalid Email accounts*")
          }
        }}
        id="outlined-size-small"
        size="small"
        value={email}
      />
<p className='errormsg'>{emailerror}</p>
</div>
<br/>

<div>
      <label> Role :&nbsp;&nbsp;</label>
      <FormControl sx={{ m: 1, minWidth: 120 }} >
      
        <Select
          value={role}
          size="small"
          onChange={(e) => setRole(e.target.value)}
        >
          <MenuItem value={"admin"}>Admin</MenuItem>
          <MenuItem value={"teacher"}>Teacher</MenuItem>
          <MenuItem value={"student"}>Student</MenuItem>

        </Select>
       
      </FormControl>
</div>
{/* </Grid */}
<br/>
<div>
      {options1 ?
        <>
          <label> College :&nbsp;&nbsp;</label><br/><br/>
          <Autocomplete
            id="outlined-basic"
            variant="outlined"
            size="small"
            value={college}
            onChange={(event, newValue) => {
              fetchdepartment(newValue);
              setDepartment()
            }}
            options={options1.map((option) => option)}
            sx={{ width: 300 }}
            renderInput={(params) => <TextField {...params} />}
          />
        </>
        :
        null}
</div>
<br/>
<div>
      {options2 ?
        <>
          <label> Department :&nbsp;&nbsp;</label><br/><br/>
          <Autocomplete
          size="small"
            value={department}
            onChange={(event, newValue) => {
              fetchlab(newValue)
              
            }}
            options={options2.map((option) => option)}
            id="controllable-states-demo"
            // options={options}
            sx={{ width: 300 }}
            renderInput={(params) => <TextField {...params} />}
          />
        </>
        :
        null}
</div>

<br/>
      {left ?
        <>
          <label> Labs :&nbsp;&nbsp;</label>
           <Autocomplete
      multiple
      id="checkboxes-tags-demo"
      options={left}
      disableCloseOnSelect
      getOptionLabel={(option) => option}
      onChange={(event,value)=>setRight(value)}
      renderOption={(props, option, { selected }) => (
        <li {...props}>
          <Checkbox
            icon={icon}
            checkedIcon={checkedIcon}
            style={{ marginRight: 8 }}
            checked={selected}
          />
          {option}
        </li>
      )}
      style={{ width: 500 }}
      renderInput={(params) => (
        <TextField {...params}   />
      )}
    />
        </>

        :
        null}


      <Button onClick={createuser} variant='contained' style={{ backgroundColor: "#F1C232", color: "black" }}>Create User</Button>
    </div>
  );
}

export default Addusersuperadmin;
