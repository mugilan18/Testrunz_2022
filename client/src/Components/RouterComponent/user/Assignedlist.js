
import {useParams,useHistory} from "react-router-dom";
import { useStateValue } from '../../../data/StateProvider';
import ApiUrl from '../../../ServerApi';

import React, { useEffect, useState } from "react";
import Snackbar from "@material-ui/core/Snackbar";

import ApiService from "../../../Sevices/ApiService";

import MaterialTable from 'material-table';

import MuiAlert from "@material-ui/lab/Alert";

const Assignedlist = () => {


    let rows = [];
    // const [{ user }, dispatch] = useStateValue();
    // const classes = useStyles();
    const [open, setOpen] = React.useState(false);
    const [users, setUsers] = useState([]);
    const [loadingscreen, setLoadingscreen]=useState(true)
    const [message, setMessage] = useState(null);
    const columns1 = [
      { title: "ID", field: "id" },
    //   { title: "Procedure Name", field: "ProcedureName" },
      // { title: "Template Id", field: "TemplateId" },
      // { title: "Experiment Name", field: "ExperimentName" },
    //    { title: "Lab Name", field: "labname"},
      //  { title: "Procedure ID    ", field: "ProcedureId",width:"18%" ,sorting:false },
      { title: "Status", field: "status" },
      { title: "Submitted By", field: "studentName" },
      { title: "Submitted Time", field: "sharedDates" },
    ];
  
  
    let history = useHistory();
  
  
    let { id,exp } = useParams();
    const [{ user }, dispatch] = useStateValue();
    console.log(id,exp)
    useEffect(()=>{
        fetch(`${ApiUrl}/experiments/specific`, {
            method: "POST",
            body: JSON.stringify({
              lab: id,
              experiment: exp,
              college:user.collegeName,
              email:user.email,
          }),
          headers: {
            "Content-type": "application/json; charset=UTF-8"
          }
        })
        .then(response => response.json())
        .then(json => 
          {
      
            // setOptions2(json.ids)
        setUsers(json.metas)
         console.log(json)
    
          }
          );

    },[])

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
            status:userr.status
    
          });
    
      });

      function Alert(props) {
        return <MuiAlert elevation={6} variant="filled" {...props} />;
      }
      


  return (
    <div>
        <h5>Lab : {id}</h5><h5>Experiment : {exp}</h5>
        
        <MaterialTable
          columns={columns1}
          data={rows}
          title="Submitted"
          onRowClick= {(e,data) => playUser(data.ProcedureId)}
          options={{
            actionsColumnIndex: -1, grouping:true,  pageSizeOptions:[5,10,15],pageSize:10,headerStyle: {
              zIndex:0
            },tableLayout: "auto"     
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
         <Snackbar open={open} autoHideDuration={3000} onClose={handleClose}>
        <Alert onClose={handleClose} severity="success">
        {message}
        </Alert>
      </Snackbar>
    </div>
  )
}

export default Assignedlist