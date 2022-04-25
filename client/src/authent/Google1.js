import React from 'react'
import { auth, provider } from "./firebase";
import Button from '@mui/material/Button';
import { useStateValue } from '../data/StateProvider';
import { useHistory, Link } from "react-router-dom";
import { FcGoogle } from 'react-icons/fc';
import { useCookies } from "react-cookie";
import { actionTypes } from "../data/reducer"
import axios from "axios";
const Google1 = () => {
  const [{ user }, dispatch] = useStateValue();
  const [cookies, setCookie, removeCookie] = useCookies(["userjwt"]);

  const history = useHistory()
  const googlesignin = () => {
    auth.signInWithPopup(provider)
      .then((result) => {
        console.log("user", result);
        const email = result.user.email
        const name = result.user.displayName
        console.log("success")
        fetch(`${process.env.REACT_APP_API}/google_login`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            email: email,
            name: name 
          }),
        }).then(response => response.json())
          .then(data => {
            console.log('Success:', data.jwttoken);
            setCookie('userjwt', data.jwttoken, { path: '/' });
            axios.post(`${process.env.REACT_APP_API}/validateuser`, {
              usertoken: data.jwttoken
            })
            .then((res) => {
              console.log("here")
              dispatch({
                type: actionTypes.SET_USER,
                user: res.data.user
             });
             history.push("/private");
             });

          })
          .catch((error) => {
            console.error('Error:', error);
          });
      })
      .catch((error) => {
        console.log("error")
        alert(error.message)})
  }
  return (
    <div>
      <Button variant="outlined" className='googlebutton' onClick={googlesignin} startIcon={<FcGoogle />} >Signin With Google</Button>
    </div>
  )
}

export default Google1