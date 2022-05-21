import React from "react";
import axios from "axios";
import PropTypes from "prop-types";
import { makeStyles } from "@material-ui/core/styles";
import Tabs from "@material-ui/core/Tabs";
import Tab from "@material-ui/core/Tab";
import Box from "@material-ui/core/Box";
import AppBar from '@material-ui/core/AppBar';

import TextField from "@material-ui/core/TextField";
import MenuItem from "@material-ui/core/MenuItem";
import FormHelperText from "@material-ui/core/FormHelperText";
import FormControl from "@material-ui/core/FormControl";
import Select from "@material-ui/core/Select";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import Typography from "@material-ui/core/Typography";
import Divider from "@material-ui/core/Divider";

/* import { withStyles } from "@material-ui/core/styles";
import { green } from "@material-ui/core/colors";
import Radio from "@material-ui/core/Radio"; */

import Observation from "./Observation/Observation";
import Record from "./Record/Record";
import Notes from "./Notes/Notes";
import ApiUrl from "../../ServerApi";
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
    id: `vertical-tab-${index}`,
    "aria-controls": `vertical-tabpanel-${index}`,
  };
}

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    backgroundColor: theme.palette.background.paper,
    width:"100%"
  },
  card:{
    // paddingTop:"100px"
  }
}));
/* const GreenRadio = withStyles({
  root: {
    color: green[400],
    "&$checked": {
      color: green[600],
    },
  },
  checked: {},
})((props) => <Radio color="default" {...props} />); */

export default function VerticalTabs({ data }) {
  const classes = useStyles();
  const [value, setValue] = React.useState(0);
  const [selectedValue, setSelectedValue] = React.useState("");

  React.useEffect(() => {
    async function fetchData() {
      let defaultString = "add something here";
      await axios
        .post(`${ApiUrl}/notes`, {
          runID: data.runID,
          notes: defaultString,
        })
        .then((res) => { });
    }

    if (data.runID) fetchData();
  }, [data.runID]);

  const handleChangeRadio = (event) => {
    setSelectedValue(event.target.value);
  };

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <>
      {/* <FormControl className={classes.formControl}>
        <Select
          value={selectedValue}
          onChange={handleChangeRadio}
          displayEmpty
          className={classes.selectEmpty}
          inputProps={{ "aria-label": "Without label" }}
        >
          <MenuItem value="d">
            <em>None</em>
          </MenuItem>
          <MenuItem value="a">Remote</MenuItem>
          <MenuItem value="b">Manual</MenuItem>
          <MenuItem value="c">Automated</MenuItem>
        </Select>
        <FormHelperText>Data Connection Type</FormHelperText>
      </FormControl>
      {selectedValue === "a" ? (
        <span>
          <TextField
            id="outlined-basic"
            label="Enter Data Source IP Here"
            variant="outlined"
            style={{ height: "5px", marginTop: "2%" }}
          />
        </span>
      ) : (
        null
      )} */}
      <Card className={classes.card}>
        <CardContent>
          <Typography
            className={classes.title}
            color="textSecondary"
            gutterBottom
          >
            {data.studentName} started {data.experimentName} from {data.labType}
          </Typography>
        </CardContent>
      </Card>
      <Divider />
      <div className={classes.root}>
      {/* <Record data={data} /> */}
      <AppBar position="static" style={{width:"100%"}}>
        <Tabs value={value} onChange={handleChange} aria-label="simple tabs example" style={{background: '#F1C232'}} 
        TabIndicatorProps={{  
      style: {
          // display: "none",
          backgroundColor:"white"
      },
    }}  >
          <Tab label="Observation" {...a11yProps(0)} />
          <Tab label="Record" {...a11yProps(1)} />
          <Tab label="Notes" {...a11yProps(3)} />
          </Tabs>
      </AppBar>
        <TabPanel value={value} index={0}>
          <Observation data={data} />
        </TabPanel>
        <TabPanel value={value} index={1}>
          <Record data={data} />
        </TabPanel>
        <TabPanel value={value} index={2}>
          <Notes data={data} />
        </TabPanel>
      </div>
    </>
  );
}
