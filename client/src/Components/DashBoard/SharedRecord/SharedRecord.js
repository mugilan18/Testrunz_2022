import Grid from "@material-ui/core/Grid";

// import Graph from "../Graph/Graph";
import ApiUrl from "../../../ServerApi";

import Lodaing from "../../RouterComponent/user/Lodaing";



import React, { useEffect } from "react";
import * as html2json from "html2json";
import parse from "html-react-parser";
import axios from "axios";
import { makeStyles } from "@material-ui/core/styles";
import Accordion from "@material-ui/core/Accordion";
import AccordionSummary from "@material-ui/core/AccordionSummary";
import AccordionDetails from "@material-ui/core/AccordionDetails";
import Typography from "@material-ui/core/Typography";
import ExpandMoreIcon from "@material-ui/icons/ExpandMore";
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import { FaDownload } from 'react-icons/fa';
import { ImCloudUpload } from 'react-icons/im';
import { BsFillCalculatorFill } from 'react-icons/bs';
import { useParams} from "react-router-dom";

import "../layout.css"
import Alert from '@mui/material/Alert';
import { GridLoadingOverlay } from "@material-ui/data-grid";

// import { stableValueHash } from "react-query/types/core/utils";
import Snackbar from '@mui/material/Snackbar';
import jsPDF from "jspdf"
import { SiMicrosoftword } from 'react-icons/si';
import ApiService from "../../../Sevices/ApiService";
const useStyles = makeStyles({
  root: {
    width: "1000px",
  },
  paper: {},
});

const SharedRecord = ({ data ,datavalues }) => {

  const classes = useStyles();
  const [htmlContext, setHtmlContext] = React.useState(null);
  const [statusmessagee, setStatusmessagee] = React.useState("")
  const [statusmessages, setStatusmessages] = React.useState("")
  const [opene, setOpene] = React.useState(false);
  const [opens, setOpens] = React.useState(false);
  const [result, setResult] = React.useState({});
  const [errorvalue, setErrorvalue]=React.useState();
  const [accord, setAccord] = React.useState(false);
  const [output,setOutput]=React.useState({})
  const vertical ="button"
  const horizontal = "center"
  let {token} = useParams();
  //console.log({ ...data });
  React.useEffect(() => {
  console.log("data",data)
    axios
      .get(`${ApiUrl}/procedures/search/${data.experimentName}`)
      .then((res) => {
        setHtmlContext((prev) => {
          if (prev === null) return res.data;
        });
        fetch(`${ApiUrl}/experiments/${token}`)
        .then((res)=>res.json())
        .then(data =>{
          // console.log("check here",data)
          const datavalues =data.datas
          console.log("datas are",datavalues)
          const filtered = Object.entries(data.datas).filter(([key, value]) => key != '');
          const obj = Object.fromEntries(filtered)
    
          for (const [key, values] of Object.entries(obj)) {
    
            document.getElementById(key).value=values
             }
             setOpens(true);
            setStatusmessages('Data has been Retrived')
    
    
    
    
    
    
    
    
    
    
    
    
            console.log(datavalues)
            fetch(`${ApiUrl}/runPython/`, {
              method: "POST",
              body: JSON.stringify({
                ...datavalues,
                title: `${data && data?.experimentName}`,
              }),
              headers: { "Content-Type": "application/json" },
            }).then((responce)=>responce.json())
            .then((data)=>{
              console.log("result",data);
             setResult( data)
             setOpens(true);
              setStatusmessages('Calculation Completed')
              setAccord(true)
            })
            .catch((error) => {
              setOpene(true);
              setErrorvalue("Check the values you have Entered")
              setStatusmessagee("Check the values you have Entered")
            });
    
    
    
    
    
    
    
    
    
    
        
        } )
        .catch((error) => {
          setOpene(true);
          setStatusmessagee('Error In data Retrive')
          console.log("error is",error)
        });
    
    
    
    
      });
  }, [data.experimentName]);

  const handleClosee = (event, reason) => {
    if (reason === 'clickaway') {
      return;
    }
    setOpene(false);
  
  };
  const handleCloses = (event, reason) => {
    if (reason === 'clickaway') {
      return;
    }
    setOpens(false);
  
  };
  const accordchange=()=>{
    setAccord(!accord)
  }
  const uses = htmlContext?.html.child.map((ele) => ele);
  return (
    <>
      <Grid container className={classes.root} spacing={2}>
        <Grid item >
          <div className={classes.paper}>
            <h1>Submitted section</h1>
           
             {/* <Contextshared value={htmlContext} dataV={data} datavalues={datavalues}/>  */}
             {htmlContext? 
         <div >
           {/* <div id="generator" style={{width:"600px", padding:"50px"}}> */}
           <div id="generator" >
          <div className="containeer">
            <form >
                {
                uses.map((el) =>
                  parse(htmlContext?.html && html2json.json2html(el))
                )} 
               
            </form>
      
          </div>
          <br /><br />
          <Accordion  expanded={accord}>
            <AccordionSummary
            expandIcon={<ExpandMoreIcon />}
            aria-controls="panel1bh-content"
            id="panel1bh-header"    
            onClick={accordchange}         
            >
              <Typography className={classes.heading}>Result</Typography>
            </AccordionSummary>
            <AccordionDetails>
              <Typography>
                <p>Result will be shown here</p>
                {errorvalue? <p style={{color:"red"}}>*{errorvalue}*</p>:
                Object.keys(result).map((item) => {
                  return Object.keys(result[item][0]).map((i) => {
                    return (
                      
                       <p>{i} : {result[item][0][i]}</p> 
                         
                        
                      
                    );
                  });
                })
                // <p>{output}</p>
              }
              </Typography>
            </AccordionDetails>
          </Accordion>
          </div>
          <br /><br />
          <Stack spacing={2} direction="row" style={{ position: "relative", left: "25%" }}>
      
     
      {/* <Button variant="contained" onClick={generate}>generate &nbsp;&nbsp;&nbsp;<GrDocumentPdf/></Button> */}
     
    </Stack>
    <Snackbar open={opene} autoHideDuration={3000} onClose={handleClosee} anchorOrigin={{ vertical, horizontal }}>
        <Alert onClose={handleClosee} severity="error" sx={{ width: '100%' }}>
          {statusmessagee}
        </Alert>
      </Snackbar>
      <Snackbar open={opens} autoHideDuration={3000} onClose={handleCloses} anchorOrigin={{ vertical, horizontal }}>
        <Alert onClose={handleCloses} severity="success" sx={{ width: '100%' }}>
          {statusmessages}
        </Alert>
      </Snackbar>

         
          {/* <Button onClick={call}>call</Button> */}
        </div> 
        :<Lodaing/>}
          </div>
        </Grid>

      </Grid>
    </>
  );
};

export default SharedRecord;
