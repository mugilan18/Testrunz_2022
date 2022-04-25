import React, { useEffect, useState } from 'react';
import TextField from "@mui/material/TextField";

import Autocomplete from '@mui/material/Autocomplete';

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
import { useParams } from "react-router-dom";
import ApiUrl from '../../../../../ServerApi';
function not(a, b) {
  return a.filter((value) => b.indexOf(value) === -1);
}

function intersection(a, b) {
  return a.filter((value) => b.indexOf(value) !== -1);
}

function union(a, b) {
  return [...a, ...not(b, a)];
}

function Manageindividual2() {
  let { token } = useParams()
  const [options1, setOptions1] = useState();
  const [options2, setOptions2] = useState();
  const [options3, setOptions3] = useState();
  const [role, setRole] = useState("");

  const [checked, setChecked] = React.useState([]);
  const [left, setLeft] = React.useState();
  const [right, setRight] = React.useState([]);

  const leftChecked = intersection(checked, left);
  const rightChecked = intersection(checked, right);
  const [department, setDepartment] = useState("");
  const [college, setCollege] = useState("");
  const [loadingscreen, setLoadingscreen] = useState(true)
  const [lab, setLab] = useState([]);
  //   let {token} = useParams()
  const [detail, setDetail] = useState()
  //   const [lab, setLab] = useState([])
  const [id, setId] = useState("")
  useEffect(() => {
    fetch(`${ApiUrl}/moreInfo/all/college`)
      .then(response => response.json())
      .then(data => {
        console.log(data)
        setOptions1(data.ids)


      });


    fetch(`${ApiUrl}/api/users/${token}`)
      .then((res) => res.json())
      .then(data => {
        setDetail(data)
        setId(data._id)
        setRole(data.role)
      })
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

  const savesdasd = () => {


    console.log(id)
    console.log(college)
    console.log(department)
    console.log(right)
    console.log(role)
    if (id == "" || null) {
      alert("id")
    }
    else if (college == "" || null) {
      alert("college")
    }
    else if (department == "" || null) {
      alert("department")
    }
    else if (right == "" || null) {
      alert("right")
    }
    else if (role == "" || null) {
      alert("role")
    }
    else {
      fetch(`${ApiUrl}/api/tooglelab/admin`, {
        method: "PATCH",

        body: JSON.stringify({
          id: id,
          college: college,
          department: department,
          labtype: right,
          role: role,


        }),
        headers: {
          "Content-type": "application/json; charset=UTF-8"
        }
      })
        .then(response => response.json())
        .then(json => {

          // setOptions2(json.ids)

          console.log(json)
        }
        );
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
          width: 200,
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
              <ListItemText id={labelId} primary={value + 1} />
            </ListItem>
          );
        })}
        <ListItem />
      </List>
    </Card>
  );














  return (
    <div className="App">
      {detail ?
        <div>
          <h6> Name : {detail.name} </h6><br /> <br />
          <h6> Email : {detail.email} </h6><br />
          <h6> Role : {detail.role} </h6><br />
          {detail.labtype ?
            <>
              lab: <ul> {

                detail.labtype.map((lab, index) => {
                  return (
                    <li >
                      {lab}
                    </li>
                  );
                })}
              </ul>
            </> : null}




          <br />
          <br />
          {/* {console.log("hello",options)} */}
          {options1 ?
            <>
              <label> College :</label>
              <Autocomplete
                id="outlined-basic"
                variant="outlined"
                value={college}
                onChange={(event, newValue) => {

                  fetchdepartment(newValue)
                }}

                options={options1.map((option) => option)}

                // options={options}
                sx={{ width: 300 }}
                renderInput={(params) => <TextField {...params} />}
              />
            </>
            :
            null}


          {options2 ?
            <>
              <label> Department :</label>
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



          {left ?
            <>
              <label> Labs :</label>
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


          <Button onClick={savesdasd} variant='contained' style={{ backgroundColor: "#F1C232", color: "black" }}>Save</Button>
        </div>
        : null}
    </div>
  );
}

export default Manageindividual2;
