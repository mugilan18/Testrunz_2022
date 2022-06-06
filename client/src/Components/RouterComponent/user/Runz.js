import React, { useEffect, useState, useContext } from "react";

import axios from "axios";
import Swal from 'sweetalert2'
import Divider from "@mui/material/Divider";

import AddCircleOutlineIcon from "@material-ui/icons/AddCircleOutline";

import { DataGrid } from "@material-ui/data-grid";
import TextField from "@material-ui/core/TextField";

import Snackbar from "@material-ui/core/Snackbar";
import MuiAlert from "@material-ui/lab/Alert";
import { makeStyles } from "@material-ui/core/styles";
import Typography from "@material-ui/core/Typography";

import Modal from "react-modal";

import ApiUrl from "../../../ServerApi";
import ApiService from "../../../Sevices/ApiService";

import AddUserComponent from "./AddUserComponent";
import EditUserComponent from "./EditUserComponent";

import { useStateValue } from "../../../data/StateProvider";
import MaterialTable from 'material-table';


import {FaRegEdit} from 'react-icons/fa';
import {RiShareForwardFill} from 'react-icons/ri';
import Box from '@mui/material/Box';
import Loading from "./Lodaing"
import { Button } from "@material-ui/core";
import { useHistory } from "react-router-dom";
import CircularProgress from '@material-ui/core/CircularProgress';
import AddUserComponentadmin from "./AddUserComponentadmin";

const USER_API_BASE_URL = `${ApiUrl}/experiments`;


function Alert(props) {
  return <MuiAlert elevation={6} variant="filled" {...props} />;
}

const style = {
  marginTop: "55px",
  display: "flex",
  justifyContent: "center",
};


const useStyles = makeStyles((theme) => ({
  root: {
    width: "100%",
    height: "100%",
    maxWidth: "100%",
    "& > * + *": {
      marginTop: theme.spacing(2),
    },
  },

}));

const customStyles = {
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

const customStylesshare = {
  content: {
    top: "50%",
    left: "50%",
    width: "30%",
    height: "50%",
    right: "auto",
    bottom: "auto",
    marginRight: "-50%",
    transform: "translate(-50%, -50%)",
    borderRadius: "2%",
  },
};

const boxstyle = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 600,
  height:700,
  bgcolor: 'background.paper',
  border: '2px solid #000',
  boxShadow: 24,
  // overflowY:'scroll',
  p: 4,
};

const customStylescell = {
  content: {
    color: "red",
    backgroundColor: "black",
  },
};
const fetchuser = async () => {
  let ress = await ApiService.fetchUsers();
  console.log("rkijriotjioprjtfgjeriogj", ress);
  return ress;
};

const Runz = () => {
  let rows = [];
  const [{ user }, dispatch] = useStateValue();
  const classes = useStyles();
  const [open, setOpen] = React.useState(false);
  const [users, setUsers] = useState([]);
  const [message, setMessage] = useState(null);
  const [modalOpenAdd, setModalOpenAdd] = useState(false);
  const [modalOpenEdit, setModalOpenEdit] = useState(false);
  const [loadingscreen, setLoadingscreen]=useState(true)
  const [sharewith, setSharewith]=useState("")
  const [sharewitherror, setSharewitherror]=useState("")
  const [datatoshare, setDatatoshare]=useState({})
  const [btnstatus,setBtnstatus]=useState(false)
  const history = useHistory()

  const columns1 = [
    { title: "ID", field: "id" },
    { title: "Procedure Name", field: "ProcedureName" ,width:"25%" },
    // { title: "Template Id", field: "TemplateId" },
    // { title: "Experiment Name", field: "ExperimentName" },
     { title: "Lab Name", field: "labname" , width:"15%"},
    // { title: "Procedure ID    ", field: "ProcedureId" ,width:"18%",sorting:false },
    { title: "Description", field: "description",width:"18%" },
    { title: "Assigned By", field: "assignedBy",emptyValue:()=><em>{user.email}</em> },
    { title: "Created Time", field: "time" },
    { title: "Status", field: "status" },
  ];

  const [page, setPage] = React.useState(0);
  const [rowsPerPage, setRowsPerPage] = React.useState(10);
  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };


  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(+event.target.value);
    setPage(0);
  };


  // model setup
  const openModal = () => {
    // window.localStorage.clear();
    setModalOpenAdd(() => true);
  };

  const openModale = () => setModalOpenEdit(() => true);
  const closeModal = () => setModalOpenAdd(() => false);
  const closeModale = () => setModalOpenEdit(() => false);


  const value = async () => {
    let userId={
      _id:user._id
    }
    const usersdum = await ApiService.fetchUsers(userId).then((res) => res);
    console.log("asdsaddsadafdwfsfas", user._id);
    setLoadingscreen(false)
    setUsers(() => usersdum.data.data);
    // console.log(usersdum.data.data)
  };


  useEffect(() => {
    value();
    console.log(user);
  }, [modalOpenAdd, modalOpenEdit]);

  
  const handleClose = (event, reason) => {
    if (reason === "clickaway") {
      return;  }
    setOpen(false);
  };

  const deleteUser = async (userId) => {
    await ApiService.deleteUser(userId).then(() => {
      setUsers((prevUser) => prevUser.filter((user) => user._id !== userId));
      setMessage("User deleted successfully.");
    });
    const deleteUser = users.find((user) => user._id === userId);
    await axios.delete(`${ApiUrl}/notes/${deleteUser.runID}`);
    setOpen(true);
  };

  // const editUser = (id) => {
  //   //window.localStorage.clear();
  //   window.localStorage.setItem("userId", id);
  //   openModale();
  //   console.log("this is id", id);
  // };

  const shareRunz =(data)=>{
    // window.localStorage.setItem("userId", id);
    openModale();
    setDatatoshare(data)
    console.log("this is iddetail", data);
    console.log("this is id", datatoshare);
  }
  
  
  const sharerunzwith =()=>{
    // window.localStorage.setItem("userId", id);
    setSharewitherror("")
      let users={
         _id:datatoshare.ProcedureId,
          procedureDescription: datatoshare.description,
          labType: datatoshare.labname,
          experimentName: datatoshare.ProcedureName,
          sharewith:sharewith,
      }
      let usermail ={
        _id:datatoshare.ProcedureId,
         procedureDescription: datatoshare.description,
         labType: datatoshare.labname,
         experimentName: datatoshare.ProcedureName,
         sharewith:sharewith,
         name:user.name
     }


if(sharewith==""||null){
  setSharewitherror("Enter a mail Id")
}
   else{
    setBtnstatus(true)
    axios.post(USER_API_BASE_URL + "/mail", usermail)
    .then((res) => {
              console.log(res.data)
              if(res.data == "error"){
                setBtnstatus(false)
                Swal.fire({
                  icon: 'error',
                  title: 'Oops...',
                  text: 'Check the Email or internet connection',
               
                })
              }
              else{
              console.log("mail sent successfully.");
              ApiService.editUser(users)
              .then((res) => {
                setBtnstatus(false)
                      Swal.fire(
                        'Shared',
                        'Runz has been shared and mailed',
                        'success'
                      )
                      closeModale()
              })
            }
    })
  }
  }



  const playUser = (id) => {
    // window.localStorage.removeItem("userId");
    // window.localStorage.setItem("userId", id);
    history.push(`/userdash/${id}`);
    // console.log("runid runz page", id)
  };
 let individuals = users;
 console.log(typeof users)
  // let individuals = users.reverse();
individuals.map((userr, ident) => {
   
      return rows.push({
        id: ident+1,
        ProcedureName: userr.experimentName,
        // TemplateId: userr.runID.slice(userr.runID.length - 12),
        // ExperimentName: userr.experimentName,
        labname:userr.labType,
        ProcedureId: userr._id,
        description:userr.procedureDescription,
        time:new Date(userr.time).toDateString(),
        status:userr.status,
        assignedBy:userr.assignedBy

      });

  });

  return (
    <div className={classes.root}>
    
    {user.role=="superadmin"?  <Modal
        isOpen={modalOpenAdd}
        appElement={document.getElementById('root')}
        style={customStyles}
        contentLabel="add runz Modal"
        disableBackdropClick="true"
        sx={{ overflow: 'hidden' }}
        
      >
        <Box sx={boxstyle}>

        <AddUserComponentadmin closeModal={closeModal} />
        </Box>
      </Modal>
:
      <Modal
        isOpen={modalOpenAdd}
        appElement={document.getElementById('root')}
        style={customStyles}
        contentLabel="add runz Modal"
        disableBackdropClick="true"
        sx={{ overflow: 'hidden' }}
        
      >
        <AddUserComponent closeModal={closeModal} />
      </Modal>
}

      <Modal
        isOpen={modalOpenEdit}
        appElement={document.getElementById('root')}
        style={customStylesshare}
        contentLabel="Example Modal"
        disableBackdropClick="true"
        // onRequestClose={closeModale}
        
      >
         <Typography variant="h5" style={style}>
        Share Runz
      </Typography>
      <br/><br/>
    {/* {datatoshare.ProcedureId} */}
      <div style={{width:"100%"}}>
     <label>Share With:</label>&nbsp;&nbsp;&nbsp;&nbsp;
              <TextField id="outlined-basic"  size="small" variant="outlined" value={sharewith} onChange={(e)=>setSharewith(e.target.value)} />
              <p className='errormsg'>{sharewitherror}</p>
      </div> 
      <br/>
      <div  style={{display: "flex",justifyContent:"center"}}>
     <Button  style={{background: '#F1C232',width:"50%"}}  onClick={()=>sharerunzwith()} disabled={btnstatus}>Share</Button> 
     </div>
     <br/>
      <div  style={{display: "flex",justifyContent:"center"}}>
     <Button  color="secondary"  variant="contained" style={{width:"50%"}}  onClick={()=>closeModale()}>Close</Button> 
     </div>

      </Modal>
      <div style={{ maxWidth: '100%' }}>
        {loadingscreen ?<Loading />:
        <MaterialTable
          columns={columns1}
          data={rows}
          title="Runz"
          onRowClick= {(e,data) => {playUser(data.ProcedureId)}}
     
          options={{
            actionsColumnIndex: -1, grouping:true,  pageSizeOptions:[5,10,15],pageSize:10,headerStyle: {
              zIndex:0
            }     
          }}
          localization={{
            pagination:{labelRowsSelect:"Runz"},
            body: {
            
              editRow: {
                deleteText: `Are you sure you want to delete this runz`
              }
          }
          }}
          actions={[
            {
              icon: 'add',
              tooltip: 'Add Runz',
              isFreeAction: true,
              onClick:() => openModal()
            },
            {
              icon: () => <RiShareForwardFill/>,
              tooltip: "Share",
               onClick: (e, data) => shareRunz(data)
              // onClick: (e, data) => alert(data.ProcedureId)
            },
          ]} 
          editable={{
            onRowDelete: (selectedRow) => new Promise((resolve, reject) => {
              deleteUser(selectedRow.ProcedureId)
              console.log(selectedRow)
              setTimeout(() => resolve(), 500);
            }),

          }}
        />
        }
      </div>
      <Snackbar open={open} autoHideDuration={3000} onClose={handleClose}>
        <Alert onClose={handleClose} severity="success">
          {message}
        </Alert>
      </Snackbar>


    </div>
  );
};

export default Runz;
