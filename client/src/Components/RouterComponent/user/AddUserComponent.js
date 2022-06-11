import React, { useState, useEffect, useContext } from "react";
import axios from "axios";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";
import ReactHTMLDatalist from "react-html-datalist";
import ApiService from "../../../Sevices/ApiService";
import Snackbar from "@material-ui/core/Snackbar";
import MuiAlert from "@material-ui/lab/Alert";
import { makeStyles } from "@material-ui/core/styles";
import { laboratries } from "./data";
import { useStateValue } from '../../../data/StateProvider';
import { IoIosArrowRoundBack } from 'react-icons/io';
import ApiUrl from "../../../ServerApi";
import Autocomplete from '@mui/material/Autocomplete';
function Alert(props) {
  return <MuiAlert elevation={6} variant="filled" {...props} />;
}

const useStyles = makeStyles((theme) => ({
  root: {
    width: "100%",
    "& > * + *": {
      marginTop: theme.spacing(2),
      zIndex: "200%",
      padding: "1%", height: "40%"
    },
  },
}));

const formContainer = {
  display: "flex",
  flexFlow: "column wrap",
  alignContent: "space-between",
  zIndex: "100%"
};

const style = {
  marginTop: "30px",
  display: "flex",
  justifyContent: "center",
};

const intialValue = {
  studentName: "",
  procedureDescription: "",
  labType: "",
  experimentName: "",
};

const AddUserComponent = (props) => {

  const classes = useStyles();
  const [data, setData] = useState(intialValue);
  const [options, setOptions] = useState([]);
  const [options1, setOptions1] = useState([]);

  const [open, setOpen] = React.useState(false);
  const [message, setMessage] = useState(null);
  const [messageerror, setMessageerror] = useState(null);
  const [{ user }, dispatch] = useStateValue();
  const username = user.name
  const useridval = user._id
  const [labTypetosent,setLabTypetosent] = useState()
  const [experimentNametosent,setExperimentNametosent] =useState()

  const [descriptionerror, setDescriptionerror] = useState();
  const [laberror, setLaberror] = useState();
  const [procedureerror, setProcedureerrorr] = useState();

  // useEffect(() => {
  //   laboratries.then((res) => setOptions(res));
  //   console.log(options)
  // }, [options]);

  // useEffect(() => {
  //   axios.get(`${ApiUrl}/labrotories`).then((result) => {
  //     const resultant = Object.getOwnPropertyDescriptor(
  //       result.data[0],
  //       labTypetosent || "Physics"
  //     ).value;
  //     const res = resultant.map((val) => ({ text: val, value: val }));
  //     setOptions1(res);
  //     console.log(res)
  //   });
  // }, [labTypetosent]);
  const fetchexperiment = (newValue) => {
    setLabTypetosent(newValue);
    setOptions1([])
    fetch(`${ApiUrl}/moreInfo/experiment`, {
      method: "POST",
   
      body: JSON.stringify({
        lab: newValue
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8"
    }
  })
  .then(response => response.json())
  .then(json => 
    {

      setOptions1(json.ids)

   console.log(json)
    }
    );
  }




  const saveUser = (e) => {
    e.preventDefault();
    setProcedureerrorr()
    setLaberror()
    setDescriptionerror()
    if (data.procedureDescription === "" || null) {
      setDescriptionerror("*Write some descriptions*")
    }
    else if (!labTypetosent) {
      setLaberror("*Choose a lab type*")
    }
    else if (!experimentNametosent) {
      setProcedureerrorr("*Select an experiment from the list*")
    }
    else {
      console.log("labtype",labTypetosent)
      let user = {
        studentName: username,
        procedureDescription: data.procedureDescription,
        labType: labTypetosent,
        experimentName: experimentNametosent,
        userId: useridval
      };
      console.log("list user", user)
      ApiService.addUser(user)
      // .then((res) =>res.json())
      .then((res)=>{
        console.log("check again",res.data)
        if(res.data.errors==="already created"){
          setMessageerror("Already Created");
        setTimeout(() => {
          props.closeModal();
        }, 1000);
        }
        else{
          setMessage("User Added successfully.");
          setTimeout(() => {
            props.closeModal();
          }, 1000);
        }
       
      });
      setOpen(true);
    }




  };

  const handleClose = (event, reason) => {
    if (reason === "clickaway") {
      return;
    }

    setOpen(false);
  };

  const onChange = (e) => setData({ ...data, [e.target.name]: e.target.value })
    ;
 
  return (
    <div className={classes.root}>

      <Typography variant="h4" style={style}>
        Add Runz &nbsp;&nbsp;&nbsp;&nbsp;
        <IoIosArrowRoundBack
          onClick={props.closeModal}
          style={{
            // color: "red",
            // border: "1px solid black",
            // borderRadius: "50%",
            // background: "white",
            alignItems: "center"


          }}
        />
      </Typography>
      <form style={formContainer}>
  
        <label>Description</label>
        <TextField
          type="text"
          placeholder="Experiment Description"
          fullWidth
          margin="normal"
          name="procedureDescription"
          value={data.procedureDescription}
          onChange={onChange}
        />
        <p className='errormsg'>{descriptionerror}</p>
        <label>Lab Type</label>
          <Autocomplete
        value={labTypetosent}
        onChange={(event, newValue) => {
          fetchexperiment(newValue)
          
        }}
        options={user.labtype.map((option) => option)}
        id="controllable-states-demo"
        // options={options}
        sx={{ width: 300 }}
        renderInput={(params) => <TextField {...params} />}
      />
        <p className='errormsg'>{laberror}</p>
        <label>Procedure Name</label>
        <Autocomplete
        value={experimentNametosent}
        onChange={(event, newValue) => {
          setExperimentNametosent(newValue);
        }}
        options={options1.map((option) => option)}
        id="controllable-states-demo"
        // options={options}
        sx={{ width: 300 }}
        renderInput={(params) => <TextField {...params} />}
      />
     
        <p className='errormsg'>{procedureerror}</p>
        <br />
        <Button variant="contained"   style={{ backgroundColor:"#F1C232",color:"black" }} onClick={saveUser}>
          Save
        </Button>
        <br />
        <Button variant="contained" color="secondary" onClick={props.closeModal}>
          Cancel
        </Button>
      </form>
      <Snackbar open={open} autoHideDuration={3000} onClose={handleClose}>
        <Alert onClose={handleClose} severity={message ?"success" :"error"}>
          {message}
          {messageerror}
        </Alert>
      </Snackbar>
    </div>
  );
};

export default AddUserComponent;
