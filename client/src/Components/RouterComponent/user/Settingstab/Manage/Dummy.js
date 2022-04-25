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

const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 1000,
  height:700,
  bgcolor: 'background.paper',
  border: '2px solid #000',
  boxShadow: 24,
  p: 4,
};

const Manageusertable = () => {
  const [{ user }, dispatch] = useStateValue();
  let row = []
  const USER_API_BASE_URL = `${ApiUrl}/api/alluser`
  const [userlist, setUserlist] = useState()
  const [loadingscreen, setLoadingscreen] = useState(true)
  const [update, setUpdate] = useState(true)
  const [editrole, setEditrole] = useState(true)
  const [editcollegename, setEditcollegename] = useState(true)
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
  const[detail,setDetail]=useState()



  useEffect(() => {

    fetch(`${ApiUrl}/api/getaccess`, {
      method: "POST",
   
      body: JSON.stringify({
      role:user.role
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8"
    }
  })
  .then(response => response.json())
  .then(json => 
    {
      setUserlist(json)
      console.log(json)
   
    }
    );
    console.log(userlist)
    setLoadingscreen(false)

  }, [update]);


  const edituser = async (userId) => {
    setOpen(true)
    fetch(`${ApiUrl}/api/users/${userId}`)
    .then((res)=>res.json())
    .then(data =>{
      setDetail(data)
     
    })
    // history.push(`/manageuser/${userId}`);

  };
  const edituseradmin = async (userId) => {
    // history.push(`/manageuseradmin/${userId}`);
    setOpen(true)
    fetch(`${ApiUrl}/api/users/${userId}`)
    .then((res)=>res.json())
    .then(data =>{
      setDetail(data)
     
    })
  };

  
  return (
    <div>
      {loadingscreen ?
        <Lodaing /> :
        user.role==="superadmin"?
        <>
        {/* <Button onClick={handleOpen}>Open modal</Button> */}
<Modal
  open={open}
  onClose={handleClose}
  aria-labelledby="modal-modal-title"
  aria-describedby="modal-modal-description"
>
  <Box sx={style}>
   {detail?
   <>
   {/* {detail.name} <Link>edit <ModeEditIcon fontSize="small"/></Link> */}
   
  Name: {detail.name} <br/><br/>

  Email: {detail.email} <br/><br/>

  <Grid container direction="row" justifyContent="space-evenly" alignItems="center">
  <Grid item>Role: </Grid>
  <Grid item>{editrole?
  detail.role:
<>
<input></input>
<Button>Update</Button>
</>
}</Grid >
  <Grid item><Button variant="contained" onClick={()=>setEditrole(!editrole)}>{editrole?<>edit<BiEditAlt/></>:<>cancel</>}</Button></Grid>
  </Grid>
  <br/>
  

  <Grid container direction="row" justifyContent="space-evenly" alignItems="center"
  ><Grid item>College Name: </Grid>
  <Grid item>{editcollegename?
  detail.collegeName:
<>
<input></input>
<Button>Update</Button>
</>
}
  
  </Grid >
  <Grid item><Button variant="contained" onClick={()=>setEditcollegename(!editcollegename)}>{editcollegename?<>edit<BiEditAlt/></>:<>cancel</>}</Button></Grid>
  </Grid>
  <br/>
  <Grid container direction="row" justifyContent="space-between" alignItems="center"><Grid item>country: {detail.country}</Grid ><Grid item><Link >edit<BiEditAlt/></Link></Grid></Grid><br/>
  <Grid container direction="row" justifyContent="space-between" alignItems="center"><Grid item>department: {detail.department}</Grid ><Grid item><Link >edit<BiEditAlt/></Link></Grid></Grid><br/>
  <Grid container direction="row" justifyContent="space-between" alignItems="center"><Grid item>Year: {detail.role}</Grid ><Grid item><Link >edit<BiEditAlt/></Link></Grid></Grid><br/>
  <Grid container direction="row" justifyContent="space-between" alignItems="center"><Grid item>State: {detail.state}</Grid ><Grid item><Link >edit<BiEditAlt/></Link></Grid></Grid><br/>
  <Grid container direction="row" justifyContent="space-between" alignItems="center"><Grid item>Semester: {detail.semester}</Grid ><Grid item><Link >edit<BiEditAlt/></Link></Grid></Grid><br/>
   {detail.labtype?
   <>
     <Grid container direction="row" justifyContent="space-between" alignItems="center"><Grid item>Labtype:</Grid><Grid item><Link>edit<BiEditAlt/></Link></Grid></Grid>
    {
     detail.labtype.map(lab => <div key={lab} 
    >{lab}</div>)
   
   } <br/>
</>
:
   null}
   </>:<>Loading...</>}
  </Box>
</Modal>
        <MaterialTable
          columns={columns}
          data={userlist}
          title="List Of User Super Admin"
          options={{
            actionsColumnIndex: -1, grouping: true, pageSizeOptions: [5, 10, 15], pageSize: 10, headerStyle: {
              zIndex: 0
            },
            // rowStyle: (data, index) => data.role == "admin" ?
            //   { backgroundColor: '#EEE' } : { backgroundColor: '#FFF' }
          }}
          onRowClick={(e, data) => edituseradmin(data._id)}
        />
        </>:
        <MaterialTable
        columns={columns}
        data={userlist}
        title="List Of User "
        options={{
          actionsColumnIndex: -1, grouping: true, pageSizeOptions: [5, 10, 15], pageSize: 10, headerStyle: {
            zIndex: 0
          },
          // rowStyle: (data, index) => data.role == "admin" ?
          //   { backgroundColor: '#EEE' } : { backgroundColor: '#FFF' }
        }}
        onRowClick={(e, data) => edituser(data._id)}
      />
      
      
      }
      

    </div>
  )
}

export default Manageusertable