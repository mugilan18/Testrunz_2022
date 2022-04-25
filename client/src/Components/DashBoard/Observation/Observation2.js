// import React from "react";
// import { makeStyles } from "@material-ui/core/styles";
// import Grid from "@material-ui/core/Grid";
// import axios from "axios";
// import Context from "../Context";
// // import Graph from "../Graph/Graph";
// import ApiUrl from "../../../ServerApi";
// const useStyles = makeStyles({
//   root: {
//     width: "1000px",
//   },
//   paper: {},
// });

// const Observation = ({ data }) => {
//   // let graph;
//   // if (
//   //   data.experimentName === "Lee's Disc Method" ||
//   //   data.experimentName === "Polarimeter"
//   // ) {
//   //   graph = true;
//   // } else {
//   //   graph = false;
//   // }
//   const classes = useStyles();
//   const [htmlContext, setHtmlContext] = React.useState(null);
//   //console.log({ ...data });
//   React.useEffect(() => {
//     axios
//       .get(`${ApiUrl}/procedures/search/${data.experimentName}`)
//       .then((res) => {
//         setHtmlContext((prev) => {
//           if (prev === null) return res.data;
//         });
       
//       });
//   }, [data.experimentName]);
  
//   return (
//     <>
//       <Grid container className={classes.root} spacing={2}>
//         <Grid item xs={7}>
//           <div className={classes.paper}>
//             <h1>Observation section</h1>
//             <Context value={htmlContext} dataV={data} />
//           </div>
//         </Grid>
//         {/* <Grid item xs={5}>
//           <div className={classes.paper}>{graph && <Graph data={data} />}</div>
//         </Grid> */}
//       </Grid>
//     </>
//   );
// };

// export default Observation;


import Grid from "@material-ui/core/Grid";

import Graph from "../Graph/Graph";
import ApiUrl from "../../../ServerApi";

import Lodaing from "../../RouterComponent/user/Lodaing";

import CanvasJSReact from "../NewGraph/assets/canvasjs.react";
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
import "../layout.css"
import Alert from '@mui/material/Alert';
import { GridLoadingOverlay } from "@material-ui/data-grid";
import { useParams} from "react-router-dom";

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

const Observation = ({ data ,datavalues }) => {
  var CanvasJSChart = CanvasJSReact.CanvasJSChart;

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
  const [data1, setData1] = React.useState({});
  const [toogle,setToogle]=React.useState(false);
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
              ////////////////////
              function call(){
                setOpene(true)
                setErrorvalue("Check the values you have Entered")
                setStatusmessagee("Check the values you have Entered")
              }
              setTimeout(
                call()
              , 1000);
            
              /////////////
            });
    
    
    
    
    
    
    
    
    
    
        
        } )
        .catch((error) => {
          setOpene(true);
          setStatusmessagee('Error In data Retrive')
          console.log("error is",error)
        });
    
    
    
    
      });
  }, [data.experimentName]);


// initial the input 
  function init() {
    // setInputEl(document.querySelectorAll("input"))
    let inputEl = document.querySelectorAll("input");
     console.log(inputEl)
    //  console.log(inputElArr)
     inputEl.forEach((ele) => {
      const { name, value } = ele;
      setData1((prev) => ({ ...prev, [name]: value ?? "1" }));
      ele.onChange = (e) => {
        const { name, value } = e.target;
        setData1((prev) => ({ ...prev, [name]: value }));
      };
    });
  }

// retrive
  const retrive = async(event) => {
    event.preventDefault();
    fetch(`${ApiUrl}/experiments/${token}`)
    .then((res)=>res.json())
    .then(data =>{
      // console.log("check here",data)
      const filtered = Object.entries(data.datas).filter(([key, value]) => key != '');
      const obj = Object.fromEntries(filtered)

      for (const [key, values] of Object.entries(obj)) {

        document.getElementById(key).value=values
         }
         setOpens(true);
        setStatusmessages('Data has been Retrived')
    
    } )
    .catch((error) => {
      setOpene(true);
      setStatusmessagee('Error In data Retrive')
    });
 

  }


// generate word
const  Export2Doc=(element, filename = '')=>{
  var preHtml = "<html xmlns:o='urn:schemas-microsoft-com:office:office' xmlns:w='urn:schemas-microsoft-com:office:word' xmlns='http://www.w3.org/TR/REC-html40'><head><meta charset='utf-8'><title>Export HTML To Doc</title></head><body>";
  var postHtml = "</body></html>";
  var html = preHtml+document.getElementById(element).innerHTML+postHtml;
  var blob = new Blob(['\ufeff', html],{
      type: 'application/msword'
  });
  var url = 'data:application/vnd.ms-word;charset=utf-8,' + encodeURIComponent(html)
  filename = filename?filename+'.doc': 'document.doc';
  var downloadLink = document.createElement("a");
  document.body.appendChild(downloadLink);
  if(navigator.msSaveOrOpenBlob){
      navigator.msSaveOrOpenBlob(blob, filename);
  }else{
      downloadLink.href = url;
      downloadLink.download = filename;
      downloadLink.click();
  }
  document.body.removeChild(downloadLink);
}
    
useEffect(() => {
  init()
  
}, []);





// calculate
const Calculate = (event) => {
  
  event.preventDefault();
  init()
  
  console.log("data to calc",data1);
  let vals = Object.values(data1)
 
  const empty = vals.filter(item => item  === "");
  const tosent  = delete data1[""]


  if (empty.length > 0){
    setErrorvalue("Must fill all Required Readings")
    setOpene(true);
    setStatusmessagee('Must fill all Required Readings')
  }
  else if(empty.length === 0){
    setErrorvalue()
    setResult({})
    let resultval ={}
  
 
  fetch(`${ApiUrl}/runPython/`, {
    method: "POST",
    body: JSON.stringify({
      ...data1,
      title: `${data && data?.experimentName}`,
    }),
    headers: { "Content-Type": "application/json" },
  }).then((responce)=>responce.json())
  .then((data)=>{
    console.log("result",data);
  //  setResult( data)
   generategraph(data)
  //  setOpens(true);
  //   setStatusmessages('Calculation Completed')
  //   setAccord(true)
  })
  .catch((error) => {
    setOpene(true);
    setErrorvalue("Check the values you have Entered")
    setStatusmessagee("Check the values you have Entered")
  });

//   setIsData((prev) => !prev);
// if(resultval){
//   setResult(resultval)
// }
}
}

/////////////generate graph




const generategraph=(data)=>{
  setToogle(false)
  var dataPoints = [];
 console.log("graph dta ",data)
  for (var i = 0; i < 6; i++) {
    dataPoints.push({
      x: data.ans.x1[i],
      y: data.ans. y1[i]
    });
    }
  const options = {
    animationEnabled: true,
          
          title:{
            text: data.ans.title
          },
          axisX:
        {
          title: data.ans.axisXtitle,
        },
          axisY:{
            title: data.ans.axisYtitle,
            includeZero: false,
          
          },
          data: [{
            type: "line",
            dataPoints: dataPoints
      
          }]
        }

        setResult(options)
        // setToogle(true)
}


//function to update the data 
const updateval = (event) => {
   
      
   
  event.preventDefault();
  init()
  
  console.log("data to send",data1);
  let vals = Object.values(data1)
 
  const empty = vals.filter(item => item  === "");
  const tosent  = delete data1[""]
  if (empty.length > 0){
    setErrorvalue("Must fill all Required Readings")
    setOpene(true);
  setStatusmessagee('No data is uploaded refresh and try again')
  }

  
  else if(empty.length === 0){
  init()
  // console.log("check", event)
  // console.log("check data legth ",Object.values(data).length)
  // console.log("check ele length ",inputEl.length )
  // console.log("check data ",Object.values(data))
  // console.log("check data ",Object.keys(data))
  // console.log("check ele ",inputEl )
 

  fetch(`${ApiUrl}/experiments/`, {
    method: "PATCH",
    body: JSON.stringify({ ...data1, id: window.location.href.split("/")[5] }),
    headers: { "Content-type": "application/json" },
  })
    .then(res => {console.log("result", res)
    setOpens(true);
    setStatusmessages('Your work has been saved')
  }
    )
    .catch((error) => {
      // console.error('Error:', error);
      setOpene(true);
      setStatusmessagee('something went wrong Try again')
    });

}}


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
            <h1>Observation section</h1>
  
             {/* <Contextshared value={htmlContext} dataV={data} datavalues={datavalues}/>  */}
             {htmlContext? 
         <div >
           {/* <div id="generator" style={{width:"600px", padding:"50px"}}> */}
           <div id="generator" >
          <div className="containeer">
            <form onChange={init}>
                {
                uses.map((el) =>
                  parse(htmlContext?.html && html2json.json2html(el))
                )} 
               
            </form>
            <Button variant="contained"
                style={{ position: "relative", left: "40%", top: "2%", backgroundColor:"#F1C232",color:"black"}}
                onClick={Calculate}
              >
                Calculate Result &nbsp;&nbsp;&nbsp;
                <BsFillCalculatorFill/>
                </Button>
          </div>
          <br /><br />
          {/* {data &&<Graph data={data} />} */}
         {/* {toogle? <CanvasJSChart options = {result} /> :null} */}
       {result? <CanvasJSChart options = {result} /> : null }
          {/* <Accordion  expanded={accord}>
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
          </Accordion> */}
          </div>
          <br /><br />
          <Stack spacing={2} direction="row" style={{ position: "relative", left: "25%" }}>
          <Button variant="contained"   style={{ backgroundColor:"#F1C232",color:"black" }} onClick={retrive}>Retrive &nbsp;&nbsp;&nbsp;<FaDownload/></Button>
      <Button variant="contained"   style={{ backgroundColor:"#F1C232",color:"black" }} onClick={updateval}>Save &nbsp;&nbsp;&nbsp;<ImCloudUpload/></Button>
      {/* <Button variant="contained" onClick={generate}>generate &nbsp;&nbsp;&nbsp;<GrDocumentPdf/></Button> */}
      <Button variant="contained"   style={{ backgroundColor:"#F1C232",color:"black" }} onClick={()=>Export2Doc('generator', 'test')}>generate &nbsp;&nbsp;&nbsp;<SiMicrosoftword/></Button>

     
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
        </div> 
        :<Lodaing/>}
          </div>
        </Grid>

      </Grid>
    </>
  );
};

export default Observation;

