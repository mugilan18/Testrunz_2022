import React, { useEffect, useState } from 'react'
import ApiUrl from '../../../../../ServerApi';
import ApiService from '../../../../../Sevices/ApiService';
import { useStateValue } from '../../../../../data/StateProvider';
import MaterialTable from 'material-table'
import Lodaing from '../../Lodaing';
import { Link, useHistory } from "react-router-dom";
import ModeEditIcon from '@mui/icons-material/ModeEdit';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';
import { BiEditAlt } from 'react-icons/bi';

import { Grid } from '@material-ui/core';
import MenuItem from '@mui/material/MenuItem';
import FormHelperText from '@mui/material/FormHelperText';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import DeleteOutlineIcon from '@mui/icons-material/DeleteOutline';

const ManageModal = (props) => {
  const [{ user }, dispatch] = useStateValue();
  let row = []
  const USER_API_BASE_URL = `${ApiUrl}/api/alluser`
  const [userlist, setUserlist] = useState()
  const [loadingscreen, setLoadingscreen] = useState(true)
  const [update, setUpdate] = useState(true)
  const [editrole, setEditrole] = useState(true)
  const [editcollegename, setEditcollegename] = useState(true)
  const [editcountry, setEditcountry] = useState(true)
  const [editdepartment, setEditdepartment] = useState(true)
  const [editstate, setEditstate] = useState(true)
  const [edityear, setEdityear] = useState(true)
  const [editsemester, setEditsemester] = useState(true)
  const [editlabtype, setEditlabtype] = useState(true)
  const [lab, setLab] = useState()
  const [role, setRole] = useState()
  const [college, setCollege] = useState()
  const [options1, setOptions1] = useState()
  const [country, setCountry] = useState()
  const [lablist, setLablist] = useState()
  const [year, setYear] = useState()
  const [semester, setSemester] = useState()
  const [state, setState] = useState()
  const [newlab, setNewlab] = useState()
  const history = useHistory()

  const columns = [
    { title: "ID", field: "_id", editable: 'never' },
    { title: "Name", field: "name", editable: 'never' },
    { title: "Email", field: "email", editable: 'never' },
    { title: "Role", field: "role", lookup: { superadmin: "Super Admin", admin: "Admin", teacher: "Teacher", student: "Student" } },
    { title: "Country", field: "country", editable: 'never' },
    { title: "College Name", field: "collegeName", editable: 'never' },
  ];

  const [open, setOpen] = React.useState(false);
  // const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);
  const [detail, setDetail] = useState()

  useEffect(()=>{
    console.log(props.selectedid)
    fetch(`${ApiUrl}/api/users/${props.selectedid}`)
        .then((res)=>res.json())
        .then(data =>{
          setDetail(data)
          setLab(data.labtype)
          setRole(data.role)
          setCollege(data.college)
          setCountry(data.country)
          setYear(data.year)
          setSemester(data.semester)
          setState(data.state)
         
        })
  },[])


  useEffect(() => {
    fetch(`${ApiUrl}/api/getaccess`, {
      method: "POST",
      body: JSON.stringify({
        role: user.role
      }),
      headers: {
        "Content-type": "application/json; charset=UTF-8"
      }
    })
      .then(response => response.json())
      .then(json => {
        setUserlist(json)
        console.log(json)
      }
      );
    console.log(userlist)
    setLoadingscreen(false)
  }, [update]);


  /// fetch lab

  const fetchlab = () => {

     const fetchlbs=()=>{
    fetch(`${ApiUrl}/moreInfo/labs/depandclg`, {
      method: "POST",
      body: JSON.stringify({
        department: detail.department,
        college: detail.college
      }),
      headers: {
        "Content-type": "application/json; charset=UTF-8"
      }
    })
      .then(response => response.json())
      .then(json => {

        // setOptions2(json.ids)
        console.log("json hekkp asdsad")
        console.log(user.role, typeof user.role)
        setLablist(json.ids)
        console.log(json)

      }
      )
     }

     if(user.role == "superadmin"){
      fetchlbs()
      console.log("heloo suoper")
    }
      else{
        console.log("list user")
        setLablist(user.labtype)
        console.log("heloo hai")
      }
  }



  /// college fetch
  const fetchcollege = () => {
    fetch(`${ApiUrl}/moreInfo/all/college`)
      .then(response => response.json())
      .then(data => {
        console.log(data)
        setOptions1(data.ids)


      });
  }
  /// filter lab 
  const filter = (labname) => {

    let templab = [...lab].filter((lab1) => lab1 !== labname);
    setLab(templab);
  }

  /// college lab
  // const fetchlab=()=>{
  //   fetch(`${ApiUrl}/moreInfo/all/college`)
  //   .then(response => response.json())
  //   .then(data => {
  //     console.log(data)
  //     setOptions1(data.ids)


  //   });
  // }
  /// patch details
  const patchsingle = (tag, value, id) => {
    fetch(`${ApiUrl}/api/tooglelab/admin`, {
      method: "PATCH",
      body: JSON.stringify({
        [tag]: value,
        id: id
      }),
      headers: {
        "Content-type": "application/json; charset=UTF-8"
      }
    })
      .then(response => response.json())
      .then(json => {
        alert("done")
        console.log(json)
        setUpdate(!update)
      }
      );
    // console.log( value)

  }

  const edituser = async (userId) => {
    setOpen(true)
    fetch(`${ApiUrl}/api/users/${userId}`)
      .then((res) => res.json())
      .then(data => {
        setDetail(data)
        setLab(data.labtype)
        setRole(data.role)
        setCollege(data.college)
        setCountry(data.country)
        setYear(data.year)
        setSemester(data.semester)
        setState(data.state)

      })
    // history.push(`/manageuser/${userId}`);

  };
  const edituseradmin = async (userId) => {
    // history.push(`/manageuseradmin/${userId}`);
    setOpen(true)
    fetch(`${ApiUrl}/api/users/${userId}`)
      .then((res) => res.json())
      .then(data => {
        setDetail(data)
        setRole(data.role)
        setCollege(data.college)
        setCountry(data.country)
        setYear(data.year)
        setSemester(data.semester)
        setState(data.state)
        setLab(data.labtype)

      })
  };

  return (
    <div>

      {detail ?
        <>
          {/* {detail.name} <Link>edit <ModeEditIcon fontSize="small"/></Link> */}
          <tr>
            <th colspan="3">Name</th>
            <th>Age</th>
          </tr>
          <br />

          <tr>
            <td>Name</td>
            <td>{detail.name}</td>
            <td><Button disabled><BiEditAlt /></Button></td>
          </tr>

          <br />
          <tr>
            <td>Email</td>
            <td>{detail.email}</td>
            <td><Button disabled><BiEditAlt /></Button> </td>
          </tr>
          <br />

          <tr >
            <td >Role: </td>
            <td >{editrole ?
              detail.role :
              <>
                {user.role == "superadmin" ?
                  <Select
                    labelId="demo-simple-select-disabled-label"
                    id="demo-simple-select-disabled"
                    value={role}
                    label="Role"
                    size="small"
                    onChange={(e) => setRole(e.target.value)}
                  >
                    <MenuItem value={"superadmin"}>Super Admin</MenuItem>
                    <MenuItem value={"admin"}>Admin</MenuItem>
                    <MenuItem value={"teacher"}>Teacher</MenuItem>
                    <MenuItem value={"student"}>Student</MenuItem>

                  </Select> : null}
                {user.role == "admin" ?
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

                  </Select> : null}

                {user.role === "teacher" || user.role === "student" ?
                  <Select
                    labelId="demo-simple-select-disabled-label"
                    id="demo-simple-select-disabled"
                    value={role}
                    label="Role"
                    size="small"
                    onChange={(e) => setRole(e.target.value)}
                  >
                    <MenuItem value={"student"}>Student</MenuItem>

                  </Select> : null}

                <Button onClick={e => patchsingle("role", role, detail._id)}>Update</Button>
              </>
            }</td >
            <td ><Button onClick={() => setEditrole(!editrole)}>{editrole ? <><BiEditAlt /></> : <>cancel</>}</Button></td>
          </tr>
          <br />


          <tr>
            <td >College Name: </td>
            <td >{editcollegename ? detail.collegeName : <>
              {options1 ?
                <>
                  <Autocomplete
                    id="outlined-basic"
                    variant="outlined"
                    size="small"
                    value={college}
                    onChange={(event, newValue) => {
                      setCollege(newValue)
                    }}
                    options={options1.map((option) => option)}
                    sx={{ width: 300 }}
                    renderInput={(params) => <TextField {...params} />}
                  />
                  <Button>Update</Button>
                </> : null
              }
            </>}</td >
            <td >{user.role == "superadmin" ?
              <Button onClick={() => { setEditcollegename(!editcollegename); fetchcollege() }}>{editcollegename ? <><BiEditAlt /></> : <>cancel</>}</Button>
              : <Button disabled><BiEditAlt /></Button>}
            </td>
          </tr>
          <br />

          <tr >
            <td >country: {country} </td>
            <td >{editcountry ? detail.country : <><input value={country} onChange={e => setCountry(e.target.value)}></input><Button onClick={() => patchsingle("country", country, detail._id)}>Update</Button></>}</td >
            <td ><Button onClick={() => setEditcountry(!editcountry)}>{editcountry ? <><BiEditAlt /></> : <>cancel</>}</Button></td>
          </tr>
          <br />

          <tr >
            <td >department: </td>
            <td >{editdepartment ? detail.department : <><input></input><Button>Update</Button></>}</td >
            <td ><Button onClick={() => setEditdepartment(!editdepartment)}>{editdepartment ? <><BiEditAlt /></> : <>cancel</>}</Button></td>
          </tr>
          <br />
          {detail.role == "student" ?
            <tr >
              <td >Year: </td >
              <td >{edityear ? detail.year : <>
                <Select
                  labelId="demo-simple-select-disabled-label"
                  id="demo-simple-select-disabled"
                  value={year}
                  label="Role"
                  size="small"
                  onChange={(e) => setYear(e.target.value)}
                >
                  <MenuItem value={1}>1</MenuItem>
                  <MenuItem value={2}>2</MenuItem>
                  <MenuItem value={3}>3</MenuItem>
                  <MenuItem value={4}>4</MenuItem>
                </Select>
                <Button>Update</Button></>}</td >
              <td ><Button onClick={() => setEdityear(!edityear)}>{edityear ? <><BiEditAlt /></> : <>cancel</>}</Button></td>
            </tr> : null}
          <br />

          <tr >
            <td >State:</td >
            <td >{editstate ? detail.state : <>
              <input value={state} onChange={e => setState(e.target.value)}></input>
              <Button onClick={e => patchsingle("state", state, detail._id)}>Update</Button></>}</td >
            <td ><Button onClick={() => setEditstate(!editstate)}>{editstate ? <><BiEditAlt /></> : <>cancel</>}</Button></td>
          </tr>
          <br />
          {detail.role == "student" ?
            <tr >
              <td >Semester: </td >
              <td >{editsemester ? detail.semester : <>
                <Select
                  labelId="demo-simple-select-disabled-label"
                  id="demo-simple-select-disabled"
                  value={year}
                  label="Role"
                  size="small"
                  onChange={(e) => setYear(e.target.value)}
                >
                  <MenuItem value={1}>1</MenuItem>
                  <MenuItem value={2}>2</MenuItem>
                  <MenuItem value={3}>3</MenuItem>
                  <MenuItem value={4}>4</MenuItem>
                  <MenuItem value={5}>5</MenuItem>
                  <MenuItem value={6}>6</MenuItem>
                  <MenuItem value={7}>7</MenuItem>
                  <MenuItem value={8}>8</MenuItem>

                </Select>
                <Button>Update</Button></>}</td >
              <td ><Button onClick={() => setEditsemester(!editsemester)}>{editsemester ? <><BiEditAlt /></> : <>cancel</>}</Button></td>
            </tr> : null}
          <br />

          {detail.labtype ?
            <>
              <tr><td >list </td><td > Labs available</td>
                <td ><Button onClick={() => { setEditlabtype(!editlabtype); fetchlab() }}>{editlabtype ? <><BiEditAlt /></> : <>cancel</>}</Button></td>
              </tr>
              {editlabtype ? null :

                lablist ? <><Autocomplete
                  size="small"
                  onChange={(event, newValue) => {
                    setNewlab(newValue)
                  }}
                  options={(lablist).map((option) => option)}
                  sx={{ width: 300 }}
                  renderInput={(params) => <TextField {...params} />}
                />
                  <Button onClick={() => {
                    let sendlab = [...lab, newlab]
                    patchsingle("labtype", sendlab, detail._id)
                  }
                  }>update</Button></> : null
              }
              {lab ?
                lab.map(lab =>
                  <div key={lab} ><span>{lab}</span> &nbsp;&nbsp;&nbsp;&nbsp; {editlabtype ? null : <DeleteOutlineIcon color='error' onClick={() => filter(lab)} />}</div>)
                : null

              } <br />
            </>
            :
            null}
        </> : <>Loading...</>}

    </div>
  )
}

export default ManageModal