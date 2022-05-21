import { Card } from '@mui/material';
import React, { useEffect, useState } from 'react'
import { useStateValue } from "../../../data/StateProvider";
import ApiUrl from '../../../ServerApi';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';
import ScienceIcon from '@mui/icons-material/Science';
import { useHistory ,useLocation} from "react-router-dom";

const Mypage = () => {
    const [{ user }, dispatch] = useStateValue();
    const [list,setList]=useState([])
    const [final,setFinal]=useState([])
    const history = useHistory()
    useEffect(()=>{
      fetch(`${ApiUrl}/experiments/mypage2`, {
        method: "POST",
        body: JSON.stringify({
          email:user.email
        }),
        headers: {
          "Content-type": "application/json; charset=UTF-8"
        }
      })
        .then(data => data.json())
        .then(data => {
          // setDat(data.data)
          // setLoadingscreen(false)
          console.log(data)
          setList(data)
          setFinal([])
         let temp ={}
         user.labtype.forEach(element => {
          let count = data.metas.filter(ind => ind.labType ===element);
          temp = {"lab":element,"count":count.length}
            
           
            console.log(temp)
            setFinal(val => [temp,...val])
         });
          // console.log(data.data.groupBy( ({ labtype }) => labtype ))
          console.log(list)
        
        })
    },[])
  return (
    <div >
      <Grid 
      container >

       { final.map((labs, index) => {
    return (
      <>
      <Grid item  style={{padding:"20px"}}>
       <Card key={index} sx={{maxWidth:400 }}>
      <CardContent>
      {/* <ScienceIcon/> */}
        <Typography sx={{ fontSize: 15 }} color="text.primary" gutterBottom>
        <ScienceIcon style={{color:"#f1c232"}}/>     {labs.lab}
        </Typography>
       
        <Typography sx={{ mb: 1.5 }} color="text.secondary">
       No of experiments submitted: {labs.count}
        </Typography>
      
      </CardContent>
      <CardActions>
        <Button size="small"  variant='contained' style={{backgroundColor:"#f4f5f7",color:"#537188"}} onClick={()=>history.push(`/app/${labs.lab}`)}>View</Button>
      </CardActions>
    </Card>
    </Grid>
    </>
        );
      })}

</Grid>

    </div>
  )
}

export default Mypage






