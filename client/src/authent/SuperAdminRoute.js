


import { Route, Redirect } from 'react-router-dom';

import React, { useState, useEffect ,useLayoutEffect} from "react";

import { useCookies } from "react-cookie";
import axios from "axios";
import { useStateValue } from '../data/StateProvider';

import { actionTypes } from "../data/reducer"

const SuperAdminRoute = ({ auth, component: Component, ...rest }) => {
  const [{ user }, dispatch] = useStateValue();
  const [cookies, setCookie, removeCookie] = useCookies(["userjwt"]);

  useEffect(()=>{
    const abortcont = new AbortController();
    console.log("coookieee",cookies.userjwt)

fetch(`${process.env.REACT_APP_API}/validateuser`, {
		method: "POST",
    signal:abortcont.signal,
	  body: JSON.stringify({
      usertoken: cookies.userjwt
	}),
	headers: {
		"Content-type": "application/json; charset=UTF-8"
	}
})
.then(response => response.json())
.then(json => 
  {
    // setB(json.user)
    // console.log("lasdkl",b)
    dispatch({
            type: actionTypes.SET_USER,
            user: json.user,
          });
    // console.log("lasdkl",user.role)
    return ()=>abortcont.abort()
  }
  );

   
  

  },[])
     return (
   <>
    <Route {...rest} render={props => ( user.role=="superadmin" ? <Component {...props} /> :  
    // <Redirect to="/signin" />
    null
    )} />   
    </>                      
)}


export default SuperAdminRoute;