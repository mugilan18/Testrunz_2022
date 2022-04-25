import React, {useEffect,useState}from 'react'
import { useStateValue } from '../../../../data/StateProvider';
import { actionTypes } from "../../../../data/reducer"
import { useCookies } from "react-cookie";
import axios from "axios";
import { GiConsoleController } from 'react-icons/gi';
import Addusersuperadmin from "./Addusersuperadmin"
import Adduseradmin from './Adduseradmin';
import Adduserteacher from './Adduserteacher';
const Adduser = (props) => {
    const [{ user }, dispatch] = useStateValue();
   
  
  
  
  
    const [cookies, setCookie, removeCookie] = useCookies(["userjwt"]);
      
  return (
    <div>
{user.role == "superadmin"?<Addusersuperadmin/>:null}
{user.role == "admin"?<Adduseradmin/>:null}
{user.role == "teacher" ||user.role =="student"?<Adduserteacher/>:null}


    </div>
  )
}

export default Adduser