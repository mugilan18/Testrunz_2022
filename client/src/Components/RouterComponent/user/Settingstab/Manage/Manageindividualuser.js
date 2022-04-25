import React, { useEffect, useState } from 'react'
import { useParams} from "react-router-dom";
import ApiUrl from '../../../../../ServerApi';
import TextField from '@mui/material/TextField';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import { useStateValue } from '../../../../../data/StateProvider';
import { Button } from '@mui/material';
import Autocomplete from '@mui/material/Autocomplete';


const Manageindividualuser = () => {
  let {token} = useParams()
  const[detail,setDetail]=useState()
  const [lab, setLab] = useState([])
  const[id,setId]=useState("")
  const [{ user }, dispatch] = useStateValue();
  useEffect(()=>{
    fetch(`${ApiUrl}/api/users/${token}`)
    .then((res)=>res.json())
    .then(data =>{
      setDetail(data)
      setId(data._id)
    })
  },[])

  const editcontrol =()=>{
    if(lab == "" || null){
alert("lab")
    }  
    else{
       
  fetch(`${ApiUrl}/api/tooglelab`, {
  method: "PATCH",

  body: JSON.stringify({
    lab:[lab],
    id:id,
    college: user.collegeName,
    department: user.department,
    role: user.role,
}),
headers: {
  "Content-type": "application/json; charset=UTF-8"
}
})
.then(response => response.json())
.then(json => 
{

      console.log("hai",json)

}
)}
  }
  return (
    <div>
      {detail? <h6>Name: {detail.name} <br/><br/>
      Role: {detail.role} <br/><br/>
      Name: {detail.email} <br/><br/>
      department: {detail.department}<br/> <br/>
      lab: <ul> {
     
      detail.labtype.map((lab, index) => {
        return (
          <li >
            {lab}
          </li>
        );
      }) }
      </ul>
       <br/>
      </h6>: null

}



      <Autocomplete
        value={lab}
        onChange={(event, newValue) => {
          setLab(newValue)
          
        }}
        options={user.labtype.map((option) => option)}
        id="controllable-states-demo"
        // options={options}
        sx={{ width: 300 }}
        renderInput={(params) => <TextField {...params} />}
      />
<br/>
<Button variant="contained" style={{background:"#F1C232",color:"black"}}  onClick={editcontrol}>Add Lab</Button>

{/* <Button variant="contained" style={{background:"#3F51B"}}  onClick={editcontrol}>Add Lab</Button> */}
    </div>
  )
}

export default Manageindividualuser
