import React,{useEffect} from 'react';
import Drawer from '@mui/material/Drawer';
import Typography from '@mui/material/Typography';
// import { makeStyles } from '@mui/styles';
import { makeStyles } from '@material-ui/core/styles';
import ManageAccountsIcon from '@mui/icons-material/ManageAccounts';
import List from '@mui/material/List';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import { ListItem } from '@material-ui/core';
import PlayCircleOutlineIcon from '@material-ui/icons/PlayCircleOutline';
import PersonAddIcon from '@mui/icons-material/PersonAdd';
import AssignmentTurnedInIcon from '@material-ui/icons/AssignmentTurnedIn';
import AccountCircleIcon from '@material-ui/icons/AccountCircle';
import SettingsIcon from '@material-ui/icons/Settings';
import ListIcon from '@material-ui/icons/List';
import PersonIcon from '@mui/icons-material/Person';
import { useHistory ,useLocation} from "react-router-dom";
import Divider from '@mui/material/Divider';
// import Navbar from "../../NavBar/NavBar"
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import { actionTypes } from "../../../data/reducer"
import { useStateValue } from '../../../data/StateProvider';
import InnerNav from '../../NavBar/InnerNav';
import PrivateNav from '../../NavBar/PrivateNav';
import OuterNav from '../../NavBar/OuterNav';
// import SettingsIcon from '@mui/icons-material/Settings';
import InventoryIcon from '@mui/icons-material/Inventory';
import HelpIcon from '@mui/icons-material/Help';
import { RiAdminFill } from 'react-icons/ri';
import { useCookies } from "react-cookie";
import axios from "axios";

const drawerWidth= 200


    const useStyles = makeStyles((theme)=>{
        return {
            drawer:{
                width:drawerWidth
            },
            page:{
                width:"100%",
                padding:theme.spacing(3)
        
            },
            drawerpaper:{
                width:drawerWidth
            },
            root:{
                display:'flex'
            },
            active:{
                backgroundColor:"#F1C232",
                color:"#fff",
            },
            appbar:{
                width:`calc(100% - ${drawerWidth}px)`,
                backgroundColor:"#fff",
                color:"#000",
              
            },
            appbaro:{
                width:`100%`,
                backgroundColor:"#fff",
                color:"#000",
              
            },
            toolbar: theme.mixins.toolbar,
     
        }
     
      });
      




const Sidelayout = ({children}) => {
  const [{ user }, dispatch] = useStateValue();
  const [cookies, setCookie, removeCookie] = useCookies(["userjwt"]);


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


      
    const classes= useStyles()  
    const history = useHistory()
    const location = useLocation()

    // const menuItem2 =[
    //     {
    //         text:"Settings",
    //         icon:<SettingsIcon/>,
    //         path:"/settings"
    //     },
    //     {
    //         text:"Support",
    //         icon:<HelpIcon/>,
    //         path:"/support"
    //     },
    //     {
    //         text:"Profile",
    //         icon:<ManageAccountsIcon/>,
    //         path:"/profile"
    //     },
    //     // {
    //     //     text:"Developer",
    //     //     icon:<RiAdminFill/>,
    //     //     path:"/adminfeedback"
    //     // },
    // ]


  return (
      <div className={classes.root}>

{user ? user.showOnce ? 
// inside the app
       <AppBar className={classes.appbar}  elevation={1}>
          <InnerNav/>
       </AppBar>
:
// inprivate page for restriction
       <AppBar className={classes.appbaro}  elevation={1}>
        <PrivateNav/>
       </AppBar>
:
// outerpage
       <AppBar className={classes.appbaro}  elevation={1}>
         <OuterNav/>
       </AppBar>
}

  {user ? user.showOnce ?   <Drawer  
        className={classes.drawer}
        variant="permanent"
        anchor="left"
        classes={{paper:classes.drawerpaper}}
      >
<List>
<ListItem  sx={{ flexGrow: 1 }}>
            <ListItemIcon><PersonIcon/></ListItemIcon>
            <ListItemText primary={user.name}/>
        </ListItem>
        <Divider/>

       <ListItem 
         button 
        key="My Page"
        onClick={()=>history.push("/app")}
        className={location.pathname== "/app" ? classes.active : null} >
            <ListItemIcon><ListIcon/></ListItemIcon>
            <ListItemText primary="My Page"/>
        </ListItem>


        <ListItem 
         button 
        key="Runz"
        onClick={()=>history.push("/runz")}
        className={location.pathname== "/runz" ? classes.active : null} >
            <ListItemIcon><PlayCircleOutlineIcon/></ListItemIcon>
            <ListItemText primary="Runz"/>
        </ListItem>

 

{/* {(user.role==="admin"||user.role==="superadmin")? */}
        <ListItem 
         button 
        key="Procedure"
        onClick={()=>history.push("/procedure")}
        className={location.pathname== "/procedure" ? classes.active : null} >
            <ListItemIcon><AssignmentTurnedInIcon/></ListItemIcon>
            <ListItemText primary="Procedure"/>
        </ListItem>
        {/* :null */}
{/* } */}


{user.role==="student"?  null: 
        <ListItem 
         button 
        key="Inventory"
        onClick={()=>history.push("/inventory")}
        className={location.pathname== "/inventory" ? classes.active : null} >
            <ListItemIcon><InventoryIcon/></ListItemIcon>
            <ListItemText primary="Inventory"/>
        </ListItem>
               
 } 

        <ListItem 
         button 
        key="Add User"
        onClick={()=>history.push("/adduser")}
        className={location.pathname== "/adduser" ? classes.active : null} >
            <ListItemIcon><PersonAddIcon/></ListItemIcon>
            <ListItemText primary="Add User"/>
        </ListItem>



    <br/>
  <Divider/>
  <br/>   <br/>  
     {/* {menuItem2.map(item=>(
        <ListItem 
         button 
        key={item.text}
        onClick={()=>history.push(item.path)}
        className={location.pathname== item.path ? classes.active : null}
     
       
        >
            <ListItemIcon>{item.icon}</ListItemIcon>
            <ListItemText primary={item.text}/>
        </ListItem>
       
    ))} */}
    
{/* {(user.role==="admin"||user.role==="superadmin")? */}

    {user.role==="student"?  null: 
<ListItem 
         button 
        key="Settings"
        onClick={()=>history.push("/settings")}
        className={location.pathname== "/settings" ? classes.active : null} >
            <ListItemIcon><SettingsIcon/></ListItemIcon>
            <ListItemText primary="Settings"/>
        </ListItem>
     
 } 



        <ListItem 
         button 
        key="Support"
        onClick={()=>history.push("/support")}
        className={location.pathname== "/support" ? classes.active : null} >
            <ListItemIcon><HelpIcon/></ListItemIcon>
            <ListItemText primary="Support"/>
        </ListItem>
               
 

        <ListItem 
         button 
        key="Profile"
        onClick={()=>history.push("/profile")}
        className={location.pathname== "/profile" ? classes.active : null} >
            <ListItemIcon><ManageAccountsIcon/></ListItemIcon>
            <ListItemText primary="Profile"/>
        </ListItem>

   
</List>



    
      </Drawer> :null:null }
      <div className={classes.page}>
          <div className={classes.toolbar}></div>
      {children}
      </div>
  </div>
  );
};

export default Sidelayout;


// ///////////////////////////////////////


// import React,{useEffect} from 'react';
// import clsx from 'clsx';
// import { makeStyles, useTheme } from '@material-ui/core/styles';
// import Drawer from '@material-ui/core/Drawer';
// import AppBar from '@material-ui/core/AppBar';
// import Toolbar from '@material-ui/core/Toolbar';
// import List from '@material-ui/core/List';
// import CssBaseline from '@material-ui/core/CssBaseline';
// import Typography from '@material-ui/core/Typography';
// import Divider from '@material-ui/core/Divider';
// import IconButton from '@material-ui/core/IconButton';
// import MenuIcon from '@material-ui/icons/Menu';
// import ChevronLeftIcon from '@material-ui/icons/ChevronLeft';
// import ChevronRightIcon from '@material-ui/icons/ChevronRight';
// import ListItem from '@material-ui/core/ListItem';
// import ListItemIcon from '@material-ui/core/ListItemIcon';
// import ListItemText from '@material-ui/core/ListItemText';
// import InboxIcon from '@material-ui/icons/MoveToInbox';
// import MailIcon from '@material-ui/icons/Mail';
// import { actionTypes } from "../../../data/reducer"
// import LogoutIcon from '@mui/icons-material/Logout';

// import Collapse from '@material-ui/core/Collapse';
// import ExpandLess from '@material-ui/icons/ExpandLess';
// import ExpandMore from '@material-ui/icons/ExpandMore';

// import ListItemButton from '@mui/material/ListItemButton';
// import ManageAccountsIcon from '@mui/icons-material/ManageAccounts';
// import PlayCircleOutlineIcon from '@material-ui/icons/PlayCircleOutline';
// import AssignmentTurnedInIcon from '@material-ui/icons/AssignmentTurnedIn';
// import AccountCircleIcon from '@material-ui/icons/AccountCircle';
// import SettingsIcon from '@material-ui/icons/Settings';
// import ListIcon from '@material-ui/icons/List';
// import PersonIcon from '@mui/icons-material/Person';
// import { useHistory ,useLocation} from "react-router-dom";
// import { useStateValue } from '../../../data/StateProvider';
// import InnerNav from '../../NavBar/InnerNav';
// import PrivateNav from '../../NavBar/PrivateNav';
// import OuterNav from '../../NavBar/OuterNav';
// // import SettingsIcon from '@mui/icons-material/Settings';
// import InventoryIcon from '@mui/icons-material/Inventory';
// import HelpIcon from '@mui/icons-material/Help';
// const drawerWidth = 240;

// const useStyles = makeStyles((theme) => ({
//   root: {
//     display: 'flex',
//   },
//   nested: {
//     paddingLeft: theme.spacing(4),
//   },
//   active:{
//                     backgroundColor:"#F1C232",
//                     color:"#fff",
//                 },
//   page:{
//         width:"100%",
//         padding:theme.spacing(3)       
//                 },
//   appBar: {
//     zIndex: theme.zIndex.drawer + 1,
//     backgroundColor:"#fff",
//                 color:"#000",
//     transition: theme.transitions.create(['width', 'margin'], {
//       easing: theme.transitions.easing.sharp,
//       duration: theme.transitions.duration.leavingScreen,
//     }),
//   },
//   appBarShift: {
//     marginLeft: drawerWidth,
//     width: `calc(100% - ${drawerWidth}px)`,
//     transition: theme.transitions.create(['width', 'margin'], {
//       easing: theme.transitions.easing.sharp,
//       duration: theme.transitions.duration.enteringScreen,
//     }),
//   },
//   menuButton: {
//     marginRight: 36,
//   },
//   hide: {
//     display: 'none',
//   },
//   drawer: {
//     width: drawerWidth,
//     flexShrink: 0,
//     whiteSpace: 'nowrap',
//   },
//   drawerOpen: {
//     width: drawerWidth,
//     transition: theme.transitions.create('width', {
//       easing: theme.transitions.easing.sharp,
//       duration: theme.transitions.duration.enteringScreen,
//     }),
//   },
//   drawerClose: {
//     transition: theme.transitions.create('width', {
//       easing: theme.transitions.easing.sharp,
//       duration: theme.transitions.duration.leavingScreen,
//     }),
//     overflowX: 'hidden',
//     width: theme.spacing(7) + 1,
//     [theme.breakpoints.up('sm')]: {
//       width: theme.spacing(9) + 1,
//     },
//   },
//   toolbar: {
//     display: 'flex',
//     alignItems: 'center',
//     justifyContent: 'flex-end',
//     padding: theme.spacing(0, 1),
//     // necessary for content to be below app bar
//     ...theme.mixins.toolbar,
//   },
//   content: {
//     flexGrow: 1,
//     padding: theme.spacing(3),
//   },
// }));

// export default function Sidelayout({children}) {
//   const classes = useStyles();
//   const theme = useTheme();
//   const history = useHistory()
//   const location = useLocation()
//   const [{ user }, dispatch] = useStateValue();
//   const [open, setOpen] = React.useState(false);
//   const menuItem =[
//             {
//                 text:"My Page",
//                 icon:<ListIcon/>,
//                 path:"/app"
//             },
//             {
//                 text:"Runz",
//                 icon:<PlayCircleOutlineIcon/>,
//                 path:"/runz"
//             },
//             {
//                 text:"Procedure",
//                 icon:<AssignmentTurnedInIcon/>,
//                 path:"/procedure"
//             },
//             {
//                 text:"Inventry",
//                 icon:<InventoryIcon/>,
//                 path:"/inventry"
//             },
//         ]
//         const menuItem2 =[
//             {
//                 text:"Settings",
//                 icon:<SettingsIcon/>,
//                 path:"/settings"
//             },
//             {
//                 text:"Support",
//                 icon:<HelpIcon/>,
//                 path:"/support"
//             },
//             {
//                 text:"Profile",
//                 icon:<ManageAccountsIcon/>,
//                 path:"/profile"
//             },
            // {
            //     text:"Developer",
            //     icon:<RiAdminFill/>,
            //     path:"/adminfeedback"
            // },
//         ]
    

//   const handleDrawerOpen = () => {
//     setOpen(true);
//   };

//   const handleDrawerClose = () => {
//     setOpen(false);
//   };
//   const runz = () => {
//     history.push("/app");
//    }
//    const logoutfun = () => {
//     window.localStorage.clear();
//     return (window.location.href = "/");
//    }
   

//    const [openl, setOpenl] = React.useState(false);

//    const handleClickl= () => {
//      setOpenl(!openl);
//    };

//    useEffect(() => {
//     dispatch({
//       type: actionTypes.SET_USER,
//       user: JSON.parse(localStorage.getItem('userdetail')),
//     });

//       }, []);
 
//   return (
//     <div className={classes.root}>
//       <CssBaseline />
//       <AppBar
//         position="fixed"
//         className={clsx(classes.appBar, {
//           [classes.appBarShift]: open,
//         })}
//       >
       
//         {user ? user.showOnce ?      
//       <Toolbar>
//          <IconButton
//             color="inherit"
//             aria-label="open drawer"
//             onClick={handleDrawerOpen}
//             edge="start"
//             className={clsx(classes.menuButton, {
//               [classes.hide]: open,
//             })}
//           >
//             <MenuIcon />
//           </IconButton> 
//           <Typography onClick={runz} sx={{ flexGrow: 1 }} > <span>Test</span><span style={{backgroundColor:"#F1C232"}}>RunZ</span></Typography>
//           </Toolbar>
//           : 
//           <Toolbar>
//           <Typography  sx={{ flexGrow: 1 }} > <span>Test</span><span style={{backgroundColor:"#F1C232"}}>RunZ</span></Typography>
//           </Toolbar>
//            :
//            <Toolbar>
//             <Typography onClick={logoutfun} sx={{ flexGrow: 1 }} > <span>Test</span><span style={{backgroundColor:"#F1C232"}}>RunZ</span></Typography>
//            </Toolbar>
//             }
      

   
       


      
//       </AppBar>
//       {user ? user.showOnce ?  <Drawer
//         variant="permanent"
//         className={clsx(classes.drawer, {
//           [classes.drawerOpen]: open,
//           [classes.drawerClose]: !open,
//         })}
//         classes={{
//           paper: clsx({
//             [classes.drawerOpen]: open,
//             [classes.drawerClose]: !open,
//           }),
//         }}
//       >
//         <div className={classes.toolbar}>
     
//              <PersonIcon/>
//              <ListItemText primary={user.name}/>
         
//          <Divider/>
//           <IconButton onClick={handleDrawerClose}>
//             {theme.direction === 'rtl' ? <ChevronRightIcon /> : <ChevronLeftIcon />}
//           </IconButton>
//         </div>
//         <Divider />
        
//         <List>

//        <Divider/>
   
//     {menuItem.map(item=>(
//         <ListItem 
//          button 
//         key={item.text}
//         onClick={()=>history.push(item.path)}
//         className={location.pathname== item.path ? classes.active : null}
       
//         >
//             <ListItemIcon>{item.icon}</ListItemIcon>
//             <ListItemText primary={item.text}/>
//         </ListItem>
       
//     ))} 
//     <br/>
//   <Divider/>
//   <br/>   <br/>  
//      {menuItem2.map(item=>(
//         <ListItem 
//          button 
//         key={item.text}
//         onClick={()=>history.push(item.path)}
//         className={location.pathname== item.path ? classes.active : null}
     
       
//         >
//             <ListItemIcon>{item.icon}</ListItemIcon>
//             <ListItemText primary={item.text}/>
//         </ListItem>
       
//     ))}
//      <ListItem >
//         <ListItemIcon>
//           <LogoutIcon />
//         </ListItemIcon>
//         <ListItemText primary="Logout" />
//         {openl ? <ExpandLess  button onClick={handleClickl}/> : <ExpandMore button onClick={handleClickl} />}
//       </ListItem>
//       <Collapse in={openl} timeout="auto" unmountOnExit>
//         <List component="div" disablePadding>
//           <ListItem button className={classes.nested} onClick={logoutfun}>
//             <ListItemText primary="Logout" />
//           </ListItem>
//           </List>
//       </Collapse>

   
// </List>
//       </Drawer> : null : null}

//         <div className={classes.page}>
//            <div className={classes.toolbar}></div>
//        {children}
//        </div>
     
//     </div>
//   );
// }