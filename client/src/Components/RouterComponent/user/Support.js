import React from 'react';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';

import Helpguide1 from './Supporttab/Helpguide1';
import Releasenotes from './Supporttab/Releasenotes';
import Feedback from './Supporttab/Feedback';


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
         {/* <Tab label="Release Notes"  {...a11yProps(1)} style={{width:"200px",color:"black"}}/> */}
          <Tab label="Feedback" {...a11yProps(0)} style={{width:"200px",color:"black"}}/>
           <Tab label="Help Guide"  {...a11yProps(1)} style={{width:"200px",color:"black"}} />
        </Tabs>
      </AppBar>
      
      {/* <TabPanel value={value} index={1}>
     <Releasenotes/>
      </TabPanel> */}
      <TabPanel value={value} index={0}>
      <Feedback/>
      </TabPanel>
      <TabPanel value={value} index={1}>
       <Helpguide1/>
      </TabPanel>
    </div>
  );
}