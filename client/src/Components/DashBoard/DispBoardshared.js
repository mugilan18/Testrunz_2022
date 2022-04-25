import React from "react";
import axios from "axios";
import PropTypes from "prop-types";
import { makeStyles } from "@material-ui/core/styles";
import Tabs from "@material-ui/core/Tabs";
import Tab from "@material-ui/core/Tab";
import Box from "@material-ui/core/Box";

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
import SharedRecord from "./SharedRecord/SharedRecord";
import Notes from "./Notes/Notes";
import ApiUrl from "../../ServerApi";
// function TabPanel(props) {
//   const { children, value, index, ...other } = props;

//   return (
//     <div
//       role="tabpanel"
//       hidden={value !== index}
//       id={`vertical-tabpanel-${index}`}
//       aria-labelledby={`vertical-tab-${index}`}
//       {...other}
//     >
//       {value === index && (
//         <Box p={3}>
//           <div>{children}</div>
//         </Box>
//       )}
//     </div>
//   );
// }

// TabPanel.propTypes = {
//   children: PropTypes.node,
//   index: PropTypes.any.isRequired,
//   value: PropTypes.any.isRequired,
// };

// function a11yProps(index) {
//   return {
//     id: `vertical-tab-${index}`,
//     "aria-controls": `vertical-tabpanel-${index}`,
//   };
// }

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    backgroundColor: theme.palette.background.paper,
    display: "flex",
    height: "80vh",
    marginLeft: "-50px",
  
  },
  tabs: {
    borderRight: `1px solid ${theme.palette.divider}`,
  },
  formControl: {
    margin: theme.spacing(1),
    minWidth: 120,
  },
  selectEmpty: {
    marginTop: theme.spacing(2),
  },
  title: {
    fontSize: 14,
  },
  card: {
    height: "8%",
    width: "40%",
    position: "absolute",
    top: "5%",
    left: "45%",
  },
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

export default function VerticalTabs({ data ,datavalues}) {
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



  return (
    <>
     
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
      <SharedRecord data={data} datavalues={datavalues} />

      </div>
    </>
  );
}
