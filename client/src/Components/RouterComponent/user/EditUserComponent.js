import React, { useState, useEffect } from "react";
import axios from "axios";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";

import ReactHTMLDatalist from "react-html-datalist";

import ApiService from "../../../Sevices/ApiService";

import Snackbar from "@material-ui/core/Snackbar";
import MuiAlert from "@material-ui/lab/Alert";
import { makeStyles } from "@material-ui/core/styles";
import ArrowBackIcon from "@material-ui/icons/ArrowBack";

import { laboratries } from "./data";
import ApiUrl from "../../../ServerApi";

function Alert(props) {
  return <MuiAlert elevation={6} variant="filled" {...props} />;
}

const formContainer = {
  display: "flex",
  flexFlow: "column wrap",
  alignContent: "space-between",
};

const style = {
  marginTop: "55px",
  display: "flex",
  justifyContent: "center",
};

const useStyles = makeStyles((theme) => ({
  root: {
    width: "100%",
    "& > * + *": {
      marginTop: theme.spacing(2),
    },
  },
}));

const intialValue = {
  studentName: "",
  labType: "",
  experimentName: "",
  procedureDescription: "",
};

const EditUserComponent = (props) => {
  const classes = useStyles();
  const [data, setData] = useState(intialValue);
  const [options, setOptions] = useState([]);
  const [options1, setOptions1] = useState([]);

  const [open, setOpen] = React.useState(false);
  const [message, setMessage] = useState(null);

  useEffect(() => {
    laboratries.then((res) => setOptions(res));
  }, [options]);

  useEffect(() => {
    axios.get(`${ApiUrl}/labrotories`).then((result) => {
      const resultant = Object.getOwnPropertyDescriptor(
        result.data[0],
        data.labType || "Physics"
      ).value;
      const res = resultant.map((val) => ({ text: val, value: val }));
      setOptions1(res);
    });
  }, [data.labType]);

  useEffect(() => {
    ApiService.fetchUserById(window.localStorage.getItem("userId")).then(
      (res) => {
        let user = res.data;
        //console.log(user);
        data._id = user._id;
        data.studentName = user.studentName;
        data.labType = user.labType;
        data.experimentName = user.experimentName;
        data.procedureDescription = user.procedureDescription || "";
        setData({ ...data });
      }
    );
  }, []);

  const onChange = (e) => {
    return setData({ ...data, [e.target.name]: e.target.value });
  };

  const saveUser = (e) => {
    e.preventDefault();
    let user = {
      ...data,
    };

    ApiService.editUser(user).then((res) => {
      // console.log(res);
      setOpen(true);
      setMessage("User Edited Succesfully");
      setTimeout(() => {
        props.closeModale();
      }, 3000);
    });
  };

  const handleClose = (event, reason) => {
    if (reason === "clickaway") {
      return;
    }

    setOpen(false);
  };

  return (
    <div className={classes.root}>
      <ArrowBackIcon
        onClick={props.closeModale}
        style={{
          color: "red",
          border: "1px solid black",
          borderRadius: "50%",
          background: "white",
          zIndex: 100000,
          position: "absolute",
          top: 10,
          right: 30,
        }}
      />
      <Typography variant="h4" style={style}>
        Edit Runz
      </Typography>
      <form style={formContainer}>
        <TextField
          type="text"
          placeholder="Student Name"
          fullWidth
          margin="normal"
          name="studentName"
          value={data.studentName}
          onChange={onChange}
        />
        <TextField
          type="text"
          placeholder="Experiment Description"
          fullWidth
          margin="normal"
          name="studentDescrition"
          value={data.procedureDescription}
          onChange={onChange}
        />
        <label>Lab Type</label>
        <ReactHTMLDatalist
          name="labType"
          placeholder="Lab Type"
          onChange={onChange}
          options={options}
          value={data.labType}
        />
        <label>Procedure Name</label>
        <ReactHTMLDatalist
          name="experimentName"
          onChange={onChange}
          options={options1}
          value={data.experimentName}
        />
        <Button variant="contained" color="primary" onClick={saveUser}>
          Save
        </Button>
      </form>
      <Snackbar open={open} autoHideDuration={3000} onClose={handleClose}>
        <Alert onClose={handleClose} severity="success">
          {message}
        </Alert>
      </Snackbar>
    </div>
  );
};

export default EditUserComponent;
