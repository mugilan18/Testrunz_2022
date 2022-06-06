import React, {useEffect,useState}from 'react'
import { useStateValue } from '../../../../data/StateProvider';
import { actionTypes } from "../../../../data/reducer"
import { useCookies } from "react-cookie";
import axios from "axios";
import { GiConsoleController } from 'react-icons/gi';
import Addusersuperadmin from "./Addusersuperadmin"
import Adduseradmin from './Adduseradmin';
import Adduserteacher from './Adduserteacher';
import { Button } from '@material-ui/core';
const Adduser = (props) => {
    const [{ user }, dispatch] = useStateValue();
   
   
  
  
  
    const [cookies, setCookie, removeCookie] = useCookies(["userjwt"]);
      
  return (
    <div>
      <div style={{display:"flex"}}>

      <div style={{ flexGrow:1}} >
      <strong ><em>Add User</em></strong>
      </div>

      <div>
      <Button color='secondary' button onClick={props.closeModal}>
          Cancel
        </Button>
      </div>


      </div>
      <br/>
 {user.role == "superadmin"?<Addusersuperadmin/>:null}
{user.role == "admin"?<Adduseradmin/>:null}
{user.role == "teacher" ||user.role =="student"?<Adduserteacher/>:null}
 


    </div>
  )
}

export default Adduser