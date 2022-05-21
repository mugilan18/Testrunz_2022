import React from 'react';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';
import Userprofile from './Usertab/Userprofile';
import Activity from './Usertab/Activity';
import Manageapp from './Settingstab/Manageapp';
import Accesscontrol from './Settingstab/Accesscontrol';
import Customfield from './Settingstab/Customfield';
import Customcolumn from './Settingstab/Customcolumn';
import Adduser from './Settingstab/Adduser';
import Manageuserpanel from './Settingstab/Manage/Manageuserpanel';
import User from './User';
import { useStateValue } from "../../../data/StateProvider";

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

export default function Settings() {
  const classes = useStyles();
  const [value, setValue] = React.useState(0);
  const [{ user }, dispatch] = useStateValue();

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
          {/* <Tab label="Manage App"  {...a11yProps(0)} style={{width:"200px",color:"black"}} />
          <Tab label="Custom Field" {...a11yProps(1)} style={{width:"200px",color:"black"}}/>
          <Tab label="Custom Column" {...a11yProps(2)} style={{width:"200px",color:"black"}}/> */}
          {/* <Tab label="Add User" {...a11yProps(3)} style={{width:"200px",color:"black"}}/> */}
          {user.role !="student"? <Tab label="Manage User" {...a11yProps(0)} style={{width:"200px",color:"black"}}/>: null}
          {/* {user.role ==="superadmin"? <Tab label="Access Control"  {...a11yProps(4)} style={{width:"200px",color:"black"}}/> : null} */}

{/* {console.log(User.role)} */}
        </Tabs>
      </AppBar>
      {/* <TabPanel value={value} index={0}>
       <Manageapp/>
      </TabPanel>
      <TabPanel value={value} index={1}>
    <Customfield/>
      </TabPanel>
      <TabPanel value={value} index={2}>
      <Customcolumn/>
      </TabPanel> */}
      {/* <TabPanel value={value} index={3}>
      <Adduser/>
      </TabPanel> */}
      <TabPanel value={value} index={0}>
      <Manageuserpanel/>
      </TabPanel>
      {/* {user.role ==="superadmin"?
      <TabPanel value={value} index={4}>
      <Accesscontrol/>
      </TabPanel>:null} */}
    </div>
  );
}