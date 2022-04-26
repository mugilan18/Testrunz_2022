import React, { useState, useEffect, useLayoutEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Button from '@material-ui/core/Button';
import { useStateValue } from '../../data/StateProvider';
import { actionTypes } from "../../data/reducer"
import { GiSoapExperiment } from 'react-icons/gi';
import { BiLogOutCircle } from 'react-icons/bi';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';
import "./Navbar.css"
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import { useHistory, Link } from "react-router-dom";
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import AccountCircleIcon from '@material-ui/icons/AccountCircle';

import { useCookies } from "react-cookie";

import Avatar from '@mui/material/Avatar';
import axios from "axios";
const useStyles = makeStyles({
  
  pointer: {

      '&:hover': {
          cursor: 'pointer'
        }
  }, 

});

const InnerNav = () => {
  const history = useHistory()
  const classes = useStyles();

  const [{user}, dispatch] = useStateValue();
  const [cookies, setCookie, removeCookie] = useCookies(["userjwt"]);
  const [anchorEl, setAnchorEl] = React.useState(null);
  // useEffect
  useEffect(()=>{
  
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
         });
    }

    fetchuserData();

  },[])

  const runz = () => {
   history.push("/app");
  }
  const logout = () => {
    window.localStorage.clear();
    removeCookie("userjwt")
      setAnchorEl(null);
     return (window.location.href = "/");
  }
  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };
  const profile = () => {
    history.push("/profile");
   }
  return (
  <div>
     <Toolbar>
             <Typography onClick={runz} sx={{ flexGrow: 1 }} > <span>Test</span><span style={{backgroundColor:"#F1C232"}}>RunZ</span></Typography>
             <Avatar  size="small"  style={{backgroundColor:"#F1C232",marginRight:"70px",color:"black"}} className={classes.logout} onClick={handleClick}>
                    {`${user.name}`.substring(0, 2)}
</Avatar>


      {/* <button className={classes.logout} style={{color:"white"}} onClick={handleClick}>hello</button> */}
      <Menu
        id="simple-menu"
        anchorEl={anchorEl}
        keepMounted
        open={Boolean(anchorEl)}
        onClose={handleClose}
      >
        <MenuItem onClick={profile}>Profile Page</MenuItem>
        <MenuItem onClick={logout}>Logout</MenuItem>
      </Menu>

           </Toolbar>
  </div>
  );
};

export default InnerNav;
