
// import { useStateValue } from '../../../../data/StateProvider';

// import Divider from '@mui/material/Divider';
// import React, { useState, useEffect } from "react";
// import axios from "axios";
// import { ToastContainer, toast } from "react-toastify";
// import "react-toastify/dist/ReactToastify.min.css";
// import { useHistory, Link } from "react-router-dom";
// import MenuItem from '@material-ui/core/MenuItem';
// import Select from '@material-ui/core/Select';
// import Button from '@mui/material/Button';
// import ApiUrl from "../../../../ServerApi";
// import { actionTypes } from "../../../../data/reducer"

// import Card from '@mui/material/Card';
// import CardActions from '@mui/material/CardActions';
// import CardContent from '@mui/material/CardContent';
// import Typography from '@mui/material/Typography';
// import Grid from '@mui/material/Grid';
// const Userprofile = () => {

//   const [{ user }, dispatch] = useStateValue();
//   const history = useHistory()
//   const [editbt, setEditbt] = useState(false)
//   const [yearerror,setYearerror]=useState()
//   const [semestererror,setSemestererror]=useState()


//   let detail =JSON.parse(localStorage.getItem('userdetail'))
//   useEffect(()=>{
//   //   dispatch({
//   //     type: actionTypes.SET_USER,
//   //     user: JSON.parse(localStorage.getItem('userdetail')),
//   //  });
//   console.log(detail)
//   },[])


//   const [credit, setCredit] = useState({
//     collegeName: detail.collegeName,
//     department: detail.department,
//     country: detail.country,
//     state: detail.state,
//     year: detail.year,
//     semester: detail.semester,
//     btnText: "Submit",
//     _id: detail._id,
//   });


//   const {
//     collegeName,
//     department,
//     country,
//     state,
//     year,
//     semester,
//     btnText,
//     _id,
//   } = credit;

//   const handleChange = (name) => (event) => {
//     setCredit({ ...credit, [name]: event.target.value, });
//   };



//   const clickSubmit = (event) => {
//     event.preventDefault();
//     setYearerror()
//     setSemestererror()
//     if(parseInt(year)> 4 ||parseInt(year)<1){
//       setYearerror("Year must be from 1 to 4")
//     }
//     else if(parseInt(semester) >8 ||parseInt(semester)<1){
//       setSemestererror("Semester must be from 1 to 8")
//     }
//     else {
//       console.log("this the patch detail",
//       collegeName,
//       department,
//       country,
//       state,
//       year,
//       semester,
//       _id)

//     setCredit({ ...credit, btnText: "Submitting" });
//     fetch(`${process.env.REACT_APP_API}/users/update`, {
//       method: "PATCH",
//       headers: {
//         "Content-Type": "application/json"
//       },
//       body: JSON.stringify({

//         collegeName,
//         department,
//         country,
//         state,
//         year,
//         semester,
//         _id,
//       }),
//     })
//       .then(response => response.json())
//       .then(data => {
//         console.log(data.updated)
//         localStorage.setItem("userdetail", JSON.stringify(data.updated))
//                 dispatch({
//                   type: actionTypes.SET_USER,
//                   user: JSON.parse(localStorage.getItem('userdetail')),
//                 })
//         setCredit({
//           ...credit,

//           collegeName: user.collegeName,
//           department: user.department,
//           country: user.country,
//           state: user.state,
//           year: user.year,
//           semester: user.semester,
//           btnText: "Submit",
//         });
//         setEditbt(!editbt)
//         console.log("noerror");
//       })
//       .catch((error) => {
//         console.error('Error:', error);
//       });
//   }}



//   return (
//     <div>
// <div style={{display:"flex",justifyContent:"flex-end"}}>
//       <Button variant="contained"  style={{ backgroundColor:"#F1C232",color:"black" }} onClick={() => setEditbt(!editbt)}>edit</Button>
//       </div>
//       <br />

//       <hr />
//       {editbt ?




//             <div className="form-group">
//               <label className="text-muted">College Name</label>
//               <input
//                 onChange={handleChange("collegeName")}
//                 type="text"
//                 className="form-control"
//                 value={collegeName}
//               />
//             </div>
//             <div className="form-group">
//               <label className="text-muted">Department</label>
//               <input
//                 onChange={handleChange("department")}
//                 type="text"
//                 className="form-control"
//                 value={department}
//               />
//             </div>
//             <div className="form-group">
//               <label className="text-muted">Country</label>
//               <input
//                 onChange={handleChange("country")}
//                 type="text"
//                 className="form-control"
//                 value={country}
//               />
//             </div>
//             <div className="form-group">
//               <label className="text-muted">State</label>
//               <input
//                 onChange={handleChange("state")}
//                 type="text"
//                 className="form-control"
//                 value={state}
//               />
//             </div>
//             {credit.designation === "student" && (
//               <>
//                 <div className="form-group">
//                   <label className="text-muted">Year</label>
//                   <input
//                     onChange={handleChange("year")}
//                     className="form-control"
//                     value={year}
//                     min="1"
//                     max="4"
//                     type="number"
//                   />
//                   <p className='errormsg'>{yearerror}</p>

//                 </div>
//                 <div className="form-group">
//                   <label className="text-muted">Semester</label>
//                   <input
//                     onChange={handleChange("semester")}
//                     className="form-control"
//                     value={semester}
//                     min="1"
//                     max="8"
//                     type="number"
//                   />
//                   <p className='errormsg'>{semestererror}</p>

//                 </div>
//               </>
//             )}
//             <br />
//             <div >
//               <Button style={{ backgroundColor:"#F1C232",color:"black" }} onClick={clickSubmit}>
//                 {btnText}
//               </Button>
//               <br />

//             </div>
//           </form>
//         </div>
//         :
//         <div>

// <Card>
//   <CardContent style={{backgroundColor:"#E7EBF0"}}>
//   <Grid container spacing={2} columns={16}>
//   <Grid item xs={8}>
//   <span style={{fontWeight: "bold"}}>Name:</span>
// <br/>
// <span style={{fontStyle: "italic",color:"gray"}}>{detail.name}</span>
//   </Grid>
//   <Grid item xs={8}>
//   <span  style={{fontWeight: "bold"}}>Email:</span>
//   <br/>
// <span style={{fontStyle: "italic",color:"gray"}}>{detail.email}</span>
//   </Grid>

//   <Grid item xs={8}>
//   <span  style={{fontWeight: "bold"}}>Designation:</span>
//   <br/>
// <span style={{fontStyle: "italic",color:"gray"}}>{detail.designation}</span>
//   </Grid>
//   <Grid item xs={8}>
//   <span  style={{fontWeight: "bold"}}>CollegeName:</span>
//   <br/>
// <span style={{fontStyle: "italic",color:"gray"}}>{detail.collegeName}</span>
//   </Grid>

//   <Grid item xs={8}>
//   <span  style={{fontWeight: "bold"}}>Department:</span>
//   <br/>
// <span style={{fontStyle: "italic",color:"gray"}}>{detail.department}</span>
//   </Grid>
//   <Grid item xs={8}>
//   <span  style={{fontWeight: "bold"}}>Role:</span>
//   <br/>
// <span style={{fontStyle: "italic",color:"gray"}}>{detail.role}</span>
//   </Grid>
  
//   <Grid item xs={8}>
//   <span  style={{fontWeight: "bold"}}>Country:</span>
//   <br/>
// <span style={{fontStyle: "italic",color:"gray"}}>{detail.country}</span>
//   </Grid>
//   <Grid item xs={8}>
//   <span  style={{fontWeight: "bold"}}>State:</span>
//   <br/>
// <span style={{fontStyle: "italic",color:"gray"}}>{detail.state}</span>
//   </Grid>
// {detail.designation ==="student" ?
// <>  <Grid item xs={8}>
//   <span  style={{fontWeight: "bold"}}>Year:</span>
//   <br/>
// <span style={{fontStyle: "italic",color:"gray"}}>{detail.year ? detail.year :"null"}</span>
//   </Grid>
//   <Grid item xs={8}>
//   <span  style={{fontWeight: "bold"}}>Semester:</span>
//   <br/>
// <span style={{fontStyle: "italic",color:"gray"}}>{detail.semester ? detail.semester : "null" }</span>
//   </Grid>
//   </>

//   : null
// }
// </Grid>




//   </CardContent>
// </Card>


          
          
//         </div>


//       }


//     </div>
//   );
// };

// export default Userprofile;



























import { useStateValue } from '../../../../data/StateProvider';

import Divider from '@mui/material/Divider';
import React, { useState, useEffect } from "react";
import axios from "axios";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.min.css";
import { useHistory, Link } from "react-router-dom";
import MenuItem from '@material-ui/core/MenuItem';
import Select from '@material-ui/core/Select';
import Button from '@mui/material/Button';
import ApiUrl from "../../../../ServerApi";
import { actionTypes } from "../../../../data/reducer"
import { useCookies } from "react-cookie";

import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';
const Userprofile = () => {

  const [{ user }, dispatch] = useStateValue();
  const history = useHistory()
  const [editbt, setEditbt] = useState(false)
  const [yearerror,setYearerror]=useState()
  const [semestererror,setSemestererror]=useState()
  const [detail,setDetail]=useState({})
  const [update, setUpdate] = useState(false)




  const [cookies, setCookie, removeCookie] = useCookies(["userjwt"]);

  useEffect(()=>{
    console.log("coookieee",cookies.userjwt)

    async function fetchuserData() {
      
      await axios
        .post(`${process.env.REACT_APP_API}/validateuser`, {
          usertoken: cookies.userjwt
        })
        .then((res) => {
          
          dispatch({
            type: actionTypes.SET_USER,
            user: res.data.user
         });
         setDetail(res.data.user)
          setCredit({
    ...credit,
    
    collegeName: user.collegeName,
    department: user.department,
    country: user.country,
    state: user.state,
    year: user.year,
    semester: user.semester,
    btnText: "Submit",
    _id: user._id,
        })
         });
    }

    fetchuserData();


  },[update])





  const [credit, setCredit] = useState({
    collegeName: "",
    department: "",
    country: "",
    state: "",
    year: "",
    semester: "",
    btnText: "Submit",
    _id: "",
  });
  


  const {

    collegeName,
    department,
    country,
    state,
    year,
    semester,
    btnText,
    _id,
  } = credit;

  const handleChange = (name) => (event) => {
    setCredit({ ...credit, [name]: event.target.value, });
  };



  const clickSubmit = (event) => {
    event.preventDefault();
    setYearerror()
    setSemestererror()
    if(parseInt(year)> 4 ||parseInt(year)<1){
      setYearerror("Year must be from 1 to 4")
    }
    else if(parseInt(semester) >8 ||parseInt(semester)<1){
      setSemestererror("Semester must be from 1 to 8")
    }
    else {

   console.log("sumitted result", collegeName, department, country, state, year, semester, _id,)

    setCredit({ ...credit, btnText: "Submitting" });
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
      }),
    })
      .then(response => response.json())
      .then(data => {
       
                dispatch({
                  type: actionTypes.SET_USER,
                  user: data.updated,
                })
        setCredit({
          ...credit,
          collegeName: user.collegeName,
          department: user.department,
          country: user.country,
          state: user.state,
          year: user.year,
          semester: user.semester,
          btnText: "Submit",
        });
        setEditbt(!editbt)
        console.log("noerror");
        setUpdate(!update)
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }}



  return (
    <div>
<div style={{display:"flex",justifyContent:"flex-end"}}>
      <Button variant="contained"  style={{ backgroundColor:"#F1C232",color:"black" }} onClick={() => setEditbt(!editbt)}>edit</Button>
      </div>
      <br />

      <hr />
      {editbt ?

        <div>
          <form>

{user.role == "superadmin" ?
<>
            <div className="form-group">
              <label className="text-muted">College Name</label>
              <input
                onChange={handleChange("collegeName")}
                type="text"
                className="form-control"
                value={collegeName}
              />
            </div>
            <div className="form-group">
              <label className="text-muted">Department</label>
              <input
                onChange={handleChange("department")}
                type="text"
                className="form-control"
                value={department}
              />
            </div>
            </>
            : null
}
            <div className="form-group">
              <label className="text-muted">Country</label>
              <input
                onChange={handleChange("country")}
                type="text"
                className="form-control"
                value={country}
              />
            </div>
            <div className="form-group">
              <label className="text-muted">State</label>
              <input
                onChange={handleChange("state")}
                type="text"
                className="form-control"
                value={state}
              />
            </div>
            {user.role === "student" && (
              <>
                <div className="form-group">
                  <label className="text-muted">Year</label>
                  <input
                    onChange={handleChange("year")}
                    className="form-control"
                    value={year}
                    min="1"
                    max="4"
                    type="number"
                  />
                  <p className='errormsg'>{yearerror}</p>

                </div>
                <div className="form-group">
                  <label className="text-muted">Semester</label>
                  <input
                    onChange={handleChange("semester")}
                    className="form-control"
                    value={semester}
                    min="1"
                    max="8"
                    type="number"
                  />
                  <p className='errormsg'>{semestererror}</p>

                </div>
              </>
            )}
            <br />
            <div >
              <Button style={{ backgroundColor:"#F1C232",color:"black" }} onClick={clickSubmit}>
                {btnText}
              </Button>
              <br />

            </div>
          </form>
        </div>
        :
        <div>

 <Card>
  <CardContent style={{backgroundColor:"#E7EBF0"}}>
  <Grid container spacing={2} columns={16}>
  <Grid item xs={8}>
  <span style={{fontWeight: "bold"}}>Name:</span>
<br/>
<span style={{fontStyle: "italic",color:"gray"}}>{detail.name ? detail.name : ""}</span>
  </Grid>
  <Grid item xs={8}>
  <span  style={{fontWeight: "bold"}}>Email:</span>
  <br/>
<span style={{fontStyle: "italic",color:"gray"}}>{detail.email ? detail.email :""}</span>
  </Grid>

  <Grid item xs={8}>
  <span  style={{fontWeight: "bold"}}>College Name:</span>
  <br/>
<span style={{fontStyle: "italic",color:"gray"}}>{detail.collegeName ? detail.collegeName: "" }</span>
  </Grid>

  <Grid item xs={8}>
  <span  style={{fontWeight: "bold"}}>Department:</span>
  <br/>
<span style={{fontStyle: "italic",color:"gray"}}>{detail.department ? detail.department:""}</span>
  </Grid>
  <Grid item xs={8}>
  <span  style={{fontWeight: "bold"}}>Role:</span>
  <br/>
<span style={{fontStyle: "italic",color:"gray"}}>{detail.role ? detail.role : ""}</span>
  </Grid>
  
  <Grid item xs={8}>
  <span  style={{fontWeight: "bold"}}>Country:</span>
  <br/>
<span style={{fontStyle: "italic",color:"gray"}}>{detail.country ? detail.country : ""}</span>
  </Grid>
  <Grid item xs={8}>
  <span  style={{fontWeight: "bold"}}>State:</span>
  <br/>
<span style={{fontStyle: "italic",color:"gray"}}>{detail.state ? detail.state: ""}</span>
  </Grid>
{user.role ==="student" ?
<>  <Grid item xs={8}>
  <span  style={{fontWeight: "bold"}}>Year:</span>
  <br/>
<span style={{fontStyle: "italic",color:"gray"}}>{detail.year ? detail.year :"null"}</span>
  </Grid>
  <Grid item xs={8}>
  <span  style={{fontWeight: "bold"}}>Semester:</span>
  <br/>
<span style={{fontStyle: "italic",color:"gray"}}>{detail.semester ? detail.semester : "null" }</span>
  </Grid>
  </>

  : null
}
</Grid>




  </CardContent>
</Card> 


          
          
        </div>


      }


    </div>
  );
};

export default Userprofile;

