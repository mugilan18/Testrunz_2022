import React, { useEffect, useState } from 'react'
import {useParams} from "react-router-dom";
import ApiUrl from '../../../ServerApi';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemText from '@mui/material/ListItemText';
import { Divider } from '@mui/material';
import { useHistory ,useLocation} from "react-router-dom";
const Lablist = () => {
    let { id } = useParams();
    const [lablist,setLablist]=useState([])
    const history = useHistory()
   useEffect(()=>{
    fetch(`${ApiUrl}/moreInfo/experiment`, {
        method: "POST",
        body: JSON.stringify({
          lab: id
      }),
      headers: {
        "Content-type": "application/json; charset=UTF-8"
      }
    })
    .then(response => response.json())
    .then(json => 
      {
  
        // setOptions2(json.ids)

        setLablist(json.ids)
     console.log(json.ids)

      }
      );
    // fetch(`${ApiUrl}/experiments/mypage2`, {
    //     method: "POST",
    //     body: JSON.stringify({
    //       email:user.email
    //     }),
    //     headers: {
    //       "Content-type": "application/json; charset=UTF-8"
    //     }
    //   })
    //     .then(data => data.json())
    //     .then(data => {
    //       console.log(data)
    //       setList(data)
    //       setFinal([])
    //      let temp ={}
    //      user.labtype.forEach(element => {
    //       let count = data.metas.filter(ind => ind.labType ===element);
    //       temp = {"lab":element,"count":count.length}
            
           
    //         console.log(temp)
    //         setFinal(val => [temp,...val])
    //      });
    //       console.log(list)
    //     })
   },[])
  return (
    <div>
        <List>
          { lablist.map((labs, index) => {
    return (
        <>
        <ListItem disablePadding key={index} >
        <ListItemButton onClick={()=>history.push(`/app/${id}/${labs}`)}>
          <ListItemText primary={labs} />
        </ListItemButton>
      </ListItem>
      <Divider/>
      </>
      );
    })}
          
        </List>
    </div>
  )
}

export default Lablist