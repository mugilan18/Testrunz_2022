import React, { useEffect, useState, useContext } from "react";

import axios from "axios";

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

import Loading from "./Lodaing"
import { Button } from "@material-ui/core";
import { useHistory,Redirect } from "react-router-dom";


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
  }

  
}));

const customStyles = {
  content: {
    top: "50%",
    left: "50%",
    width: "50%",
    height: "55%",
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
    height: "35%",
    right: "auto",
    bottom: "auto",
    marginRight: "-50%",
    transform: "translate(-50%, -50%)",
    borderRadius: "2%",
  },
};


const customStylescell = {
  content: {
    color: "red",
    backgroundColor: "black",
  },
};
const fetchuser = async () => {
  let ress = await ApiService.fetchUsers();
  return ress;
};

const Mypage = () => {
  let rows = [];
  const [{ user }, dispatch] = useStateValue();
  const classes = useStyles();
  const [open, setOpen] = React.useState(false);
  const [users, setUsers] = useState([]);
  const [loadingscreen, setLoadingscreen]=useState(true)
  const [message, setMessage] = useState(null);
  const columns1 = [
    { title: "ID", field: "id" },
    { title: "Procedure Name", field: "ProcedureName" , width:"25%"},
    // { title: "Template Id", field: "TemplateId" },
    // { title: "Experiment Name", field: "ExperimentName" },
     { title: "Lab Name", field: "labname", width:"15%"},
     { title: "Procedure ID    ", field: "ProcedureId",width:"18%" ,sorting:false },
    { title: "Submitted By", field: "studentName",width:"18%" },
    { title: "Submited Time", field: "sharedDates" },
  ];


  let history = useHistory();


  useEffect(() => {
    value();
    console.log(user);
    if(user.showOnce===false){
           
      history.push("/private"); 
      console.log("truee",user.showOnce)
     }
  }, [message]);


  const value = async () => {
    let userId={
      _id:user.email
      // _id:"mugilan.learny@gmail.com"
    }
    const usersdum = await ApiService.fetchUsersmail(userId).then((res) => res);
    console.log("asdsaddsadafdwfsfas", usersdum);
    setLoadingscreen(false)
    setUsers(() => usersdum.data.data);
  };


  const handleClose = (event, reason) => {
    if (reason === "clickaway") {
      return;  }
    setOpen(false);
  };

  const deleteUser = async (data) => {
  
  // console.log("this isFinite", data.email)
     
        let toremove={
           email: user.email,
           _id:data.ProcedureId
        }
  
    
      ApiService.removeshareduser(toremove).then((res) => {
        setMessage("Deleted Successfully")
        
      });
    
  
  }




  const playUser = (id) => {
    // window.localStorage.removeItem("sharedId");
    // window.localStorage.setItem("sharedId", id);
    history.push(`/shareddash/${id}`);
    // console.log("runid mypage", id)
  };
  // let individuals = users.filter(function (userr) {return userr.shareWith.includes(user.email);}).reverse();
  let individuals = users
  individuals.map((userr, ident) => {
   
 
      return rows.push({
        id: ident+1,
        labname:userr.labType,
        ProcedureName: userr.experimentName,
        // TemplateId: userr.runID.slice(userr.runID.length - 12),
        // ExperimentName: userr.experimentName,
        studentName:userr.studentName,
        ProcedureId: userr._id,
        sharedDates:new Date(userr.sharedDate).toDateString(),

      });

  });

  return (
    <div className={classes.root}>

      <div style={{ maxWidth: '100%', }}>
        {loadingscreen ?<Loading/>:
        <MaterialTable
          columns={columns1}
          data={rows}
          title="Submited"
          onRowClick= {(e,data) => playUser(data.ProcedureId)}
          options={{
            actionsColumnIndex: -1, grouping:true,  pageSizeOptions:[5,10,15],pageSize:10,headerStyle: {
              zIndex:0,tableLayout:"fixed"
            }     
          }}
          localization={{
            pagination:{labelRowsSelect:"Runz"}
          }}
     
          editable={{
            onRowDelete: (data) => new Promise((resolve, reject) => {
               deleteUser(data)
           
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



export default Mypage;
