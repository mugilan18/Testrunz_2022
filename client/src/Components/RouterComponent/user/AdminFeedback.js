import React, { useEffect, useState } from 'react'
import Grid from '@mui/material/Grid';
import TextField from '@mui/material/TextField';

import ApiUrl from "../../../ServerApi";
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Autocomplete from '@mui/material/Autocomplete';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';

const AdminFeedback = () => {
const [feedbacks,setFeedbacks]=useState()
const [status,setStatus] = useState()
  useEffect(()=>{
fetch(`${ApiUrl}/feedback`)
.then(response => response.json())
  .then(data => {
    setFeedbacks(data)
  });

  },[])
  return (
    <div>
    <div>Admin Feedback section</div>
    {feedbacks ?<>
    {feedbacks.map((feedback) => (
      <div>
       <Card
       key={feedback._id}
       >
         <CardContent>
           <div>
   Feedback: {feedback.feedback}
   </div>
   <div>
   Status: {feedback.status}
   </div>
   <div>
   Assigned to: {feedback.assignedto? feedback.assignedto: "Not yet assigned"}
   </div>
         </CardContent>
         <CardActions>
           <Grid container spacing={2}>
<div style={{ margin:"20px"}}>
           <Button style={{ backgroundColor:"#F1C232",color:"black" }}> Assign </Button>
</div>
<div style={{ margin:"20px"}}>

  <Select
               size="small"

   style={{width:"200px"}}
    value={status}
    label="status"
    onChange={(e)=>{setStatus(e.target.value)}}
  >
    <MenuItem value={"error"}>error</MenuItem>
    <MenuItem value={"closed"}>closed</MenuItem>
    <MenuItem value={"devclosed"}>dev closed</MenuItem>
    <MenuItem value={"testclosed"}>test closed</MenuItem>
  </Select>
  </div >

  <div style={{ margin:"20px"}}>

            <Button style={{ backgroundColor:"#F1C232",color:"black" }}> Update Status </Button>
            </div >

           </Grid>
           </CardActions>
       </Card>
       <br/>
      
       </div>
      ))}
      </>
      : <p>loading ....</p>
}
    </div>
  )
}

export default AdminFeedback