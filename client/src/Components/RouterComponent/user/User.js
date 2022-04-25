import React,{useEffect} from 'react';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';
import Userprofile from './Usertab/Userprofile';
import Activity from './Usertab/Activity';
import { actionTypes } from "../../../data/reducer"
import { useStateValue } from '../../../data/StateProvider';
import { useCookies } from "react-cookie";
import axios from "axios";
function TabPanel(props) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box p={3}>
          <Typography>{children}</Typography>
        </Box>
      )}
    </div>
  );
}

TabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.any.isRequired,
  value: PropTypes.any.isRequired,
};

function a11yProps(index) {
  return {
    id: `simple-tab-${index}`,
    'aria-controls': `simple-tabpanel-${index}`,
  };
}

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    backgroundColor: theme.palette.background.paper,
    width:"100%"
  },
}));

export default function User() {
  const classes = useStyles();
  const [value, setValue] = React.useState(0);
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

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <div className={classes.root}>
      
      <AppBar position="static" >
        <Tabs value={value} onChange={handleChange} aria-label="simple tabs example" style={{background: '#F1C232'}} 
        TabIndicatorProps={{  
      style: {
          // display: "none",
          backgroundColor:"white"
      },
    }}  >
          <Tab label="Profile"  {...a11yProps(0)} style={{width:"200px",color:"black"}} />
          <Tab label="Activity"  {...a11yProps(1)} style={{width:"200px",color:"black"}}/>

        </Tabs>
      </AppBar>
      <TabPanel value={value} index={0}>
        <Userprofile/>
      </TabPanel>
      <TabPanel value={value} index={1}>
      <Activity />
      </TabPanel>
  
    </div>
  );
}
