import React, { useState, useEffect ,useLayoutEffect} from "react";
import axios from "axios";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.min.css";
//import Layout from "./Layout";

import MenuItem from '@material-ui/core/MenuItem';

import Select from '@material-ui/core/Select';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import { actionTypes } from "../data/reducer"
import CardContent from '@material-ui/core/CardContent';
import { useStateValue } from '../data/StateProvider';
const useStyles = makeStyles({
  root: {
    minWidth: 275,
    marginTop: "100px"
  },

});

const Private = (props) => {
  const [_id, set_id] = useState("")
  const [collegenameerror, setCollegenameerror] = useState()
  const [departmenterror, setDepartmenterror] = useState()
  const [countryerror, setCountryerror] = useState()
  const [stateerror, setStateerror] = useState()
  const [yearerror, setYearerror] = useState()
  const [semestererror, setSemestererror] = useState()

  const [role, setRole] = useState("")
  const [collegeName, setCollegeName] = useState("")
  const [department, setDepartment] = useState("")
  const [country, setCountry] = useState("")
  const [state, setState] = useState("")
  const [year, setYear] = useState("")
  const [semester, setSemester] = useState("")
  const [showOnce, setShowOnce] = useState(false)
  const [btnText, setBtnText] = useState("submit")
  
  const [goTo, setGoTo] = useState(false);

  const [{ user }, dispatch] = useStateValue();
  const classes = useStyles();


  useEffect(()=>{
  
   set_id(user._id)
console.log("private",user)
  if(user.department){
    setDepartment(user.department)
  }
  if(user.collegeName){
    setCollegeName(user.collegeName)
  }
  if(user.role){
    setRole(user.role)
  }
   if(user.showOnce===true){
    props.history.push("/app");
   }
  },[])
  

//   const loadProfile = () => {
//  let idval = JSON.parse(localStorage.getItem('userdetail'))._id
//  console.log("helloo id",idval)
 
//  fetch(`${process.env.REACT_APP_API}/users/${idval}`)
//     .then(response => response.json())
//     .then(data => console.log("helloo eiwfklwejfklsd",data))
//     .catch((error) => {
//       console.error('Error:ererere', error);
//     });

//    };

 

 

  const clickSubmit = (event) => {
    event.preventDefault();

    setCollegenameerror()
    setDepartmenterror()
    setCountryerror()
    setStateerror()
    setYearerror()
    setSemestererror()
 

  if (collegeName === ""||null ) {
    console.log("no email")
    setCollegenameerror("*College Name required*")
  } 
  else if (department === ""||null ) {
    console.log("no password")
    setDepartmenterror("*Department required*")
  }
  else if (country === ""||null ) {
    console.log("no email")
    setCountryerror("*Country required*")
  } 
  else if (state === ""||null ) {
    console.log("no password")
    setStateerror("*State required*")
  }
  else if ((role === "student") && (year === ""||null) ) {
    console.log("no email")
    setYearerror("*Year required  enter a valid number*")
  } 
  else if((role === "student") &&  parseInt(year)> 4 ||parseInt(year)<1){
    setYearerror("Year must be from 1 to 4")
  }
  else if ( (role === "student") && (semester === ""||null)) {
    console.log("no password")
    setSemestererror("*Semester required enter a valid number*")
  }
  else if((role === "student") &&  parseInt(semester) >8 ||parseInt(semester)<1){
    setSemestererror("Semester must be from 1 to 8")
  }
 else{
 
   setBtnText("Submitting");
    fetch(`${process.env.REACT_APP_API}/users/update`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        collegeName,
        department,
        country,
        state,
        year,
        semester,
        _id,
        showOnce: true,
      }),
    })
//       .then((response) => {
//         setCredit({
//           ...credit,
//           collegeName: "",
//           department: "",
//           country: "",
//           state: "",
//           year: "",
//           semester: "",
//           btnText: "Submitted",
//           showOnce: true,
//         });
.then((response) => {
;


        fetch(`${process.env.REACT_APP_API}/users/${user._id}`)
        .then(res => res.json())
        .then(json => {
        dispatch({
          type: actionTypes.SET_USER,
          user: json,
      });
      toast.success("Profile updated successful");
      props.history.push("/app");
      // history.push("/private");
     })
  })
      .catch ((error) => {
  console.log("Sign-up error", error);
  setBtnText("Submit")
  toast.error("error.response.data.error");
});


  

 }

  };


return (
  <Card className={classes.root}>
    <CardContent style={{ alignItems: "center" }}>
      <div >
        <ToastContainer />
        {showOnce && props.history.push("/app")}

        {(showOnce === false) && (<> <p className="lead text-center">Profile Update</p>
          <form>
           
          {   !collegeName &&   <>      
            <div className="form-group">
              <label className="text-muted">College Name</label>
              <input
                onChange={e => setCollegeName(e.target.value)}
                type="text"
                className="form-control"
                value={collegeName}
              />
            </div>
            <p className='errormsg'>{collegenameerror}</p>
            </>}
            
    {   !department &&   <>  <div className="form-group">
              <label className="text-muted">Department</label>
              <input
                onChange={e => setDepartment(e.target.value)}
                type="text"
                className="form-control"
                value={department}
              />
            </div>
            <p className='errormsg'>{departmenterror}</p>
            </>

}
            <div className="form-group">
              <label className="text-muted">Country</label>
              <input
                onChange={e => setCountry(e.target.value)}
                type="text"
                className="form-control"
                value={country}
              />
            </div>
            <p className='errormsg'>{countryerror}</p>
            <div className="form-group">
              <label className="text-muted">State</label>
              <input
                onChange={e => setState(e.target.value)}
                type="text"
                className="form-control"
                value={state}
              />
            </div>
            <p className='errormsg'>{stateerror}</p>
            {role === "student" && (
              <>
                <div className="form-group">
                  <label className="text-muted">Year</label>
                  <input
                    onChange={e => setYear(e.target.value)}
                    className="form-control"
                    value={year}
                    type="number"
                    min="1"
                    max="4"
                  />
                </div>
                <p className='errormsg'>{yearerror}</p>
                <div className="form-group">
                  <label className="text-muted">Semester</label>
                  <input
                    onChange={e => setSemester(e.target.value)}
                    className="form-control"
                    value={semester}
                    type="number"
                    min="1"
                    max="8"
                  />
                </div>
                <p className='errormsg'>{semestererror}</p>
              </>
            )}
            <br />
            <div style={{ alignItems: "center" }}>
              <button className="btn btn-primary" onClick={clickSubmit}>
                {btnText}
              </button>
              <br />

            </div>
          </form>

        </>)}
      </div>
    </CardContent>
    {/* {window.location.reload(true)} */}
  </Card>

);
};

export default Private;

