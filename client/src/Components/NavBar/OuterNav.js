// import React from 'react';
// import Typography from '@mui/material/Typography';
// import Toolbar from '@material-ui/core/Toolbar';
// const OuterNav = () => {
//     const runz = () => {
//         window.localStorage.clear();
//        return (window.location.href = "/");
//       }
//   return (
//   <div>
//        <Toolbar>
//              <Typography onClick={runz}> <span>Test</span><span style={{backgroundColor:"#F1C232",cursor: "pointer"}}>RunZ</span></Typography>
//         </Toolbar>
//   </div>
//     );
// };

// export default OuterNav;
import React ,{useState,useEffect, useLayoutEffect}from 'react';
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


const useStyles = makeStyles({

  pointer: {
    paddingRight:"75px",

      '&:hover': {
          cursor: 'pointer'
        }
  }, 

});



const OuterNav = () => {

    const classes = useStyles();
    const [anchorEl, setAnchorEl] = React.useState(null);
    const open = Boolean(anchorEl);
    const handleClick = (event) => {
      setAnchorEl(event.currentTarget);
   
    };
    const handleClose = () => {
      setAnchorEl(null);
      return (window.location.href = "/");
    };
   
    const [{user}, dispatch] = useStateValue();
    const history = useHistory()
  
    
    const runz = () => {
      window.localStorage.clear();
      
     return (window.location.href = "/");
    }
    
  
 
    
    return (
      
     
     <Toolbar >
             <Typography onClick={runz} sx={{ flexGrow: 1 }} > <span>Test</span><span style={{backgroundColor:"#F1C232",cursor: "pointer"}}>RunZ</span></Typography>
     <div className='navhide'>
     <Grid
   container
   direction="row"
   justifyContent="flex-end"
   alignItems="center"
 >
 
     {/* <Typography className={classes.pointer}>Documentation </Typography>
     <Typography className={classes.pointer}>Support </Typography> */}
     <Typography className={classes.pointer} onClick={()=>{window.location.href ='/#/signin'}}> Sign In </Typography>
     <Typography className={classes.pointer} onClick={()=>{window.location.href = '/#/signup'}}> Sign Up </Typography>
 
     
     </Grid>
     </div>
     <div className='navhide1'>
     <IconButton edge="end" color="inherit" aria-label="menu" sx={{ mr: 2 }}
     id="basic-button"
     aria-controls={open ? 'basic-menu' : undefined}
     aria-haspopup="true"
     aria-expanded={open ? 'true' : undefined}
     onClick={handleClick}>
         <MenuIcon/>
       </IconButton>
       <Menu
         id="basic-menu"
         anchorEl={anchorEl}
         open={open}
         onClose={handleClose}
         MenuListProps={{
           'aria-labelledby': 'basic-button',
         }}
       >
         {/* <MenuItem onClick={()=>{setAnchorEl(null)
    window.location.href = "/"}}>Documentation</MenuItem>
 
         <MenuItem onClick={()=>{setAnchorEl(null)
     window.location.href = "/"}}>Support</MenuItem> */}
 
         <MenuItem onClick={()=>{setAnchorEl(null)
    window.location.href = "/#/signin"}}>Sign In</MenuItem>
 
         <MenuItem onClick={()=>{setAnchorEl(null)
     window.location.href = "/#/signup"}}>Sign Up</MenuItem>
       </Menu>
     </div>
 
     </Toolbar>
    
    )
}

export default OuterNav

