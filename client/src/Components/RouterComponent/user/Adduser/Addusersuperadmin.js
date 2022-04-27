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
    console.log(right)
    console.log(college)
    console.log(department)
    console.log("this is password", password)

    if (name === "" || null) {
      alert("no name")
      // setNameerror("*Name required*")
    }
    else if (email === "" || null) {
      alert("no email")
      // setEmailerror("*Email required*")
    }
    else if (role === "" || null) {
      alert("no role")
      // setRoleerror("*Role required*")
    }
    else if (right == "" || null) {
      alert("no lab")
      // setNameerror("*Name required*")
    }
    else if (college === "" || null) {
      alert("no college")
      // setEmailerror("*Email required*")
    }
    else if (department === "" || null) {
      alert("no department")
      // setRoleerror("*Role required*")
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
                      'Runz has beed Created and password is sent through mail',
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
              // setStatusmessage("Database not created")
              // setOpen(true);
            });
        })
        .catch((error) => {
          var errorCode = error.code;
          var errorMessage = error.message;
          console.log("Failure1", errorMessage)
          console.log("Failure2", errorCode)
          // setStatusmessage(errorMessage)
          // setOpen(true);
        });
    }
  }



  const handleToggle = (value) => () => {
    const currentIndex = checked.indexOf(value);
    const newChecked = [...checked];

    if (currentIndex === -1) {
      newChecked.push(value);
    } else {
      newChecked.splice(currentIndex, 1);
    }

    setChecked(newChecked);
  };

  const numberOfChecked = (items) => intersection(checked, items).length;

  const handleToggleAll = (items) => () => {
    if (numberOfChecked(items) === items.length) {
      setChecked(not(checked, items));
    } else {
      setChecked(union(checked, items));
    }
  };

  const handleCheckedRight = () => {
    setRight(right.concat(leftChecked));
    setLeft(not(left, leftChecked));
    setChecked(not(checked, leftChecked));
  };

  const handleCheckedLeft = () => {
    setLeft(left.concat(rightChecked));
    setRight(not(right, rightChecked));
    setChecked(not(checked, rightChecked));
  };



  const customList = (title, items) => (
    <Card>
      <CardHeader
        sx={{ px: 2, py: 1 }}
        avatar={
          <Checkbox
            onClick={handleToggleAll(items)}
            checked={numberOfChecked(items) === items.length && items.length !== 0}
            indeterminate={
              numberOfChecked(items) !== items.length && numberOfChecked(items) !== 0
            }
            disabled={items.length === 0}
            inputProps={{
              'aria-label': 'all items selected',
            }}
          />
        }
        title={title}
        subheader={`${numberOfChecked(items)}/${items.length} selected`}
      />
      <Divider />
      <List
        sx={{
          width: 320,
          height: 230,
          bgcolor: 'background.paper',
          overflow: 'auto',
        }}
        dense
        component="div"
        role="list"
      >
        {items.map((value) => {
          const labelId = `transfer-list-all-item-${value}-label`;

          return (
            <ListItem
              key={value}
              role="listitem"
              button
              onClick={handleToggle(value)}
            >
              <ListItemIcon>
                <Checkbox
                  checked={checked.indexOf(value) !== -1}
                  tabIndex={-1}
                  disableRipple
                  inputProps={{
                    'aria-labelledby': labelId,
                  }}
                />
              </ListItemIcon>
              <ListItemText id={labelId} primary={value} />
            </ListItem>
          );
        })}
        <ListItem />
      </List>
    </Card>
  );














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
        onChange={(e) => setName(e.target.value)} 
      />
</div> 
<br/>


<div>
      <label>email :&nbsp;&nbsp; </label>
      <TextField
        onChange={e => {
          setEmail(e.target.value)
        }}
        id="outlined-size-small"
        size="small"
        value={email}
      />
</div>
<br/>

<div>
      <label> role :&nbsp;&nbsp;</label>
      <FormControl sx={{ m: 1, minWidth: 120 }} >
      
        <Select
          // labelId="demo-simple-select-disabled-label"
          // id="demo-simple-select-disabled"
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
              fetchdepartment(newValue)
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
            value={department}
            onChange={(event, newValue) => {
              fetchlab(newValue)
              console.log(newValue)
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
          <Grid container spacing={2} justifyContent="center" alignItems="center">
            <Grid item>{customList('Choices', left)}</Grid>
            <Grid item>
              <Grid container direction="column" alignItems="center">
                <Button
                  sx={{ my: 0.5 }}
                  variant="outlined"
                  size="small"
                  onClick={handleCheckedRight}
                  disabled={leftChecked.length === 0}
                  aria-label="move selected right"
                >
                  &gt;
                </Button>
                <Button
                  sx={{ my: 0.5 }}
                  variant="outlined"
                  size="small"
                  onClick={handleCheckedLeft}
                  disabled={rightChecked.length === 0}
                  aria-label="move selected left"
                >
                  &lt;
                </Button>
              </Grid>
            </Grid>
            <Grid item>{customList('Chosen', right)}</Grid>
          </Grid>
        </>

        :
        null}


      <Button onClick={createuser} variant='contained' style={{ backgroundColor: "#F1C232", color: "black" }}>Create User</Button>
    </div>
  );
}

export default Addusersuperadmin;
