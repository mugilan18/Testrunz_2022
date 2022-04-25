import React, { useState, useEffect } from "react";

import axios from "axios";
import serverApi from "../../../ServerApi";

import { makeStyles } from "@material-ui/core/styles";

import MuiAlert from "@material-ui/lab/Alert";

const useStyles = makeStyles((theme) => ({
  root: {
    width: "100%",
    "& > * + *": {
      marginTop: theme.spacing(2),
    },
  },
}));

const style = {
  marginTop: "25px",
  display: "flex",
  justifyContent: "center",
  textDecoration: "underline",
};

const formContainer = {
  display: "flex",
  flexFlow: "column wrap",
  alignContent: "space-between",
};

const intialValue = {
  labType: "",
  experimentName: "",
};

function Alert(props) {
  return <MuiAlert elevation={6} variant="filled" {...props} />;
}

const Runz = (props) => {
  const classes = useStyles();
  const [open, setOpen] = useState(false);
  const [message, setMessage] = useState(null);
  const [data, setData] = useState(intialValue);
  const [options, setOptions] = useState([]);
  const [options1, setOptions1] = useState([]);

  function renderOptions(options) {
    return (
      options &&
      options.length > 0 &&
      options.map((option, index) => {
        return <option>{option}</option>;
      })
    );
  }

  useEffect(() => {
    let newSet = new Set();
    let newSet1 = new Set();
    axios.get(`${serverApi}/moreInfo`).then((data) => {
      data.data.data.forEach((ele) => {
        newSet.add(ele.labtype);
        newSet1.add(ele.ProcedureName);
      });
      setOptions(() => Array.from(newSet));
      setOptions1(() => Array.from(newSet1));
    });
  }, []);

  const onChange = (e) => setData({ ...data, [e.target.name]: e.target.value });

  const saveUser = (e) => {
    e.preventDefault();
    axios
      .post(`${serverApi}/labrotories`, {
        name: data.labType,
        experiment: data.experimentName,
      })
      .then(() => {
        setMessage("Assigned successfully.");
        setOpen(true);
      });
  };

  const handleClose = (event, reason) => {
    if (reason === "clickaway") {
      return;
    }
    setOpen(false);
  };

  return (
    <>
    </>
    // <div className={classes.root}>
    //   <>
    //     <form style={formContainer}>
    //       {options && (
    //         <>
    //           <label>Lab Type</label>
    //           <select name="labType" onChange={onChange} value={data.labType}>
    //             {renderOptions(options)}
    //           </select>
    //         </>
    //       )}
    //       {options1 && (
    //         <>
    //           <label>Procedure Name</label>
    //           <select
    //             name="experimentName"
    //             onChange={onChange}
    //             value={data.experimentName}
    //           >
    //             {renderOptions(options1)}
    //           </select>
    //         </>
    //       )}

    //       <Button variant="contained" color="primary" onClick={saveUser}>
    //         Save
    //       </Button>
    //     </form>
    //   </>
    //   <Snackbar open={open} autoHideDuration={3000} onClose={handleClose}>
    //     <Alert onClose={handleClose} severity="success">
    //       {message}
    //     </Alert>
    //   </Snackbar>
    // </div>
  );
};

export default Runz;
