import React, { useEffect, useState } from 'react'
import ApiUrl from '../../../../../ServerApi';

import { useStateValue } from '../../../../../data/StateProvider';
import MaterialTable from 'material-table'
import Lodaing from '../../Lodaing';
import { Link, useHistory } from "react-router-dom";

import Box from '@mui/material/Box';
import { Button } from '@material-ui/core';

// import Modal from '@mui/material/Modal';
import { BiEditAlt } from 'react-icons/bi';
import Modal from "react-modal";

import { Grid } from '@material-ui/core';
import MenuItem from '@mui/material/MenuItem';

import Select from '@mui/material/Select';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import DeleteOutlineIcon from '@mui/icons-material/DeleteOutline';
import Adduser from '../../Adduser/Adduser';
import ManageModal from './ManageModal';

const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 1000,
  height:"70%",
  bgcolor: 'background.paper',
  border: '2px solid #000',
  boxShadow: 24,
  overflowY:'scroll',
  p: 4,
};

const customStyles = {
  content: {
    top: "50%",
    left: "50%",
    width: "50%",
    height: "70%",
    right: "auto",
    bottom: "auto",
    marginRight: "-50%",
    transform: "translate(-50%, -50%)",
    borderRadius: "2%",
  },
};

const customStylesbig = {
  content: {
    top: "50%",
    left: "50%",
    width: "100%",
    height: "100%",
    right: "auto",
    bottom: "auto",
    marginRight: "-50%",
    transform: "translate(-50%, -50%)",
    borderRadius: "2%",
  },
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
  const [editcountry, setEditcountry] = useState(true)
  const [editdepartment, setEditdepartment] = useState(true)
  const [editstate, setEditstate] = useState(true)
  const [edityear, setEdityear] = useState(true)
  const [editsemester, setEditsemester] = useState(true)
  const [modalOpenAdd, setModalOpenAdd] = useState(false);
  const [editlabtype,setEditlabtype]= useState(true)
  const [lab,setLab]=useState()
  const [role,setRole]=useState()
  const [college,setCollege]=useState()
  const [options1,setOptions1]=useState()
  const [options2,setOptions2]=useState()
  const [country,setCountry]=useState()
  const [lablist,setLablist]=useState()
  const [year,setYear]=useState()
  const [department,setDepartment]=useState()
  const [semester,setSemester]=useState()
  const [state,setState]=useState()
  const [newlab,setNewlab]=useState()
  const history = useHistory()
  const [useridnum,setUseridnum]=useState()

  

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
  const handleClose = () => {
  setOpen(false);
  setEditlabtype(true)
  setEditrole(true)
  setEditcollegename(true)
  setEditcountry(true)
  setEditdepartment(true)
  setEditstate(true)
  setEdityear(true)
  setEditsemester(true)
  setEditlabtype(true)
  }

  const[detail,setDetail]=useState()



  useEffect(() => {
console.log(user)
    fetch(`${ApiUrl}/api/getaccess`, {
      method: "POST",
   
      body: JSON.stringify({
      role:user.role,
      department:user.department,
      collegeName:user.collegeName
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

  }, [update,modalOpenAdd,open]);


  /// fetch lab

   const fetchlab=()=>{
     const fetchlbs=()=>{
      fetch(`${ApiUrl}/moreInfo/labs/depandclg`, {
        method: "POST",
        body: JSON.stringify({
          department: detail.department,
          college:detail.collegeName
        }),
        headers: {
          "Content-type": "application/json; charset=UTF-8"
        } 
      })
        .then(response => response.json())
        .then(json => {
  
          // setOptions2(json.ids)
          console.log("json hekk  kkkp")
          setLablist(json.ids)
          console.log(json)
          console.log( typeof user.role)
        }
        )
     }

     if(user.role =="superadmin"){
      fetchlbs()
    }
      else{
        console.log("list user")
        setLablist(user.labtype)
      }
 }   

/// department fetch
const fetchdepartment=(college)=>{
  console.log(college)
  fetch(`${ApiUrl}/moreInfo/department`, {
    method: "POST",

    body: JSON.stringify({
      college:college
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

/// college fetch
const fetchcollege=()=>{
  fetch(`${ApiUrl}/moreInfo/all/college`)
  .then(response => response.json())
  .then(data => {
    console.log(data)
    setOptions1(data.ids)


  });
}
/// filter lab 
const filter=(labname)=>{
 
    let templab = [...lab].filter((lab1) => lab1 !== labname);
    setLab(templab);
}


const patchsingle=(tag,value,id)=>{
  fetch(`${ApiUrl}/api/tooglelab/admin`, {
    method: "PATCH",
    body: JSON.stringify({
      [tag]:value,
      id:id
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
}

  const edituser = async (userId) => {
    setOpen(true)
    setUseridnum(userId)
  };
  const edituseradmin = async (userId) => {
    // history.push(`/manageuseradmin/${userId}`);
    setOpen(true)
    setUseridnum(userId)
  };


  // content for add user modal 
  const openModal = () =>   setModalOpenAdd(() => true);
  const closeModal = () => setModalOpenAdd(() => false);

  const closeeditModal = () => setOpen(() => false);




  return (
    <div>
      <Modal
  isOpen={open}
  appElement={document.getElementById('root')}
  style={customStylesbig}
  contentLabel="Manage User"
  disableBackdropClick="true"
  sx={{ overflow: 'hidden' }}
>
  
  <ManageModal useridnum={useridnum} closeeditModal={closeeditModal} />
  </Modal>
      {loadingscreen ?
        <Lodaing /> :
        
        user.role==="superadmin"?
        <>
      <Modal
        isOpen={modalOpenAdd}
        appElement={document.getElementById('root')}
        style={customStyles}
        contentLabel="add runz Modal"
        disableBackdropClick="true"
        sx={{ overflow: 'hidden' }}
        
      >
        <Adduser closeModal={closeModal} />
      </Modal>

        <MaterialTable
          columns={columns}
          data={userlist}
          title="List Of User"
          actions={[
            {
              icon: 'add',
              tooltip: 'Add User',
              isFreeAction: true,
              onClick:() => openModal()
            }]}
          options={{
            actionsColumnIndex: -1, grouping: true, pageSizeOptions: [5, 10, 15], pageSize: 10, headerStyle: {
              zIndex: 0
            },
          }}
          onRowClick={(e, data) => edituseradmin(data._id)}
        />
        </>:
        <>

<Modal
        isOpen={modalOpenAdd}
        appElement={document.getElementById('root')}
        style={customStyles}
        contentLabel="add runz Modal"
        disableBackdropClick="true"
        sx={{ overflow: 'hidden' }}
        
      >
        <Adduser  closeModal={closeModal} />
      </Modal>
        <MaterialTable
        columns={columns}
        data={userlist}
        title="List Of User"
        actions={[
          {
            icon: 'add',
            tooltip: 'Add User',
            isFreeAction: true,
            onClick:() => openModal()
          }]}
        options={{
          actionsColumnIndex: -1, grouping: true, pageSizeOptions: [5, 10, 15], pageSize: 10, headerStyle: {
            zIndex: 0
          },
        }}
        onRowClick={(e, data) => edituser(data._id)}
      />
      </>
      }
      </div>
  )
}

export default Manageusertable